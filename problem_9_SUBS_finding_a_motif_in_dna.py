 #!/usr/bin/env python

'''
A solution to a ROSALIND bioinformatics problem.
Problem Title: Counting DNA Nucleotides
Rosalind ID: SUB
Rosalind #: 009
URL: http://rosalind.info/problems/dna/
'''

import re
import validator
import constants


def get_substring_occurences(dna_substring, dna_string):
    if not validator.is_string_valid_dna_string(dna_string):
        return None
    if not validator.is_string_valid_dna_string(dna_substring):
        return None
    if not validator.is_string_right_len(dna_string, constants.DNA_MAX_LENGTH):
        return None
    if dna_string == None or dna_substring == None:
        return None
    if dna_string.strip() == '':
        return [0]
    if dna_string.strip() == '':
        return None
    if len(dna_string) < len(dna_substring):
        return None

    dna_substring_starting_indices = [
        m.start() + 1
        for m in re.finditer(f'(?={dna_substring.strip()})', dna_string.strip())
    ]
    return ' '.join(str(index) for index in dna_substring_starting_indices)


def main():
    print('Input a dna string and sub string separated by space: ')
    dna_substring, dna_string = input().split(' ')
    substring_indices = get_substring_occurences(dna_substring, dna_string)
    print(substring_indices)


if __name__ == '__main__':
    main()
