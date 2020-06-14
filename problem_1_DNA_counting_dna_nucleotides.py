 #!/usr/bin/env python

'''
A solution to a ROSALIND bioinformatics problem.
Problem Title: Counting DNA Nucleotides
Rosalind ID: DNA
Rosalind #: 001
URL: http://rosalind.info/problems/dna/
'''

import validator
import constants


def get_nucleotide_count(dna_string):
    if not validator.is_string_valid_dna_string(dna_string):
        return None
    if not validator.is_string_right_len(dna_string, 1000):
        return None
    valid_nucleotides = ''.join(constants.VALID_DNA_NUCLEOTIDES_CHARACTERS)
    nucleotide_count = [str(n) for n in map(dna_string.count, valid_nucleotides)]
    return ' '.join(nucleotide_count)


def main():
    print('Input a string: ')
    dna_string = input()
    nucleotide_count = get_nucleotide_count(dna_string)
    print(nucleotide_count)


if __name__ == '__main__':
    main()
