VOWELS = ['a', 'e', 'i', 'o', 'u']
VOWEL_SOUNDS = ['xr', 'yt']
CONSONANT_PAIRS = ['ch', 'qu', 'rh', 'th']
CONSONANT_TRIPLE = ['sch', 'squ', 'thr']


def translate(text: str) -> str:
    final_string = []
    suffix = 'ay'
    words = text.split(' ')
    for word in words:
        if word[:3] in CONSONANT_TRIPLE:
            final_string.append(word[3:] + word[:3] + suffix)
        elif word[:2] in CONSONANT_PAIRS:
            final_string.append(word[2:] + word[:2] + suffix)
        elif word[:2] in VOWEL_SOUNDS or word[0] in VOWELS: #Both would make a vowel sounds either ways
            final_string.append(word + suffix)
        else:    
            final_string.append(word[1:] + word[0] + suffix)
    return ' '.join(final_string)