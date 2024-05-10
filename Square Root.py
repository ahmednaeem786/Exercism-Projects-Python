def square_root(number: int) -> int:
    if number < 0:
        raise ValueError("There are no square roots for negative values")
    
    guess = 1.0
    while guess ** 2 != number:  # Set to True so that loop runs infinitely until square root is found
        guess = (guess + number / guess) / 2  #Babylonian Method
    return round(guess)