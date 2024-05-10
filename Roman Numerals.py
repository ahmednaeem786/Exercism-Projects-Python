ROMAN_DICT = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX',
              10: 'X', 40: 'XL', 50: 'L', 90: 'XC',
              100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}


def roman(number: int) -> str:
    final = ''
    for value in reversed(ROMAN_DICT):
        while number >= value:
            final += ROMAN_DICT[value]
            number -= value
    return final