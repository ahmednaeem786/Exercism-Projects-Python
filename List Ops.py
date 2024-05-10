from typing import Callable


def append(list1: list, list2: list) -> list:
    return list1 + list2


def concat(lists: list) -> list:
    return [element for single_element in lists for element in single_element]


def filter(function: Callable[[int], bool], list: list[int]) -> list[int]:
    return [element for element in list if function(element)]


def length(list: list[int]) -> int:
    return sum(1 for _ in list)


def map(function: Callable[[int], int], list: list[int]) -> list[int]:
    return [function(element) for element in list]


def foldl(function: Callable[[int], int], list: list[int], initial: int) -> int:
    for element in list:
        initial = function(initial, element)
    return initial


def foldr(function: Callable[[int], int], list: list[int], initial: int) -> int:
    for element in reversed(list):
        initial = function(initial, element)
    return initial


def reverse(list: list[int]) -> list[int]:
    return list[::-1]