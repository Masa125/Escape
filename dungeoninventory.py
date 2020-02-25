# Course: CS 30
# Period: 1
# Date created: 20/02/14
# Date last modified: 19/02/24
# Name: Masa Barth
# Description: Inventory of Dungeon Desertion using list commands.


# The sword, and bow are originally assigned to the variable called weapons.
# The element called Axe is then appended to weapons at the end of the list.
# The list of weapons is printed to show that the axe was added.
# The list is presented in alphabetical order, but doesn't affect the original
# list. The weapons are printed out in a sentence.
weapons = ['Sword', 'Bow']
(weapons.append('Axe'))
print(weapons)
print(sorted(weapons))
print(f"The weapons in Dungeon Desertion are the {weapons[0].lower()}, \
{weapons[1].lower()}, and {weapons[2].lower()}.")


# The poison potion, invincibility potion, strength potion, and invisibility
# potion are originally assigned to the variable called potions. The
# potion is removed from 'potions'. The list of potions are printed to show
# that the invisibility potion is removed. The health potion is inserted into
# the first position of the list. The list of potions are printed to show
# that the health potion was inserted into the first position.The order of the
# new list is reversed. The list of potions are printed to show that the order
# of the new list is reversed. The potions are printed out in a sentence.
potions = ['Poison potion', 'Invincibility potion', 'Strength potion',
           'Invisibility potion']
potions.remove('Invisibility potion')
print(potions)
potions.insert(0, 'Health potion')
print(potions)
potions.reverse()
print(potions)
print(f"The potions in Dungeon Desertion are the {potions[0].lower()}, \
{potions[1].lower()}, {potions[2].lower()}, and {potions[3].lower()}.")


# Zeus, Hera, Aphrodite, Apollo, Ares, Artemis, Athena, Demeter, Dionysus,
# Hephaestus, Hermes, Poseidon, and Hades are originally assigned to the
# variable called bosses. Hades is removed from the list of bosses. The list
# of bosses is printed to show that Hades was removed. Zeus is removed from
# the list, but is still accessible.The list of bosses is printed to show that
# Zeus was removed from the list. The list is sorted in alphabetical order.
# The list of bosses is printed to show that the list is in alphabetical order.
# The length of the list of bosses is printed. The bosses are printed out in a
# sentence.
bosses = ['Zeus', 'Hera', 'Aphrodite', 'Apollo', 'Ares', 'Artemis', 'Athena',
          'Demeter', 'Dionysus', 'Hephaestus', 'Hermes', 'Poseidon', 'Hades']
del bosses[-1]
print(bosses)
popped_boss = bosses.pop(0)
print(bosses)
bosses.sort()
print(bosses)
print(len(bosses))
print(f"The bosses in Dungeon Desertion are {bosses[0].title()}, \
{bosses[1].title()}, {bosses[2].title()}, {bosses[3].title()}, \
{bosses[4].title()}, {bosses[5].title()}, {bosses[6].title()}, \
{bosses[7].title()}, {bosses[8].title()}, {bosses[9].title()}, and \
{bosses[10].title()}.")
