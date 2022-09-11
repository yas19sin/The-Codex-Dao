"""
Create a list of 10 random Xianxia/Xuanhuan Special Physiques and print one out
"""

import random

# List of Special Physiques
special_physiques = [
    "Dragon",
    "Phoenix",
    "Qilin",
    "Kirin",
    "Unicorn",
    "Phoenix",
    "Tortoise",
    "Tiger",
    "Lion",
    "Wolf",
    "Snake",
    "Eagle",
    "Demonic",
    "Divine",
    "Heavenly",
    "Earthly",
    "Human",
    "Devil",
    "God",
    "Immortal",
    "Demon"
]

# List of Special Physiques nicknames
special_physiques_essence = [
    "Blood",
    "Bone",
    "Body",
    "Breath",
    "Chakra",
    "Chi",
    "Cultivation",
    "Curse",
    "Earth",
    "Energy",
    "Essence",
    "Eye",
    "Fire",
    "Force",
    "Fury",
    "Heart",
    "Karma",
    "Life",
    "Light",
    "Mana",
    "Mind",
    "Moon",
    "Mystic",
    "Nature",
    "Nether",
    "Origin",
    "Power",
    "Qi",
    "Shadow",
    "Soul",
    "Spirit",
    "Star",
    "Sun",
    "Time",
    "Void",
    "Water",
    "Wind",
    "Wood",
    "World",
    "Wu",
    "Yang",
    "Yin",
    "Yuan",
    "Zhen"
]

# List of Special Physiques attributes
special_physiques_type = ["Physique", "Constitution", "Body", "Bloodline"]


def generate_physique_name():
    return random.choice(special_physiques) + " " + \
           random.choice(special_physiques_essence) + " " + \
           random.choice(special_physiques_type)
