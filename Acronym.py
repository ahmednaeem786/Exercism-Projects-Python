import string


def abbreviate(words: str) -> str:
    pattern = str.maketrans('', '', string.punctuation)
    cleaned = (words.replace('-', ' ').translate(pattern)).split()
    return ''.join(word[0].upper() for word in cleaned)