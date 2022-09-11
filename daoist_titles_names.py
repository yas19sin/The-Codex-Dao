"""
Create 10 random Xianxia Cultivation Daoist Names with Titles and print one out
"""

import random

# Create a list of first names
first_names = ["Qing", "Yun", "Xiao", "Yi", "Yue", "Zi", "Yao", "Ying", "Yi", "Yun"]

# Create a list of last names
last_names = ["Yun", "Yi", "Yue", "Zi", "Yao", "Ying", "Yi", "Yun", "Qing", "Xiao"]

# Create a list of titles
titles = ["Daoist", "Priest", "Disciple", "Sage", "Monk", "Shaman", "Wizard", "Warlock", "Magician"]

# Create a list of suffixes
suffixes = ["of the Heavens", "of the Earth", "of the Mountains", "of the Rivers", "of the Seas", "of the Stars",
            "of the Moon", "of the Sun", "of the Clouds", "of the Wind"]

# Create a list of prefixes
prefixes = ["Great", "Grand", "Elder", "Young", "Little", "Master", "Mistress", "Lord", "Lady", "Prince", "Princess"]

# Create a list of nicknames
nicknames = ["the Great", "the Wise", "the Strong", "the Brave", "the Mighty", "the Powerful", "the Fierce",
             "the Demonic", "the Fearless", "the Invincible", "The Godly", "The Heavenly"]

# Create a list of full names
full_names = []

# Create a list of full names with titles
full_names_with_titles = []

# Create a list of full names with titles and suffixes and prefixes and nicknames
full_names_with_titles_and_suffixes_and_prefixes_and_nicknames = []


# Create method to generate a random name
def generate_random_name():
    # Generate a random first name
    first_name = random.choice(first_names)
    # Generate a random last name
    last_name = random.choice(last_names)
    # Generate a random title
    title = random.choice(titles)
    # Generate a random prefix
    prefix = random.choice(prefixes)
    # Generate a random nickname
    nickname = random.choice(nicknames)
    # Create a full name with title and suffix and prefix and nickname
    full_name_with_title_and_suffix_and_prefix_and_nickname = nickname + " " + prefix + " " + title \
                                                              + " " + first_name + " " + last_name
    # Add the full name with title and suffix to the list of full names with titles and suffixes
    full_names_with_titles_and_suffixes_and_prefixes_and_nicknames.append(
        full_name_with_title_and_suffix_and_prefix_and_nickname)

    return random.choice(full_names_with_titles_and_suffixes_and_prefixes_and_nicknames)
