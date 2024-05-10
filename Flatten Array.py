def flatten(iterable: list[int]) -> list[int]:
    flattened_array = []
    
    for element in iterable:
        if type(element) == list:
            flattened_array += flatten(element)
        elif element is not None:
            flattened_array += [element] #.append() cannot be used since it would join the list itself 
            #+= concatenates(joins) both lists
    return flattened_array