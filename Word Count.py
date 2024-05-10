import re


def count_words(sentence: str) -> dict[str, int]:
    splitted = re.findall(r"[a-z\d]+'?[a-z\d]+|\d+|[a-z]", sentence.lower())
    final = {}
    for word in splitted:
        final[word] = final.get(word, 0) + 1
    return final
    
print(count_words("'First: don't laugh. Then: don't cry. You're getting it.'"))