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


def transcribe_dna_to_rna(dna_string):
    if not validator.is_string_valid_dna_string(dna_string):
        return None

    if not validator.is_string_right_len(dna_string, 1000):
        return None

    transcribed_rna = dna_string.replace('T', 'U')

    if not validator.is_string_valid_rna_string(transcribed_rna):
        return None

    return transcribed_rna


def main():
    print('Input a string: ')
    string = input()
    nucleotide_count = transcribe_dna_to_rna(string)
    print(nucleotide_count)


if __name__ == '__main__':
    main()
