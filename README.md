## Possible Pull Requests 

### Easy

1. **Add a new item to a category**
   - Example: Add a new animal, food item, Pokémon, or character.
   - Requirement: Fill **all existing attributes** for the new item.
   - *Hint:* Copy an existing item and modify the values carefully.

2. **Improve question wording**
   - Make a question more natural or clearer.
   - *Hint:* Only change the text, not the attribute key.

3. **Reorder questions for better flow**
   - Move broader questions earlier and specific ones later.
   - *Hint:* Early questions should split the list roughly in half.

4. **Fix spelling or capitalization**
   - Text-only fixes anywhere in the repository.
   - *Hint:* Small changes are still valid and valuable PRs.

---

### Easy–Medium

5. **Add a visual confidence indicator**
   - Display confidence as a progress bar instead of only text.
   - *Hint:* Tkinter’s `ttk.Progressbar` can be updated dynamically.

6. **Show question count separately**
   - Display `Question X / 10` as a separate label in the UI.
   - *Hint:* The engine already tracks how many questions were asked.

7. **Skip ineffective questions**
   - Automatically skip questions that don’t split remaining candidates.
   - *Hint:* If all remaining candidates give the same answer, the question adds no information.

8. **Randomize question selection**
   - When multiple good questions exist, randomly choose one to improve replayability.
   - *Hint:* You don’t need full randomness-randomly choosing among the best few is enough.

---

### Medium 

9. **Add “Why I guessed this” explanation**
   - After guessing, show which attributes led to the final guess.
   - *Hint:* Track which questions were answered “Yes” during the game.

10. **Add an Undo / Back button**
    - Allow users to undo the last Yes/No answer.
    - *Hint:* Store previous candidate lists and restore them when undoing.

---

### Contribution Guidelines

- Follow existing data structures exactly.
- Do not remove or rename attributes.
- Keep pull requests small and focused.
- Clearly explain *what* you changed and *why* in the PR description.
