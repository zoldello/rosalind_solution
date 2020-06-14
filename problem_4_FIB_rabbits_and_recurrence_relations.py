#!/usr/bin/env python

'''
A solution to a ROSALIND bioinformatics problem.
Problem Title: Rabbits and Recurrence Relations
Rosalind ID: FIB
Rosalind #: 002
URL: http://rosalind.info/problems/rna/
'''
from functools import lru_cache
import constants
import validator

@lru_cache(maxsize=1000)
def fibonacci(n, k):
    """Calculates the n-th fibonnaci srquence with f(0) and f(1) = k

    Arguments:
        n {integer} -- The n-th sequence to calculate
        k {interger} -- f(1)

    Raises:
        TypeError: Ensures paramters are number
        ValueError: Ensures values are valid

    Returns:
        integer -- Fibonacci number
    """
    if type(n) != int or type(k) != int:
        raise TypeError(f'{n} and {k} must both be a number')
    if n < 0 or k < 0:
        raise ValueError(f'{n} and {k} must both be greater than 0')

    if n <= 2:
        return k
    else:
        return fibonacci(n-1, k) + fibonacci(n-2, k)


def main():
    print('Input  two numbers for n and k, space separated: ')
    string = input()
    n, k = [int(s) for s in string.split(' ') if s != ' ']
    print(f'{n} {k}')
    calc = fibonacci(n, k)
    print(calc)


if __name__ == '__main__':
    main()
