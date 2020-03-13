# Course: CS 30
# Period: 1
# Date created: 20/03/10
# Date last modified: 20/03/12
# Name: Masa Barth
# Description: Properties of the characters, locations and inventory in Dungeon
# Desertion using nested dictionaries.


# Pairs the player's name with a small description of what the player can do by
# using a list in the player's description. The player's name along with their
# description is printed.
player = {'Nicholas': ["use his fists to attack enemies",
          'find items to attack the enemies with']}
for player, info in player.items():
    print(f"The player's name is {player.title()} and he can either:")
    for information in info:
        print(f"- {information}")
print("\n")


# Pairs the ordering of each boss along with the names of each boss by using a
# dictionary. The ordering of each boss and the name of the boss is printed.
bosses = {'First Boss': 'Hera',
          'Second Boss': 'Aphrodite', 'Third Boss': 'Apollo',
          'Fourth Boss': 'Ares', 'Fifth': 'Artemis',
          'Sixth Boss': 'Athena', 'Seventh Boss': 'Demeter',
          'Eighth Boss': 'Dionysus', 'Ninth Boss': 'Hephaestus',
          'Tenth Boss': 'Hermes', 'Eleventh Boss': 'Poseidon',
          'Twelfth Boss': 'Hades', 'Thirteenth Boss': 'Zeus'}
print('The bosses in Dungeon Desertion are:')
for boss, name in bosses.items():
    print(f"\t- {name.title()} is the {boss.title()}.")
print("\n")


# Pairs each item along with their descriptions and how much damage,
# protection, and health they do to the player by using a dictionary in a
# dictionary to describe what each item does in an organized matter. Variables
# are then assigned to the item's information, and finally printed to show
# what each item does.
inventory = {'Sword': {'description': 'slashes at the enemy',
             'damage': '50-100', 'protection': '0', 'health': '0'},
             'Bow': {'description': 'shoots arrows at the enemy',
                     'damage': '50-75', 'protection': '0', 'health': '0'},
             'Axe': {'description': 'slices at the enemy',
                     'damage': '30-60', 'protection': '0', 'health': '0'},
             'Poison potion': {'description': 'poisons the enemy',
                               'damage': '70-80', 'protection': '0',
                               'health': '0'},
             'Invincibility potion': {'description': 'makes you invicible',
                                      'damage': '0',
                                      'protection': '1000 for 3 attacks',
                                      'health': '0'},
             'Strength potion': {'description': 'strengthens your attacks',
                                 'damage': '25% more', 'protection': '0',
                                 'health': '0'},
             'Health potion': {'description': 'heals you up',
                               'damage': '0', 'protection': '0',
                               'health': '50-100'}}

for item, item_info in inventory.items():
    description = item_info['description']
    damage = item_info['damage']
    protection = item_info['protection'].title()
    health = item_info['health']

    print(f"\nThe {item.title()} {description}.")
    print(f"\t- damage : {damage}")
    print(f"\t- protection : {protection}")
    print(f"\t- health : {health}")


# Pairs the location the bosses will appear in along with the names of
# boss. The location and boss is printed to show what each boss' room is
# called.
locations = {'The Curse Room': 'Hera', 'The Revenge Room': 'Aphrodite',
             'The Space Room': 'Apollo', 'The Sky Room': 'Ares',
             'The Moon Room': 'Artemis', 'The Justice Room': 'Athena',
             'The Harvest Room': 'Demeter', 'The Madness Room': 'Dionysus',
             'The Fire Room': 'Hephaestus', 'The Wealth Room': 'Hermes',
             'The Storm Room': 'Poseidon'}
print('\nThe rooms are:')
for room, boss in locations.items():
    print(f"\t- {room.title()} is {boss.title()}'s room.")
