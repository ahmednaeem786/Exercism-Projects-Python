# Score categories.
# Change the values as you see fit.
from typing import Callable


ONES = lambda x: x.count(1) * 1
TWOS = lambda x: x.count(2) * 2
THREES = lambda x: x.count(3) * 3
FOURS = lambda x: x.count(4) * 4
FIVES = lambda x: x.count(5) * 5
SIXES = lambda x: x.count(6) * 6
YACHT = lambda x: 50 if len(set(x)) == 1 else 0
FULL_HOUSE = lambda x: sum(x) if set(x.count(y) for y in x).issuperset({2, 3}) else 0
FOUR_OF_A_KIND = lambda x: next((y * 4 for y in x if x.count(y) >= 4), 0)
LITTLE_STRAIGHT = lambda x: 30 if set(x).issuperset({1, 2, 3, 4, 5}) else 0
BIG_STRAIGHT = lambda x: 30 if set(x).issuperset({2, 3, 4, 5, 6}) else 0
CHOICE = lambda x: sum(x)


def score(dice: list[int], category: Callable[[list[int]], int]) -> int:
    return category(dice)