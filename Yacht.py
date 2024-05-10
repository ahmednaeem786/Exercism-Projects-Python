# Score categories.
# Change the values as you see fit.
YACHT = 1
ONES = 2
TWOS = 3
THREES = 4
FOURS = 5
FIVES = 6
SIXES = 7
FULL_HOUSE = 8
FOUR_OF_A_KIND = 9
LITTLE_STRAIGHT = 10
BIG_STRAIGHT = 11
CHOICE = 12


def score(dice: list[int], category: int) -> int:
    set_dice = set(dice)
    counts = {}
    for number in set_dice:
        counts[number] = dice.count(number)
    
    #Category -- Ones
    if category == ONES: return counts.get(1, 0) * 1
    #Category -- Twos
    if category == TWOS: return counts.get(2, 0) * 2
    #Category -- Threes
    if category == THREES: return counts.get(3, 0) * 3
    #Category -- Fours
    if category == FOURS: return counts.get(4, 0) * 4
    #Category -- Fives
    if category == FIVES: return counts.get(5, 0) * 5
    #Category -- Sixes
    if category == SIXES: return counts.get(6, 0) * 6
    #Category -- Full House
    if category == FULL_HOUSE:
        three_counter = 0
        two_counter = 0
        for count in counts.values():
            if count == 3:
                three_counter += 1
            if count == 2:
                two_counter += 1
        if three_counter == 1 and two_counter == 1: return sum(dice)
        return 0
    #Category -- Four of a Kind
    if category == FOUR_OF_A_KIND:
        for key, value in counts.items():
            if value >= 4:
                return key * 4
        return 0
    #Category -- Little Straight
    if category == LITTLE_STRAIGHT:
        return 30 if set_dice.issuperset({1, 2, 3, 4, 5}) else 0
    #Category -- Big Straight
    if category == BIG_STRAIGHT:
        return 30 if set_dice.issuperset({2, 3, 4, 5, 6}) else 0
    #Category -- Choice
    if category == CHOICE: return sum(dice)
    #Category -- Yacht
    if category == YACHT:
        if max(counts.values()) == 5:
            return 50
        return 0