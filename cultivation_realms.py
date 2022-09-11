"""
Create a list of 20 random Xuanhuan cultivation realms

"""
import random

realms = ["Foundation Establishment", "Core Formation", "Nascent Soul", "Golden Core",
          "Void Refinement", "Void Fragmentation", "Void Tribulation", "Void Ascension",
          "Void Quasi-Dao", "Void Dao", "Void Monarch", "Void God", "Void Sovereign",
          "Void Lord", "Void Emperor", "Void King", "Void Ancestor", "Void Origin", "Void Heaven", "Void Godking"]


def generate_random_cultivation_realm():
    return random.choice(realms)