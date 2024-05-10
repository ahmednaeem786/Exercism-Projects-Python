from random import choices, seed
from string import ascii_uppercase, digits

cache = set()

class Robot:
    def __init__(self):
        self.name = self.new_name()
        cache.add(self.name)
    
    def new_name(self) -> str:
        seed()
        while True:
            name = ''.join(choices(ascii_uppercase, k=2) + choices(digits, k=3))
            if name not in cache:
                break
        return name

    def reset(self):
        cache.remove(self.name)
        self.name = self.new_name()
        cache.add(self.name)