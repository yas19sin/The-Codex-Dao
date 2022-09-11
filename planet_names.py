"""
Create 10 random Xianxia Cultivation Genre Planet Names and print one out
"""

import random


def generate_planet_name():
    """
    Generate a random planet name
    """
    # Create a list of adjectives
    adjectives = ["Ancient", "Blessed", "Celestial", "Divine", "Eternal", "Fabled", "Golden", "Holy", "Immortal",
                  "Jade", "Karmic", "Legendary", "Mystic", "Numinous", "Omnipotent", "Pious", "Quintessential",
                  "Radiant", "Sacred", "Timeless", "Ultimate", "Venerable", "Wondrous", "Xian", "Yuan", "Zenith"]

    # Create a list of nouns
    nouns = ["Bastion", "Citadel", "Domain", "Elysium", "Fortress", "Garden", "Haven", "Isle", "Jade",
             "Kingdom", "Land", "Nirvana", "Oasis", "Paradise", "Quarters", "Realm", "Sanctuary", "Temple",
             "Utopia", "Vale", "World", "Xian", "Yuan", "Zenith"]

    # Generate a random name
    return random.choice(adjectives) + " " + random.choice(nouns)


if __name__ == "__main__":
    print(generate_planet_name())
