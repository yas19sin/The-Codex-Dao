"""
Create a list of 10 random Xianxia/Xuanhuan Cultivation Spirit Herbs Names, Types and Special Attributes
and combine them and print one out.
Note: all animals and monsters names are NOT to be used.
"""

import random

# Create a list of  spirit herbs types
spirit_herbs_types = ["Spirit", "Essence", "Energy", "Vitality", "Soul",
                      "Spiritual", "Heavenly", "Divine", "Immortal", "Demonic"]

# Create a list of spirit herbs special attributes
spirit_herbs_special_attributes = ["Fire", "Water", "Earth", "Wind", "Lightning",
                                   "Thunder", "Ice", "Snow", "Metal", "Wood"]

# Create a list of spirit herbs names
spirit_herbs_names = ["Herb", "Plant", "Flower", "Grass", "Fruit", "Root", "Seed", "Leaf", "Bud", "Stem"]

# Create a list of spirit herbs
spirit_herbs = []

# Create a list of 10 random spirit herbs
for i in range(10):
    spirit_herbs.append(random.choice(spirit_herbs_types) + " " +
                        random.choice(spirit_herbs_special_attributes) + " " +
                        random.choice(spirit_herbs_names))


def generate_herb_name():
    return random.choice(spirit_herbs)
