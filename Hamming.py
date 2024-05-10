def distance(strand_a: str, strand_b: str) -> int:
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    discrepancy_counter = 0
    strand_a = list(strand_a)
    strand_b = list(strand_b)
    for index in range(len(strand_a)):
        if strand_a[index] != strand_b[index]:
            discrepancy_counter += 1
    return discrepancy_counter



def distance(strand_a: str, strand_b: str) -> int:
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    return sum(strand_a[index] != strand_b[index] 
               for index in range(len(strand_a)))