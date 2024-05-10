from itertools import groupby


def decode(string: str) -> str:
    count = ''
    final = ''
    for key, group in groupby(string):
        if key.isnumeric(): #Multiple Occurences of Alphabet
            count += str(key)
        elif not count: #Case: Single Alphabet
            final += str(key)
        else:
            final += int(count) * key
            count = ''
    return final


def encode(string: str) -> str:
    final = ''
    count = 0
    for key, group in groupby(string):
        count = sum(1 for _ in group)
        if count > 1:
            final += str(count) + key
        else:
            final += key
    return final