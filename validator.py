#!/usr/bin/env python

'''
Collection of genomic validation functions
'''

import constants

def is_string_right_len(string, expected_len):
    if not string or string.strip() == '':
        return False
    return len(string) <= expected_len 



def is_string_valid_dna_string(dna_string):
    '''
    Determines if dna string has all valid nucleotides selected from ('A', 'C'.'T'. 'G')

    Parameters
    ----------
    dna_string : str
        DNA string

    Returns
    -------
    bool
        True if DNA is valid, false otherwise.
    '''
    if not dna_string:
        return False
    invalid_nucleotides = [nucleotide for nucleotide in dna_string if nucleotide not in constants.VALID_DNA_NUCLEOTIDES_CHARACTERS]
    return len(invalid_nucleotides) == 0


def is_string_valid_rna_string(rna_string):
    '''
    Determines if rna string is valid

    Parameters
    ----------
    rna_string : string
        RNA string

    Returns
    -------
    string
        True if RNA string is valid, false otherwise
    '''
    if not rna_string:
        return False
    invalid_nucleotides = [nucleotide for nucleotide in rna_string if nucleotide not in constants.VALID_RNA_NUCLEOTIDES_CHARACTERS]
    return len(invalid_nucleotides) == 0
