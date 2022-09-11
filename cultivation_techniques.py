"""
Create one random Xianxia/Xuanhuan Cultivation Techniques for each alphabet from A to Z and print one out
"""

import random


# Cultivation Technique Class
class CultivationTechnique:
    def __init__(self, name, types, description, rank, power, speed, defense, health, mana, spirit, luck, requirements):
        self.name = name
        self.type = types
        self.description = description
        self.rank = rank
        self.power = power
        self.speed = speed
        self.defense = defense
        self.health = health
        self.mana = mana
        self.spirit = spirit
        self.luck = luck
        self.requirements = requirements

    def __str__(self):
        return "Name: " + self.name \
               + "\nType: " + self.type \
               + "\nDescription: " + self.description \
               + "\nRank: " + self.rank \
               + "\nPower: " + self.power \
               + "\nSpeed: " + self.speed \
               + "\nDefense: " + self.defense \
               + "\nHealth: " + self.health \
               + "\nMana: " + self.mana \
               + "\nSpirit: " + self.spirit \
               + "\nLuck: " + self.luck \
               + "\nRequirements: " + self.requirements


# Cultivation Technique Types
cultivation_technique_types = ["Xianxia", "Xuanhuan"]

# Cultivation Technique Ranks
cultivation_technique_ranks = ["Heaven", "Earth", "Mystic", "Divine", "Immortal", "Saint", "Demon", "Dragon", "God"]

# Cultivation Technique Requirements
cultivation_technique_requirements = [
    "None", "Bloodline", "Cultivation", "Cultivation and Bloodline",
    "Cultivation and Bloodline and Item",
    "Cultivation and Bloodline and Item and Secret Technique"]

# Cultivation Technique Names
cultivation_technique_names = [
    "Azure Dragon", "Black Tortoise", "Vermilion Bird", "White Tiger", "Qinglong", "Zhuque",
    "Xuanwu", "Baihu", "Jade Emperor", "Yellow Emperor", "Fuxi", "Nuwa", "Pangu", "Shennong",
    "Yandi", "Huangdi", "Laozi", "Yin and Yang", "Five Elements", "Eight Trigrams",
    "Nine Palaces", "Ten Heavenly Stems", "Twelve Earthly Branches", "Four Symbols",
    "Seven Stars", "Twenty-Eight Constellations", "Sixty-Four Hexagrams",
    "One Hundred and Eight Stars", "Five Phases", "Six Directions", "Seven Emotions",
    "Eight Winds", "Nine Heavens", "Ten Hells", "Twelve Zodiacs", "Twenty-Four Solar Terms",
    "Thirty-Six Stratagems", "Sixty-Four Arts", "One Hundred and Eight Skills",
    "Five Elements", "Six Paths", "Seven Wonders", "Eight Extremities", "Nine Mountains",
    "Ten Lands", "Twelve Palaces", "Twenty-Four Bridges", "Thirty-Six Caves",
    "Sixty-Four Hexagrams"]

# Cultivation Technique Descriptions
cultivation_technique_descriptions = [
    "A cultivation technique that allows the user to control the Azure Dragon.",
    "A cultivation technique that allows the user to control the Black Tortoise.",
    "A cultivation technique that allows the user to control the Vermilion Bird.",
    "A cultivation technique that allows the user to control the White Tiger.",
    "A cultivation technique that allows the user to control the Qinglong.",
    "A cultivation technique that allows the user to control the Zhuque.",
    "A cultivation technique that allows the user to control the Xuanwu.",
    "A cultivation technique that allows the user to control the Baihu.",
    "A cultivation technique that allows the user to control the Jade Emperor.",
    "A cultivation technique that allows the user to control the Yellow Emperor.",
    "A cultivation technique that allows the user to control the Fuxi.",
    "A cultivation technique that allows the user to control the Nuwa.",
    "A cultivation technique that allows the user to control the Pangu.",
    "A cultivation technique that allows the user to control the Shennong.",
    "A cultivation technique that allows the user to control the Yandi.",
    "A cultivation technique that allows the user to control the Huangdi.",
    "A cultivation technique that allows the user to control the Laozi.",
    "A cultivation technique that allows the user to control the Yin and Yang.",
    "A cultivation technique that allows the user to control the Five Elements.",
    "A cultivation technique that allows the user to control the Eight Trigrams.",
    "A cultivation technique that allows the user to control the Nine Palaces.",
    "A cultivation technique that allows the user to control the Ten Heavenly Stems.",
    "A cultivation technique that allows the user to control the Twelve Earthly Branches.",
    "A cultivation technique that allows the user to control the Four Symbols.",
    "A cultivation technique that allows the user to control the Seven Stars.",
    "A cultivation technique that allows the user to control the Twenty-Eight Constellations.",
    "A cultivation technique that allows the user to control the Sixty-Four Hexagrams.",
    "A cultivation technique that allows the user to control the One Hundred and Eight Stars.",
    "A cultivation technique that allows the user to control the Five Phases.",
    "A cultivation technique that allows the user to control the Six Directions.",
    "A cultivation technique that allows the user to control the Seven Emotions.",
    "A cultivation technique that allows the user to control the Eight Winds.",
    "A cultivation technique that allows the user to control the Nine Heavens.",
    "A cultivation technique that allows the user to control the Ten Hells.",
    "A cultivation technique that allows the user to control the Twelve Zodiacs.",
    "A cultivation technique that allows the user to control the Twenty-Four Solar Terms.",
    "A cultivation technique that allows the user to control the Thirty-Six Stratagems.",
    "A cultivation technique that allows the user to control the Sixty-Four Arts.",
    "A cultivation technique that allows the user to control the One Hundred and Eight Skills.",
    "A cultivation technique that allows the user to control the Five Elements.",
    "A cultivation technique that allows the user to control the Six Paths.",
    "A cultivation technique that allows the user to control the Seven Wonders.",
    "A cultivation technique that allows the user to control the Eight Extremities.",
    "A cultivation technique that allows the user to control the Nine Mountains.",
    "A cultivation technique that allows the user to control the Ten Lands.",
    "A cultivation technique that allows the user to control the Twelve Palaces.",
    "A cultivation technique that allows the user to control the Twenty-Four Bridges.",
    "A cultivation technique that allows the user to control the Thirty-Six Caves.",
    "A cultivation technique that allows the user to control the Sixty-Four Hexagrams."]

# Cultivation Technique Powers
cultivation_technique_powers = ["10", "20", "30", "40", "50", "60", "70", "80", "90", "100", "110", "120", "130", "140",
                                "150", "160", "170", "180", "190", "200", "210", "220", "230", "240", "250", "260",
                                "270", "280", "290", "300", "310", "320", "330", "340", "350", "360", "370", "380",
                                "390", "400", "410", "420", "430", "440", "450", "460", "470", "480", "490", "500",
                                "510", "520", "530", "540", "550", "560", "570", "580", "590", "600", "610", "620",
                                "630", "640", "650", "660", "670", "680", "690", "700", "710", "720", "730", "740",
                                "750", "760", "770", "780", "790", "800", "810", "820", "830", "840", "850", "860",
                                "870", "880", "890", "900", "910", "920", "930", "940", "950", "960", "970", "980",
                                "990", "1000"]

# Cultivation Technique Speeds
cultivation_technique_speeds = ["10", "20", "30", "40", "50", "60", "70", "80", "90", "100", "110", "120", "130", "140",
                                "150", "160", "170", "180", "190", "200", "210", "220", "230", "240", "250", "260",
                                "270", "280", "290", "300", "310", "320", "330", "340", "350", "360", "370", "380",
                                "390", "400", "410", "420", "430", "440", "450", "460", "470", "480", "490", "500",
                                "510", "520", "530", "540", "550", "560", "570", "580", "590", "600", "610", "620",
                                "630", "640", "650", "660", "670", "680", "690", "700", "710", "720", "730", "740",
                                "750", "760", "770", "780", "790", "800", "810", "820", "830", "840", "850", "860",
                                "870", "880", "890", "900", "910", "920", "930", "940", "950", "960", "970", "980",
                                "990", "1000"]

# Cultivation Technique Defenses
cultivation_technique_defenses = ["10", "20", "30", "40", "50", "60", "70", "80", "90", "100", "110", "120", "130",
                                  "140", "150", "160", "170", "180", "190", "200", "210", "220", "230", "240", "250",
                                  "260", "270", "280", "290", "300", "310", "320", "330", "340", "350", "360", "370",
                                  "380", "390", "400", "410", "420", "430", "440", "450", "460", "470", "480", "490",
                                  "500", "510", "520", "530", "540", "550", "560", "570", "580", "590", "600", "610",
                                  "620", "630", "640", "650", "660", "670", "680", "690", "700", "710", "720", "730",
                                  "740", "750", "760", "770", "780", "790", "800", "810", "820", "830", "840", "850",
                                  "860", "870", "880", "890", "900", "910", "920", "930", "940", "950", "960", "970",
                                  "980", "990", "1000"]

# Cultivation Technique Healths
cultivation_technique_healths = ["10", "20", "30", "40", "50", "60", "70", "80", "90", "100", "110", "120", "130",
                                 "140", "150", "160", "170", "180", "190", "200", "210", "220", "230", "240", "250",
                                 "260", "270", "280", "290", "300", "310", "320", "330", "340", "350", "360", "370",
                                 "380", "390", "400", "410", "420", "430", "440", "450", "460", "470", "480", "490",
                                 "500", "510", "520", "530", "540", "550", "560", "570", "580", "590", "600", "610",
                                 "620", "630", "640", "650", "660", "670", "680", "690", "700", "710", "720", "730",
                                 "740", "750", "760", "770", "780", "790", "800", "810", "820", "830", "840", "850",
                                 "860", "870", "880", "890", "900", "910", "920", "930", "940", "950", "960", "970",
                                 "980", "990", "1000"]

# Cultivation Technique Manas
cultivation_technique_manas = ["10", "20", "30", "40", "50", "60", "70", "80", "90", "100", "110", "120", "130", "140",
                               "150", "160", "170", "180", "190", "200", "210", "220", "230", "240", "250", "260",
                               "270", "280", "290", "300", "310", "320", "330", "340", "350", "360", "370", "380",
                               "390", "400", "410", "420", "430", "440", "450", "460", "470", "480", "490", "500",
                               "510", "520", "530", "540", "550", "560", "570", "580", "590", "600", "610", "620",
                               "630", "640", "650", "660", "670", "680", "690", "700", "710", "720", "730", "740",
                               "750", "760", "770", "780", "790", "800", "810", "820", "830", "840", "850", "860",
                               "870", "880", "890", "900", "910", "920", "930", "940", "950", "960", "970", "980",
                               "990", "1000"]

# Cultivation Technique Spirits
cultivation_technique_spirits = ["Spirit", "Soul", "Heart", "Mind", "Will", "Consciousness", "Intent", "Aura",
                                 "Essence", "Energy", "Qi", "Ki", "Chi"]

# Cultivation Technique Lucks
cultivation_technique_lucks = ["Normal", "Good", "Great", "Excellent", "Perfect", "Godly"]

# Cultivation Technique List
cultivation_technique_list = []

# Create Cultivation Techniques
for i in range(26):
    cultivation_technique_list.append(CultivationTechnique(cultivation_technique_names[i] + '<br>',
                                                           random.choice(cultivation_technique_types) + '<br>',
                                                           cultivation_technique_descriptions[i] + '<br>',
                                                           random.choice(cultivation_technique_ranks) + '<br>',
                                                           random.choice(cultivation_technique_powers) + '<br>',
                                                           random.choice(cultivation_technique_speeds) + '<br>',
                                                           random.choice(cultivation_technique_defenses) + '<br>',
                                                           random.choice(cultivation_technique_healths) + '<br>',
                                                           random.choice(cultivation_technique_manas) + '<br>',
                                                           random.choice(cultivation_technique_spirits) + '<br>',
                                                           random.choice(cultivation_technique_lucks) + '<br>',
                                                           random.choice(cultivation_technique_requirements) + '<br>'))


def generate_cultivation_technique():
    return random.choice(cultivation_technique_list)
