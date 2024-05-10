class Luhn:
    def __init__(self, card_num: int) -> None:
        self.card_num = card_num

    def valid(self) -> bool:
        cleaned = self.card_num.replace(' ','')
        try:
            cleaned = list((map(int, cleaned)))
        except ValueError:
            return False
        length = len(cleaned)
        if length <=1:
            return False
        
        count = 0
        start = length - 2
        for index in range(start, -1, -2):
            if cleaned[index] * 2 > 9:
                count += 1
                cleaned[index] = (cleaned[index] * 2) - 9
            else:
                cleaned[index] *= 2
        return sum(cleaned) % 10 == 0