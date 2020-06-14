'''
Pytest of constant.py
'''

import constants

def test_VALID_DNA_NUCLEOTIDES_CHARACTERS():
    expected = ['A','C', 'G', 'T']
    assert constants.VALID_DNA_NUCLEOTIDES_CHARACTERS == expected
 
def test_VALID_RNA_NUCLEOTIDES_CHARACTERS():
    expected = ['A','C', 'G', 'U']
    assert constants.VALID_RNA_NUCLEOTIDES_CHARACTERS == expected
