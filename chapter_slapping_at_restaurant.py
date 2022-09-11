"""
Create a random Xianxia/Xuanhuan Cultivation story of the Main Character Visiting a Restaurant with a twist and
 print it out
"""

import random

# Create a list of the main character's names
main_character_names = ["Xiao Long", "Xiao Mei", "Xiao Fang", "Xiao Wei",
                        "Xiao Li", "Xiao Yu", "Xiao Xiao", "Xiao Xiao", "Xiao Xiao", "Xiao Xiao"]

# Create a list of the restaurant's names
restaurant_names = ["The Golden Dragon", "The Silver Dragon", "The Jade Dragon",
                    "The Iron Dragon", "The Copper Dragon", "The Bronze Dragon",
                    "The Golden Phoenix", "The Silver Phoenix", "The Jade Phoenix",
                    "The Iron Phoenix", "The Copper Phoenix", "The Bronze Phoenix"]

# Create a list of the restaurant's food
restaurant_food = ["Noodles", "Rice", "Dumplings", "Soup", "Bread", "Pork",
                   "Chicken", "Beef", "Fish", "Vegetables", "Fruit", "Soup",
                   "Bread", "Pork", "Chicken", "Beef", "Fish", "Vegetables", "Fruit"]

# Create a list of the restaurant's drinks
restaurant_drinks = ["Water", "Tea", "Juice", "Soda", "Beer", "Wine", "Sake",
                     "Whiskey", "Vodka", "Rum", "Tequila", "Gin", "Brandy",
                     "Cider", "Coffee", "Milk", "Hot Chocolate", "Lemonade", "Smoothie"]

# Create a list of the restaurant's desserts
restaurant_desserts = ["Ice Cream", "Cake", "Pie", "Cookies", "Candy", "Chocolate",
                       "Fruit", "Custard", "Pudding", "Cheesecake", "Tiramisu",
                       "Mousse", "Gelato", "Macaroons", "Crepes", "Donuts",
                       "Brownies", "Cupcakes", "Pancakes"]

# Create a list of the restaurant's prices
restaurant_prices = ["$1", "$2", "$3", "$4", "$5", "$6", "$7", "$8", "$9",
                     "$10", "$11", "$12", "$13", "$14", "$15", "$16", "$17",
                     "$18", "$19", "$20"]

# Create a list of the restaurant's waiters
restaurant_waiters = ["Xiao Long", "Xiao Mei", "Xiao Fang", "Xiao Wei", "Xiao Li",
                      "Xiao Yu", "Xiao Xiao", "Xiao Xiao", "Xiao Xiao", "Xiao Xiao"]

# Create a list of the restaurant's waitresses
restaurant_waitresses = ["Xiao Long", "Xiao Mei", "Xiao Fang", "Xiao Wei", "Xiao Li",
                         "Xiao Yu", "Xiao Xiao", "Xiao Xiao", "Xiao Xiao", "Xiao Xiao"]

# Create a list of the restaurant's chefs
restaurant_chefs = ["Xiao Long", "Xiao Mei", "Xiao Fang", "Xiao Wei", "Xiao Li",
                    "Xiao Yu", "Xiao Xiao", "Xiao Xiao", "Xiao Xiao", "Xiao Xiao"]

# Create a list of the restaurant's cooks
restaurant_cooks = ["Xiao Long", "Xiao Mei", "Xiao Fang", "Xiao Wei", "Xiao Li",
                    "Xiao Yu", "Xiao Xiao", "Xiao Xiao", "Xiao Xiao", "Xiao Xiao"]

# Create a list of the restaurant's owners
restaurant_owners = ["Xiao Long", "Xiao Mei", "Xiao Fang", "Xiao Wei", "Xiao Li",
                     "Xiao Yu", "Xiao Xiao", "Xiao Xiao", "Xiao Xiao", "Xiao Xiao"]

# Create a list of the restaurant's managers
restaurant_managers = ["Xiao Long", "Xiao Mei", "Xiao Fang", "Xiao Wei", "Xiao Li",
                       "Xiao Yu", "Xiao Xiao", "Xiao Xiao", "Xiao Xiao", "Xiao Xiao"]

# Create a list of the restaurant's customers
restaurant_customers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11",
                        "12", "13", "14", "15", "16", "17", "18", "19", "20"]

# Create a list of the restaurant's wait times
restaurant_wait_times = ["5 minutes", "10 minutes", "15 minutes", "20 minutes",
                         "25 minutes", "30 minutes", "35 minutes", "40 minutes",
                         "45 minutes", "50 minutes", "55 minutes", "60 minutes",
                         "65 minutes", "70 minutes", "75 minutes", "80 minutes",
                         "85 minutes", "90 minutes", "95 minutes", "100 minutes"]

# Create a list of the restaurant's seating times
restaurant_seating_times = ["5 minutes", "10 minutes", "15 minutes", "20 minutes",
                            "25 minutes", "30 minutes", "35 minutes", "40 minutes",
                            "45 minutes", "50 minutes", "55 minutes", "60 minutes",
                            "65 minutes", "70 minutes", "75 minutes", "80 minutes",
                            "85 minutes", "90 minutes", "95 minutes", "100 minutes"]

# Create a list of the restaurant's eating times
restaurant_eating_times = ["5 minutes", "10 minutes", "15 minutes", "20 minutes",
                           "25 minutes", "30 minutes", "35 minutes", "40 minutes",
                           "45 minutes", "50 minutes", "55 minutes", "60 minutes",
                           "65 minutes", "70 minutes", "75 minutes", "80 minutes",
                           "85 minutes", "90 minutes", "95 minutes", "100 minutes"]

# Create a list of the restaurant's leaving times
restaurant_leaving_times = ["5 minutes", "10 minutes", "15 minutes", "20 minutes",
                            "25 minutes", "30 minutes", "35 minutes", "40 minutes",
                            "45 minutes", "50 minutes", "55 minutes", "60 minutes",
                            "65 minutes", "70 minutes", "75 minutes", "80 minutes",
                            "85 minutes", "90 minutes", "95 minutes", "100 minutes"]

# Create a list of the restaurant's closing times
restaurant_closing_times = ["7 PM", "8 PM", "9 PM", "10 PM", "11 PM", "12 AM", "1 AM",
                            "2 AM", "3 AM", "4 AM", "5 AM", "6 AM", "7 AM", "8 AM",
                            "9 AM", "10 AM", "11 AM", "12 PM", "1 PM", "2 PM"]

# Create a list of the restaurant's opening times
restaurant_opening_times = ["7 AM", "8 AM", "9 AM", "10 AM", "11 AM", "12 PM", "1 PM",
                            "2 PM", "3 PM", "4 PM", "5 PM", "6 PM", "7 PM", "8 PM",
                            "9 PM", "10 PM", "11 PM", "12 AM", "1 AM", "2 AM"]
# Create a list of the restaurant's opening events
restaurant_opening_events = ["A Birthday", "A Wedding", "A Funeral", "A Party",
                             "A Celebration", "A Festival", "A Concert", "A Play",
                             "A Show", "A Performance", "A Game", "A Match", "A Race",
                             "A Competition", "A Tournament", "A Contest", "A Battle", "A Fight", "A Duel"]

# Create a list of the restaurant's closing reasons
restaurant_closing_reasons = ["A Fire", "A Flood", "A Tornado", "A Hurricane",
                              "A Blizzard", "A War", "A Fight", "A Duel", "A Murder",
                              "A Robbery", "A Bankruptcy", "A Lawsuit", "A Protest",
                              "A Demonstration", "A Riot", "A Strike", "A Lockout",
                              "A Pandemic", "A Plague", "A Disease"]

main_character_name = random.sample(main_character_names, 1)
manager_character_name = random.sample(restaurant_managers, 1)
while main_character_name == manager_character_name:
    manager_character_name = random.sample(restaurant_managers, 1)
price = random.sample(restaurant_prices, 2)

# Create a list of scenarios that the restaurant with random formatting
restaurant_scenarios = ["{} entered the {} restaurant, he looked around and saw {} customers, he waited {} to be "
                        "seated, but {} event was happening, so he asked for the manager to be called who\'s name was "
                        "{}, the manager and {} argued so they decided to settle it on {} event, {} won and {} lost, "
                        "{} was happy and {} was sad, {} asked for a compensation of {} and {} agreed, finally he "
                        "asked for {} to eat with a {} for dessert, the bill was {} he payed it and left, on the way "
                        "home he murmured \"That was a good little face slapping session for today\" and continued to "
                        "his humble abode to cultivate."
                            .format(main_character_name[0], random.choice(restaurant_names),
                                    random.choice(restaurant_customers), random.choice(restaurant_wait_times),
                                    random.choice(restaurant_opening_events), manager_character_name[0],
                                    main_character_name[0], random.choice(restaurant_opening_events),
                                    main_character_name[0], manager_character_name[0],
                                    main_character_name[0], manager_character_name[0],
                                    main_character_name[0], price[1],
                                    manager_character_name[0], random.choice(restaurant_food),
                                    random.choice(restaurant_desserts), price[0])]


def generate_restaurant_chapter():
    return random.choice(restaurant_scenarios)

