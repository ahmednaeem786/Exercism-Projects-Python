def rotate(text: str, key: int) -> str:
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    final_result = ''
    for char in text:
        if char.isalpha():
            if char.isupper():
                final_result += alphabets[(alphabets.index(char.lower()) + key) % 26].upper()
            else:
                final_result += alphabets[(alphabets.index(char) + key) % 26]
        else:
            final_result += char
    return final_result