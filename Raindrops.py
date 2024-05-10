def convert(number: int) -> str:
    final_string = ''
    
    if number % 3 == 0:
        final_string += 'Pling'
    if number % 5 == 0:
        final_string += 'Plang'
    if number % 7 == 0:
        final_string += 'Plong'
    
    return str(number) if final_string == '' else final_string