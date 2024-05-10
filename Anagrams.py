def find_anagrams(word: str, candidates: list[str]) -> str:
    final_result = []
    for single_candidate in candidates:
        if single_candidate.lower() != word.lower() and converted_word(single_candidate) == converted_word(word):
            final_result.append(single_candidate)
    return final_result


def converted_word(word: str) -> str:
    return sorted(word.lower())