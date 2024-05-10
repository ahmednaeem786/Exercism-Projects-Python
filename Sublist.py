"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4


def sublist(list_one: list[int], list_two: list[int]) -> int:
    if list_one == list_two:
        return EQUAL
    if sub_superlist(list_one, list_two):
        return SUPERLIST
    if sub_superlist(list_two, list_one):
        return SUBLIST
    return UNEQUAL
    
    
def sub_superlist(list_one: list[int], list_two: list[int]) -> bool: #Check if list_one is super to list_two
    if len(list_one) < len(list_two):
        return False
    
    for index in range(len(list_one) - len(list_two) + 1):
        if list_one[index:index + len(list_two)] == list_two:
            return True

    return False