def sum_of_multiples(limit: int, multiples: list[int]) -> int:
    final = set()
    for number in multiples:
        if number != 0:
            for multiple in range(number,limit,number):
                final.add(multiple)
    return sum(final) #converted to set to get rid of duplicates