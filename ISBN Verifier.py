import re

def is_valid(isbn: str) -> bool:
    valid_format = re.compile(r"^[0-9]{9}([0-9]|X)$")
    clean_ISBN = isbn.replace('-','')
    if valid_format.match(clean_ISBN):
        return is_check_digit_valid(clean_ISBN) == clean_ISBN[-1]
    return False

def is_check_digit_valid(isbn: str) -> str:
    total = 0
    for index, digit in enumerate(isbn[:-1]): #Starting from reverse String
        total += (index + 1) * int(digit)
    
    check_digit = total % 11
    if total % 11 == 10:
        check_digit = 'X'
        return check_digit
    else:
        check_digit = str(check_digit)
        return check_digit