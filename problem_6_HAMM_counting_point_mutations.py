#!/usr/bin/env python

'''
A solution to a ROSALIND bioinformatics problem.
Problem Title: Rabbits and Recurrence Relations
Rosalind ID: hamm
Rosalind #: 006
URL: http://rosalind.info/problems/hamm/
'''
import validator
import operator


def get_hamming_distance(dna_string_1, dna_string_2):
    is_dna_string_1_valid = validator.is_string_valid_dna_string(dna_string_1)
    is_dna_string_2_valid = validator.is_string_valid_dna_string(dna_string_2)

    if not is_dna_string_1_valid or not is_dna_string_2_valid:
        print(f'One or both dna strings are invalid: {dna_string_1}, {dna_string_2}')
        return None

    if len(dna_string_1) != len(dna_string_2):
        print(f'length of dna strings must match')
        return None

    diff_count = map(operator.ne, dna_string_1, dna_string_2)
    return sum(diff_count)


def main():
    dna_strings = input('Input two dna strings to find their Hamming Distance, space separated:')
    dna_sting_1, dna_string_2 = [dna_string for dna_string in dna_strings.split(' ')  if dna_string != '']
    diff_count = get_hamming_distance(dna_sting_1, dna_string_2)
    print(diff_count)


if __name__ == '__main__':
    main()
