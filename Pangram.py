def is_pangram(sentence: str) -> bool:
    duplicates_removed = set(sentence.lower())
    total_ascii_value = 0

    if sentence == "":
        return False
    
    total_ascii_value = sum(ord(char) for char in duplicates_removed if char.isalpha())
    
    return total_ascii_value == 2847 #2847 is the sum of ASCII values from alphabets a-z
