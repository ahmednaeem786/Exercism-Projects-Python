import textwrap
codon_protein = {'AUG': 'Methionine',
                 'UUU': 'Phenylalanine',
                 'UUC': 'Phenylalanine',
                 'UUA': 'Leucine',
                 'UUG': 'Leucine',
                 'UCU': 'Serine',
                 'UCC': 'Serine',
                 'UCA': 'Serine',
                 'UCG': 'Serine',
                 'UAU': 'Tyrosine',
                 'UAC': 'Tyrosine',
                 'UGU': 'Cysteine',
                 'UGC': 'Cysteine',
                 'UGG': 'Tryptophan',
}


def proteins(strand: str) -> list[str]:
    strand_split = textwrap.wrap(strand, 3)
    final = []
    for codons in strand_split:
        if codons in ('UAA', 'UAG', 'UGA'):
            break
        final.append(codon_protein[codons])
    return final