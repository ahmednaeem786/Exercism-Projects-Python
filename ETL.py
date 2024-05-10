def transform(legacy_data: dict[int, list[str]]) -> dict[str, int]:
    final_dict = {}
    for score, letters in legacy_data.items():
        for single_letter in letters:
            final_dict.setdefault(single_letter.lower(), score)
    return final_dict