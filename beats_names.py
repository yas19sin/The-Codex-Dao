"""
Create a list of 10 random Xianxia/Xuanhuan Cultivation Beasts Species and Types and Special Attributes and combine them and print one out.
"""

import random

# Create a list of cultivation beast special attributes
cultivation_beast_special_attributes = ["Deadly", "Spiritual", "Illusive", "Time", "Space", "Destructive", "Creation",
                                        "Chaotic"]

# Create a list of cultivation beast types
cultivation_beast_types = ["Ice", "Fire", "Lightning", "Earth", "Wind", "Water", "Wood", "Metal", "Darkness", "Light"]

# Create a list of cultivation beast species
cultivation_beast_species = ["Dragon", "Phoenix", "Tiger", "Lion", "Wolf", "Horse", "Snake", "Eagle", "Bear", "Fox",
                             "Monkey", "Rabbit", "Deer", "Pig", "Rat", "Ox", "Goat", "Rooster", "Dog", "Boar", "Ape"]


def generate_beast_name():
    return random.choice(cultivation_beast_special_attributes) + " " + \
           random.choice(cultivation_beast_types) + " " + \
           random.choice(cultivation_beast_species)
