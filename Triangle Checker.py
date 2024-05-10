def equilateral(sides: list[int]) ->bool:
    if 0 in sides:
        return False

    if sides[0] == sides[1] == sides[2]:
        return True
    
    return False
def isosceles(sides: list[int]) ->bool:
    if (sides[0] == sides[1] and sides[0] >= sides[2] ) or (sides[1] == sides[2] and sides[2] >= sides[0]) or( sides[0] == sides[2] and sides[0] >= sides[1]):
        return True
    
    if 0 in sides:
        return False
    
    return False
def scalene(sides: list[int]) ->bool:
    if 0 in sides:
        return False

    if (sides[0]==sides[1]) or (sides[0]==sides[2]) or (sides[2]==sides[1]):
        return False

    if (sides[0]+sides[1]+sides[2]-max(sides)) < max(sides):
        return False
    
    return True    