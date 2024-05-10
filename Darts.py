import math
def score(x: int, y: int) -> int:
    distance = math.sqrt(x**2 + y**2)
    
    OUTER = 10 #CAPITAL LETTERS indicate CONSTANTS
    MIDDLE = 5
    INNER = 1
    
    if distance <= INNER:
        return 10
    if INNER <= distance <= MIDDLE:
        return 5
    if MIDDLE <= distance <= OUTER:
        return 1
    return 0