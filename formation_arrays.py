"""
Create a list of Xianxia/Xuanhuan Cultivation Formation Arrays Names and print one out
"""

import random

# Formation Arrays ranks
formation_arrays_ranks = ["Lower", "Middle", "Higher", "Top"]

# Formation Arrays types
formation_arrays_types = ["Heavenly", "Earthly", "Mysterious", "Divine", "Lost", "Secret", "Forbidden", "Immortal",
                          "Demonic"]

# Formation Arrays names
formation_arrays_names = ["Five Elements Array", "Nine Palaces Array", "Eight Trigrams Array", "Eight Gates Array",
                          "Eight Diagrams Array", "Four Holy Beasts Array", "Four Symbols Array",
                          "Four Divinities Array", "Four Gods Array", "Four Heavenly Kings Array",
                          "Four Guardians Array", "Four Emperors Array", "Four Seasons Array", "Four Directions Array",
                          "Four Seasons Array", "Four Virtues Array", "Big Dipper Array", "Seven Stars Array",
                          "Seven Sages Array", "Seven Emotions Array", "Seven Sins Array", "Seven Wonders Array",
                          "Qi Gathering Array", "Qi Condensing Array", "Qi Refining Array", "Qi Transforming Array",
                          "Qi Tempering Array", "Illusion Array", "Concealment Array", "Stealth Array",
                          "Disguise Array", "Void-Breaking Array", "Teleportation Array", "Space-Shifting Array",
                          "Space-Folding Array", "Space-Tearing Array", "Mountain-Shaking Array",
                          "Earth-Crushing Array", "Heaven-Shaking Array", "Sky-Splitting Array"]


def generate_random_formation_array():
    """
    Generate a random formation array name
    """
    return random.choice(formation_arrays_ranks) + "-Rank " + random.choice(
        formation_arrays_types) + " " + random.choice(formation_arrays_names)


def main():
    """
    Test function
    """
    print(random_formation_array())


if __name__ == "__main__":
    main()
