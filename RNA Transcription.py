def to_rna(dna_strand: str) -> str:
    final_result=''
    for single_strand in dna_strand:
        if single_strand == 'G':
            final_result += 'C'
        if single_strand == 'C':
            final_result += 'G'
        if single_strand == 'T':
            final_result += 'A'
        if single_strand == 'A':
            final_result += 'U'
    return final_result

def to_rna(dna_strand: str) -> str:
    translation = str.maketrans('GCTA', 'CGAU')
    return dna_strand.translate(translation)
#This code is much faster and accepts complex translations (better refactoring)
# Cleaner and Concise Solution than previous, more readable and more efficient 
# than previous iteration