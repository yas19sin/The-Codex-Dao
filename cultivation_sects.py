"""
Create 10 random Xianxia Cultivation Sect names and print one out
"""

import random

# Create a list of 10 random names
names = []
for i in range(10):
    names.append(random.choice(
        ["Cultivation Sect", "Cultivation School", "Cultivation Clan", "Cultivation House", "Cultivation Temple",
         "Cultivation Palace", "Cultivation Tower", "Cultivation Cave", "Cultivation Valley", "Cultivation Mountain"])
                 + " of " +
                 random.choice(["the " +
                                random.choice(
                                    ["Heavenly", "Divine", "Mystical", "Sacred", "Holy", "Immortal", "Celestial",
                                     "Ethereal", "Spiritual", "Arcane", "Mystic", "Mysterious", "Magical", "Enchanted",
                                     "Fantastic", "Fantastical", "Mythical", "Legendary", "Fabled", "Fairy",
                                     "Fairytale", "Jade"]) +
                                " " +
                                random.choice(
                                    ["Dragon", "Phoenix", "Tiger", "Lion", "Wolf", "Fox", "Horse", "Deer", "Rabbit",
                                     "Monkey", "Snake", "Turtle", "Fish", "Bird", "Eagle", "Falcon", "Hawk", "Owl",
                                     "Crow", "Raven", "Swan", "Crane", "Stork", "Duck", "Goose", "Sparrow", "Pigeon",
                                     "Dove", "Parrot", "Peacock", "Penguin", "Seal", "Whale", "Dolphin", "Shark",
                                     "Tuna",
                                     "Sword", "Blade", "Knife", "Dagger", "Spear", "Lance", "Halberd", "Axe", "Hammer",
                                     "Mace", "Flail", "Scythe", "Whip", "Bow", "Arrow", "Crossbow", "Shield", "Helmet",
                                     "Armor", "Cloak", "Robe", "Staff", "Wand", "Scepter", "Crown", "Throne",
                                     "Sword"])]))


def generate_sect_name():
    return random.choice(names)
