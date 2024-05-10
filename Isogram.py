def is_isogram(string):
    cleaned_string = string.replace(' ', '').replace('-', '').lower()
    return len(set(cleaned_string)) == len(cleaned_string)