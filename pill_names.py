"""
Create a list of 10 random Xianxia/Xuanhuan Cultivation Pill Names, Types and Special Attributes
and combine them and print one out.
"""

import random

# Create a list of cultivation pill special attributes
cultivation_pill_special_attributes = ["Fire", "Water", "Earth", "Wind", "Lightning",
                                       "Thunder", "Metal", "Wood", "Ice", "Light", "Darkness",
                                       "Time", "Space", "Life", "Death", "Destruction", "Creation",
                                       "Healing", "Poison", "Acid", "Void", "Nether", "Chaos", "Order",
                                       "Good", "Evil", "Law", "Chaos", "Lawful", "Chaotic", "Neutral",
                                       "Holy", "Unholy", "Celestial", "Infernal", "Arcane", "Divine",
                                       "Demonic", "Dragon", "Phoenix", "Tiger", "Lion", "Wolf", "Fox",
                                       "Snake", "Serpent"]

# Create a list of cultivation pill types
cultivation_pill_types = ["Spirit", "Essence", "Energy", "Vitality", "Soul",
                          "Spiritual", "Heavenly", "Divine", "Immortal", "Demonic"]

# Create a list of cultivation pill names
cultivation_pill_name = "Pill"


def generate_pill_name():
    return random.choice(cultivation_pill_special_attributes) + " " + \
           random.choice(cultivation_pill_types) + " " + \
           cultivation_pill_name
