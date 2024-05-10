from string import ascii_letters

class PhoneNumber:
    def __init__(self, number: str):
        if any(digit in ascii_letters for digit in number):
            raise ValueError('letters not permitted')
        if any(digit in '@:!' for digit in number):
            raise ValueError('punctuations not permitted')

        only_digits = [char for char in number if char.isdigit()]

        if len(only_digits) < 10:
            raise ValueError('must not be fewer than 10 digits')
        if len(only_digits) > 11:
            raise ValueError('must not be greater than 11 digits')
        if len(only_digits) == 11 and only_digits[0] != '1':
            raise ValueError('11 digits must start with 1')

        if len(only_digits) == 11:
            only_digits = only_digits[1:]

        if only_digits[0] == '0':
            raise ValueError('area code cannot start with zero')
        if only_digits[0] == '1':
            raise ValueError('area code cannot start with one')

        if only_digits[3] == '0':
            raise ValueError('exchange code cannot start with zero')
        if only_digits[3] == '1':
            raise ValueError('exchange code cannot start with one')

        self.number = ''.join(only_digits)
        self.area_code = self.number[:3]

    def pretty(self):
        return f'({self.area_code})-{self.number[3:6]}-{self.number[6:]}'