"""
File: complement.py
Name: Shane Liu
-------------------------
This program uses string manipulation to 
find the complement strand of a DNA sequence.
"""


def main():
    """
    This program finds the complement strand of a DNA sequence,
    through following rules: (1)A<-->T (2)C<-->G    
    """
    dna = input('Please give me a DNA strand and I\'ll find the complement: ')
    complement = build_complement(dna)
    print('The complement of '+str(dna)+' is '+complement)


def build_complement(dna):
    """
    :param dna: str, a DNA sequence
    :return: str, the complement strand of a DNA sequence
    """
    # case-insensitive
    dna = dna.upper()
    complement = ''
    for i in dna:
        if i == 'A':
            complement += 'T'
        elif i == 'T':
            complement += 'A'
        elif i == 'G':
            complement += 'C'
        elif i == 'C':
            complement += 'G'
    return complement


if __name__ == '__main__':
    main()
