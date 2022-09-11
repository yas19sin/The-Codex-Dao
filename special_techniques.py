"""
Create a list of 10 random Xianxia/Xuanhuan Cultivation Special Technique Name,
and its Special Attributes and combine them and print one out.
"""

import random

# Create a list of cultivation special technique attributes
cultivator_special_technique_attributes = ["Fire", "Water", "Earth", "Wind", "Lightning", "Ice", "Space", "Time",
                                           "Destruction", "Deadly", "Light", "Darkness", "Heaven", "Hell"]

# Create a list of cultivation special technique name
cultivator_special_technique_name = ["Sword of the Seven Stars", "Dragon Slaying Saber", "Nine Heavens Thunder Sword",
                                     "Ascending Dragon Sword", "Heavenly Dragon Sword", "Flaming Dragon Sword",
                                     "Five Elements Sword", "Earth Shifting Steps", "Space Sealing Palm",
                                     "Void Burning Palm", "Raging Demonic Eyes", "Heavenly Demon Eyes",
                                     "Demonic Dragon Eyes", "Karmic Fire Eyes", "Karmic Lineage Eyes",
                                     "Space Freezing Finger", "Shattering Space Finger"]


def generate_special_technique():
    return random.choice(cultivator_special_technique_attributes) + " " + \
           random.choice(cultivator_special_technique_name)
