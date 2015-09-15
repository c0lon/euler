#!/usr/bin/env python

# Find the sum of the digits in the number 100!
# answer = 648

import sys

def factorial(x):
    fac = 1
    for i in range(2, x+1):
        fac *= i

    return fac

def fac_digit_sum(x):
    return sum([int(i) for i in str(factorial(x))])

if __name__ == '__main__':
    x = 10
    if len(sys.argv) == 2:
        x = int(sys.argv[1])

    print(fac_digit_sum(x))