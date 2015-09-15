#!/usr/bin/env python

# What is the sum of the digits of the number 2^1000?
# answer = 1366

import sys

def sum_digits(x):
    return sum([int(x) for x in str(x)])

if __name__ == '__main__':
    n = 1000
    if len(sys.argv) == 2:
        n = int(sys.argv[1])

    print(sum_digits(2**n))