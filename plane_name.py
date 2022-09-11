"""
Create a list of random Xianxia/xuanhuan Cultivation Planes/Dimensions Name and Type and Special Attributes then
 combine them and print one out.
Note: all animals and monsters names are NOT to be used.
"""

import random

Start = "The"

# Uniquer Cultivation Planes/Dimensions Special Attributes
cultivation_planes_special_attributes = ["Infernal", "Freezing", "Frozen", "Burning", "Burned", "Flaming", "Flame",
                                         "Fiery", "Windy", "Ether", "Ethereal", "Oceanic", "Aquatic"]

# Uniquer Cultivation Planes/Dimensions Name
cultivation_planes_name = ["Heavenly", "Demonic", "Divine", "Immortal", "Demon", "Devil", "God", "Godly", "Earthly",
                           "Ghostly", "Spiritual", "Mystical", "Mystic", "Mysterious"]

# Uniquer Cultivation Planes/Dimensions Type
cultivation_planes_type = ["Plane", "Dimension", "Realm", "Domain", "Kingdom", "Land", "Heaven", "Hell", "Abyss",
                           "Void", "Universe"]


def generate_plane_name():
    return Start + " " + random.choice(cultivation_planes_special_attributes) + " " + random.choice(
        cultivation_planes_name) + " " + random.choice(cultivation_planes_type)
