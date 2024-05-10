def is_paired(input_string: str) -> bool:
    brackets = {'(': ')',
                '[': ']',
                '{': '}'
                }
    stack = []
    for single_char in input_string:
        if single_char in brackets.keys():
            stack.append(single_char)
        elif single_char in brackets.values(): #Closing Bracket without opening bracket
            if not stack or brackets.get(stack.pop()) != single_char:
                return False
    return not stack #Empty Stack == All Brackets Match