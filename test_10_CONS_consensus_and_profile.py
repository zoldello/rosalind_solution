#!/usr/bin/env python

'''
A solution to a ROSALIND bioinformatics problem.
Problem Title: Rabbits and Recurrence Relations
Rosalind ID: CONS
Rosalind #: 010
URL: http://rosalind.info/problems/rna/
'''
import constants
import validator


def method(n, k):


def main():
    print('Input  two numbers for n and k, space separated: ')
    string = input()
    n, k = [int(s) for s in string.split(' ') if s != ' ']
    print(f'{n} {k}')
    calc = method(n, k)
    print(calc)


if __name__ == '__main__':
    main()
