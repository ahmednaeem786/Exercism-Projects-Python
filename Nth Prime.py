import math


def prime(number: int) -> int:
    if number < 1:
        raise ValueError('there is no zeroth prime')
    
    prime_numbers = []
    my_number = 2
    while len(prime_numbers) < number:
        if is_prime(my_number):
            prime_numbers.append(my_number)
        my_number += 1
    return prime_numbers[-1]
        
        
def is_prime(number: int):
    for index in range(2, int(math.sqrt(number)) + 1):
        if number % index == 0: #Checking if it is divisible by any other number rather than itself and 1
            return False
    return True

print(prime(101))