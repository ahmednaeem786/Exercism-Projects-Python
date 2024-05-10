#Armstrong number is a number that is equal to the sum of its own digits each raised to the power of the number of digits.


def is_armstrong_number(number: int) -> bool:
    total = 0
    for index in str(number):
        total += int(index) ** len(str(number))
    return total == number