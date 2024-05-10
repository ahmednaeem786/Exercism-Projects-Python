def commands(binary_str: str) -> str:
    actions = ['wink', 'double blink', 'close your eyes', 'jump', ]
    result = []
    for counter, digit in enumerate(binary_str[-1:-5:-1]):
            if digit == '1':
                result.append(actions[counter])
    if binary_str[0] == '1':
        result.reverse()
    return result
    
commands("00010")