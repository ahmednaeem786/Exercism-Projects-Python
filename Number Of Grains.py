from typing import Union


def square(number: int) -> Union[ValueError, int]:
    if not 0 < number < 65:
        raise ValueError("square must be between 1 and 64")
    return 2 ** (number - 1)


def total() -> int:
    return (2**64) - 1