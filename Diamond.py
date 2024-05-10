def rows(letter: str) -> list[str]:
    letters = []
    for alpha in range(ord('A'), ord(letter) + 1):
        letters.append(chr(alpha))
    alphabet = letters[:-1] + letters[::-1]
    diamond_line = letters[::-1] + letters[1:]
    return [''.join(x if x == y else ' ' for y in diamond_line) for x in alphabet]