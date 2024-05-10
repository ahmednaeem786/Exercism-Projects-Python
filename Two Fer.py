"""
The function generates a phrase for sharing something
In case, no name is provided, it uses a common noun; 'you'
name param: str
return param: str
"""
def two_fer(name: str = 'you') -> str:
    return f'One for {name}, one for me.'