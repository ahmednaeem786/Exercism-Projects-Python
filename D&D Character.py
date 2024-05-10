import random


def modifier(fixed_constitution):
    return (fixed_constitution - 10) // 2

class Character:
    
    def __init__(self):
        self.strength = self.ability
        self.dexterity = self.ability
        self.constitution = self.ability
        self.intelligence = self.ability
        self.wisdom = self.ability
        self.charisma = self.ability
        self.hitpoint = 10 + modifier(self.constitution)
        
    def ability():
        dice_numbers = [random.randint(1,6) for _ in range(4)]
        return sum(dice_numbers) - min(dice_numbers)