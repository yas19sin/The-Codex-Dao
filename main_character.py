"""
Create a character class for Xianxia/Xuanhua Cultivation Main Character, which will have his age, cultivation, skills, items, lovers, pets, allies, enemies. Generate a random character and print out its details.
"""

import random


class Character:
    def __init__(self, name, age, cultivation, skills, items, lovers, pets, allies, enemies):
        self.name = name
        self.age = age
        self.cultivation = cultivation
        self.skills = skills
        self.items = items
        self.lovers = lovers
        self.pets = pets
        self.allies = allies
        self.enemies = enemies

    def __str__(self):
        return f"Name: {self.name}\n<br>" \
               f"Age: {self.age}\n<br>" \
               f"Cultivation: {self.cultivation}\n<br>" \
               f"Skills: {self.skills}\n<br><br>" \
               f"Items: {self.items}\n<br><br>" \
               f"Lovers: {self.lovers}\n<br><br>" \
               f"Pets: {self.pets}\n<br><br>" \
               f"Allies: {self.allies}\n<br><br>" \
               f"Enemies: {self.enemies}\n<br><br>"


def generate_character():
    name = random.choice(["Yang Kai", "Wang Li", "Xiao Yan", "Meng Hao", "Zhang Wuji", "Ye Wuchen", "Feng Feiyun"])
    age = random.randint(15, 1000)
    cultivation = random.choice(
        ["Qi Condensation", "Foundation Establishment", "Core Formation", "Nascent Soul", "Divine Soul",
         "Divine Tribulation", "Dao Seeking", "Dao Fusion", "Dao Realm", "Dao Sovereign"])
    skills = random.sample(["Soul Split", "Undying Spirit", "Alchemy Refining", "Poison Refining", "Formation Refining",
                            "Talisman Refining", "Inscription Refining", "Summoning", "Taming", "Sealing"],
                           random.randint(4, 10))
    items = random.sample(
        ["Spirit Stones", "Spirit Herbs", "Spirit Medicines", "Spirit Weapons", "Spirit Armors", "Spirit Tools",
         "Spirit Talismans", "Spirit Formations", "Spirit Inscriptions", "Spirit Beasts"], random.randint(3, 10))
    lovers = random.sample(
        ["Liu Meng'er", "Su Yan", "Xiao Yulan", "Xiao Yumei", "Xiao Yufei", "Xiao Yuchen", "Han Yunxi", "Long Feiye",
         "Gu Beiyue", "Baili Mingxiang"], random.randint(1, 10))
    pets = random.sample(
        ["Little White", "Little Black", "Little Red", "Little Green", "Little Yellow", "Little Purple",
         "Little Orange", "Little Blue", "Little Brown", "Little Pink"], random.randint(1, 5))
    allies = random.sample(
        ["Fu Qingzhu", "Liu Qingge", "Shen Qingqiu", "Zhang Qingyu", "Zhang Qingxue", "Gu Bailu", "Gu Baili",
         "Ouyang Dihua", "Qin Yining", "Qin Yuyang"], random.randint(2, 10))
    enemies = random.sample(
        ["Murong Wanru", "Murong Wanjian", "Wang Zhenyi", "Aunt Ru", "Aunt Ru's Son", "Old Demon", "Old Demon's Son",
         "Jiang Cheng", "Jade Beauty", "Jade Beauty's Son"], random.randint(3, 10))
    return Character(name, age, cultivation, skills, items, lovers, pets, allies, enemies)


def main():
    character = generate_character()
    print(character)


if __name__ == "__main__":
    main()
