#!/usr/bin/env python

'''
A solution to a ROSALIND bioinformatics problem.
Problem Title: Transcribing DNA into RNA 
Rosalind ID: PROT
Rosalind #: 002
URL: http://rosalind.info/problems/prot/
'''
from Bio.Seq import Seq
import validator


def translate_rna_to_protein(rna_string):
    '''
    Translates RNA to Protein

    Parameters
    ----------
    rna_sting : string
        RNA string

    Returns
    -------
    string
        Protein
    '''
    if not validator.is_string_valid_rna_string(rna_string):
        raise ValueError(f'RNA string is not valid. The string given was: {rna_string}')

    rna_seq = Seq(rna_string)
    translated_protein = rna_seq.translate()
    breakpoint()
    return str(translated_protein)


def main():
    print('Input a string: ')
    dna_string = input()
   


if __name__ == '__main__':
    main()
