class AkinatorEngine:
    def __init__(self, data, update_ui):
        self.data = data
        self.update_ui = update_ui
        self.MAX_QUESTIONS = 10
        self.MIN_GUESS_QUESTIONS = 6
        self.CONFIDENCE_THRESHOLD = 70
        self.reset()

    def reset(self):
        self.all_candidates = self.data["candidates"]
        self.candidates = self.all_candidates[:]
        self.questions = self.data["questions"]
        self.asked = set()
        self.q_count = 0
        self.current = None

    def start(self):
        self.ask_next()

    def compute_confidence(self):
        candidate_conf = 1 - (len(self.candidates) / len(self.all_candidates))
        question_conf = self.q_count / self.MAX_QUESTIONS
        return int((0.7 * candidate_conf + 0.3 * question_conf) * 100)

    def choose_best_question(self):
        best = None
        best_score = 0

        for text, key in self.questions:
            if key in self.asked:
                continue

            yes = sum(1 for c in self.candidates if c.get(key) is True)
            no = sum(1 for c in self.candidates if c.get(key) is False)

            score = min(yes, no)
            if score > best_score:
                best_score = score
                best = (text, key)

        return best

    def ask_next(self):
        confidence = self.compute_confidence()

        if (
            self.q_count >= self.MIN_GUESS_QUESTIONS
            and confidence >= self.CONFIDENCE_THRESHOLD
        ):
            self.finish(force=False)
            return

        # Hard stop
        if self.q_count >= self.MAX_QUESTIONS or len(self.candidates) <= 1:
            self.finish(force=True)
            return

        next_q = self.choose_best_question()
        if not next_q:
            self.finish(force=True)
            return

        self.current = next_q
        text, _ = next_q

        self.update_ui(
            f"🤔 {text}\n\nQuestion {self.q_count + 1}/{self.MAX_QUESTIONS}\nConfidence: {confidence}%",
            False,
            confidence
        )

    def answer(self, yes):
        _, key = self.current
        self.candidates = [c for c in self.candidates if c.get(key) == yes]
        self.asked.add(key)
        self.q_count += 1
        self.ask_next()

    def finish(self, force):
        confidence = self.compute_confidence()

        if not self.candidates:
            self.update_ui("😢 I’m out of ideas.", True, confidence)
            return

        guess = self.candidates[0]["name"]

        message = (
            f"🎯 My guess:\n\n{guess}\n\nConfidence: {confidence}%"
            if not force
            else f"⏹ Final guess:\n\n{guess}\n\nConfidence: {confidence}%"
        )

        self.update_ui(message, True, confidence)
