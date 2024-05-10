from typing import Union


def find(search_list: list[int], value: int) -> Union[ValueError, int]:
    if value not in search_list:
        raise ValueError("value not in array")
        
    lower_bound = 0
    upper_bound = len(search_list) - 1
    while lower_bound <= upper_bound:
        middle_index = (upper_bound+lower_bound) // 2
            
        if search_list[middle_index] == value:
            return middle_index
        elif search_list[middle_index] > value:
            upper_bound = middle_index - 1
        elif search_list[middle_index] < value:
            lower_bound = middle_index + 1
            

print(find([6], 6))
print(find([1, 3, 4, 6, 8, 9, 11], 6))
print(find([1, 3, 4, 6, 8, 9, 11], 1))
print(find([1, 3, 4, 6, 8, 9, 11], 11))
print(find([1, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 634], 144))
print(find([1, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377], 21))
print(find([1, 3, 4, 6, 8, 9, 11], 7))
print(find([1, 3, 4, 6, 8, 9, 11], 0))
print(find([1, 3, 4, 6, 8, 9, 11], 13))
print(find([], 1))
print(find([1, 2], 0))
