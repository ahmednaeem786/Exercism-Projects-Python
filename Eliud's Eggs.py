def egg_count(display_value: int) -> int:
    binary = []
    while display_value > 0:
        remainder = display_value % 2
        display_value //= 2
        binary.append(remainder)
    return binary.count(1)

def egg_coun2(display_value):
    spot = 0;
    while display_value:
        spot += display_value & 1
        display_value >>= 1
    return spot
