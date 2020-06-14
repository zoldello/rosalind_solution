#!/usr/bin/env python

'''
A solution to a ROSALIND bioinformatics problem.
Problem Title: Transcribing DNA into RNA 
Rosalind ID: RNA
Rosalind #: 002
URL: http://rosalind.info/problems/rna/
'''

import constants
import validator


def dna_string_reverse_complement(dna_string):
    if not validator.is_string_valid_dna_string(dna_string):
        return None

    if not validator.is_string_right_len(dna_string, 1000):
        return None
    
    complement = [constants.COMPLEMENTS[nucleotide] for nucleotide in dna_string]
    reverse_complement = complement[::-1]
    return ''.join(reverse_complement)    


def main():
    print('Input a string: ')
    dna_string = input()
    reverse_complement = dna_string_reverse_complement(dna_string)
    print(reverse_complement)


if __name__ == '__main__':
    main()
