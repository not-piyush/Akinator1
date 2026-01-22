ANIMALS = {
    "candidates": [
        {
            "name": "Dog 🐶",
            "is_living": True, "is_animal": True, "is_pet": True, "is_mammal": True,
            "size_large": False, "domestic": True, "wild": False, "aggressive": False,
            "barks": True, "meows": False, "flies": False, "water_animal": False,
            "has_fur": True, "four_legs": True, "nocturnal": False, "cold_region": False,
        },
        {
            "name": "Cat 🐱",
            "is_living": True, "is_animal": True, "is_pet": True, "is_mammal": True,
            "size_large": False, "domestic": True, "wild": False, "aggressive": False,
            "barks": False, "meows": True, "flies": False, "water_animal": False,
            "has_fur": True, "four_legs": True, "nocturnal": True, "cold_region": False,
        },
        {
            "name": "Rabbit 🐰",
            "is_living": True, "is_animal": True, "is_pet": True, "is_mammal": True,
            "size_large": False, "domestic": True, "wild": False, "aggressive": False,
            "barks": False, "meows": False, "flies": False, "water_animal": False,
            "has_fur": True, "four_legs": True, "nocturnal": False, "cold_region": False,
        },

        # 🦁 WILD LAND ANIMALS
        {
            "name": "Lion 🦁",
            "is_living": True, "is_animal": True, "is_pet": False, "is_mammal": True,
            "size_large": True, "domestic": False, "wild": True, "aggressive": True,
            "barks": False, "meows": False, "flies": False, "water_animal": False,
            "has_fur": True, "four_legs": True, "nocturnal": True, "cold_region": False,
        },
        {
            "name": "Tiger 🐯",
            "is_living": True, "is_animal": True, "is_pet": False, "is_mammal": True,
            "size_large": True, "domestic": False, "wild": True, "aggressive": True,
            "barks": False, "meows": False, "flies": False, "water_animal": False,
            "has_fur": True, "four_legs": True, "nocturnal": True, "cold_region": False,
        },
        {
            "name": "Elephant 🐘",
            "is_living": True, "is_animal": True, "is_pet": False, "is_mammal": True,
            "size_large": True, "domestic": False, "wild": True, "aggressive": False,
            "barks": False, "meows": False, "flies": False, "water_animal": False,
            "has_fur": False, "four_legs": True, "nocturnal": False, "cold_region": False,
        },
        {
            "name": "Bear 🐻",
            "is_living": True, "is_animal": True, "is_pet": False, "is_mammal": True,
            "size_large": True, "domestic": False, "wild": True, "aggressive": True,
            "barks": False, "meows": False, "flies": False, "water_animal": False,
            "has_fur": True, "four_legs": True, "nocturnal": True, "cold_region": True,
        },

        # 🐦 BIRDS
        {
            "name": "Eagle 🦅",
            "is_living": True, "is_animal": True, "is_pet": False, "is_mammal": False,
            "size_large": False, "domestic": False, "wild": True, "aggressive": True,
            "barks": False, "meows": False, "flies": True, "water_animal": False,
            "has_fur": False, "four_legs": False, "nocturnal": False, "cold_region": True,
        },
        {
            "name": "Parrot 🦜",
            "is_living": True, "is_animal": True, "is_pet": True, "is_mammal": False,
            "size_large": False, "domestic": True, "wild": False, "aggressive": False,
            "barks": False, "meows": False, "flies": True, "water_animal": False,
            "has_fur": False, "four_legs": False, "nocturnal": False, "cold_region": False,
        },
        {
            "name": "Owl 🦉",
            "is_living": True, "is_animal": True, "is_pet": False, "is_mammal": False,
            "size_large": False, "domestic": False, "wild": True, "aggressive": False,
            "barks": False, "meows": False, "flies": True, "water_animal": False,
            "has_fur": False, "four_legs": False, "nocturnal": True, "cold_region": False,
        },

        # 🌊 WATER ANIMALS
        {
            "name": "Shark 🦈",
            "is_living": True, "is_animal": True, "is_pet": False, "is_mammal": False,
            "size_large": True, "domestic": False, "wild": True, "aggressive": True,
            "barks": False, "meows": False, "flies": False, "water_animal": True,
            "has_fur": False, "four_legs": False, "nocturnal": False, "cold_region": False,
        },
        {
            "name": "Dolphin 🐬",
            "is_living": True, "is_animal": True, "is_pet": False, "is_mammal": True,
            "size_large": False, "domestic": False, "wild": True, "aggressive": False,
            "barks": False, "meows": False, "flies": False, "water_animal": True,
            "has_fur": False, "four_legs": False, "nocturnal": False, "cold_region": False,
        },
        {
            "name": "Octopus 🐙",
            "is_living": True, "is_animal": True, "is_pet": False, "is_mammal": False,
            "size_large": False, "domestic": False, "wild": True, "aggressive": False,
            "barks": False, "meows": False, "flies": False, "water_animal": True,
            "has_fur": False, "four_legs": False, "nocturnal": True, "cold_region": False,
        },

        # ❄️ COLD REGION
        {
            "name": "Penguin 🐧",
            "is_living": True, "is_animal": True, "is_pet": False, "is_mammal": False,
            "size_large": False, "domestic": False, "wild": True, "aggressive": False,
            "barks": False, "meows": False, "flies": False, "water_animal": True,
            "has_fur": False, "four_legs": False, "nocturnal": False, "cold_region": True,
        },
        {
            "name": "Polar Bear 🐻‍❄️",
            "is_living": True, "is_animal": True, "is_pet": False, "is_mammal": True,
            "size_large": True, "domestic": False, "wild": True, "aggressive": True,
            "barks": False, "meows": False, "flies": False, "water_animal": False,
            "has_fur": True, "four_legs": True, "nocturnal": False, "cold_region": True,
        },

        # 🐍 REPTILES / INSECTS
        {
            "name": "Snake 🐍",
            "is_living": True, "is_animal": True, "is_pet": False, "is_mammal": False,
            "size_large": False, "domestic": False, "wild": True, "aggressive": True,
            "barks": False, "meows": False, "flies": False, "water_animal": False,
            "has_fur": False, "four_legs": False, "nocturnal": True, "cold_region": False,
        },
        {
            "name": "Ant 🐜",
            "is_living": True, "is_animal": True, "is_pet": False, "is_mammal": False,
            "size_large": False, "domestic": False, "wild": True, "aggressive": False,
            "barks": False, "meows": False, "flies": False, "water_animal": False,
            "has_fur": False, "four_legs": True, "nocturnal": False, "cold_region": False,
        },
        {
            "name": "Lady Bug 🐞",
            "is_living": True, "is_animal": True, "is_pet": False, "is_mammal": False,
            "size_large": False, "domestic": False, "wild": True, "aggressive": False,
            "barks": False, "meows": False, "flies": True, "water_animal": False,
            "has_fur": False, "four_legs": False, "nocturnal": False, "cold_region": False,
        }
    ],

    "questions": [
        ("Is it a living being?", "is_living"),
        ("Is it an animal?", "is_animal"),
        ("Is it a pet?", "is_pet"),
        ("Is it a mammal?", "is_mammal"),
        ("Is it large in size?", "size_large"),
        ("Is it domestic?", "domestic"),
        ("Is it wild?", "wild"),
        ("Is it aggressive?", "aggressive"),
        ("Does it bark?", "barks"),
        ("Does it meow?", "meows"),
        ("Can it fly?", "flies"),
        ("Does it live in water?", "water_animal"),
        ("Does it have fur?", "has_fur"),
        ("Does it have four legs?", "four_legs"),
        ("Is it nocturnal?", "nocturnal"),
        ("Does it live in cold regions?", "cold_region"),
    ]
}
