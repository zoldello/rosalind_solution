#!/usr/bin/env python

'''
Collection of constants
'''

VALID_DNA_NUCLEOTIDES_CHARACTERS = ['A','C', 'G', 'T']
VALID_RNA_NUCLEOTIDES_CHARACTERS = ['A','C', 'G', 'U']
COMPLEMENTS = {
    'A': 'T',
    'C': 'G',
    'T': 'A',
    'G': 'C',
}
DNA_MAX_LENGTH = 1000