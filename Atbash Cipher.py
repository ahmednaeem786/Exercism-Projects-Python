import textwrap

plain_latin = 'abcdefghijklmnopqrstuvwxyz1234567890'
cipher_latin = 'zyxwvutsrqponmlkjihgfedcba1234567890'
cipher_dict = dict(zip(plain_latin, cipher_latin))

def encode(text: str, decode: bool = False):
    filtered_text = ''.join(char.lower() for char in text if char.lower() in cipher_dict and char not in ',.')
    processed_text = ''.join(cipher_dict[char] for char in filtered_text)
    if decode:
        return processed_text
    else:
        return ' '.join(textwrap.wrap(processed_text, 5))

def decode(text: str):
    return encode(text, decode=True)
