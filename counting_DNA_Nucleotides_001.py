 
#!/usr/bin/env python

'''
A solution to a ROSALIND bioinformatics problem.
Problem Title: Counting DNA Nucleotides
Rosalind ID: DNA
Rosalind #: 001
URL: http://rosalind.info/problems/dna/
'''

from collections import Counter

VALID_NUCLEOTIDES_CHARACTERS = ['A','C', 'G', 'T']


def is_string_right_len(string, expected_len):
    if not string or string.strip() == '':
        return False
    return len(string) <= expected_len 


def is_string_valid(string):
    if not string:
        return False
    invalid_nucleotide = [nucleotide for nucleotide in string if nucleotide not in VALID_NUCLEOTIDES_CHARACTERS]
    return len(invalid_nucleotide) == 0


def get_nucleotide_count(string):
    if not is_string_valid(string):
        return None
    if not is_string_right_len(string, 1000):
        return None
    nucleotide_count = Counter(string)
    count = []

    # results has to be in count order of 'A C G T'
    for nucleotide in VALID_NUCLEOTIDES_CHARACTERS:
        count.append(nucleotide_count[nucleotide])
    return ' '.join([str(n) for n in count])


def main():
    print('Input a string: ')
    string = input()
    nucleotide_count = get_nucleotide_count(string)
    print(nucleotide_count)


if __name__ == '__main__':
    main()
