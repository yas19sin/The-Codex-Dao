"""
Create 10 random Xianxia Forbidden Areas Names and print one out
"""

import random

# Create a list of first words
first_word = ["Forbidden", "Cursed", "Lost", "Ancient", "Forgotten", "Hidden", "Secret", "Mysterious", "Sacred",
              "Magical"]

# Create a list of second words
second_word = ["Forest", "Mountain", "Valley", "Cave", "Temple", "Lake", "River", "Island", "Ruins", "Tomb"]

# Create a list of third words
third_word = ["of the"]

# Create a list of fourth words
fourth_word = ["Immortal", "Dragon", "Phoenix", "Tiger", "Snake", "Monkey", "Turtle", "Crane", "Toad", "Frog"]

# Create a list of fifth words
fifth_word = ["King", "Queen", "Prince", "Princess", "Emperor", "Empress", "Lord", "Lady", "Master", "Mistress"]


# Create a method to generate a random name
def generate_forbidden_name():
    return random.choice(first_word) + " " + random.choice(second_word) + " " + random.choice(
        third_word) + " " + random.choice(fourth_word) + " " + random.choice(fifth_word)

