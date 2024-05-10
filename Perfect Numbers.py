def classify(number: int) -> str:
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number <= 0:
        raise ValueError('Classification is only possible for positive integers.')
    
    #Extracting Factors
    factors = [factor for factor in range(1, number) if number % factor == 0]
    
    #Final Decisions
    if sum(factors) == number:
        return 'perfect'
    if sum(factors) > number:
        return 'abundant'
    return 'deficient'