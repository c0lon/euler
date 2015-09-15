#!/usr/bin/env python

# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
# answer = 2783915460

import sys
import utils

def nth_permutation(n):
    return ''.join([str(x) for x in utils.permutations(10)[n-1]])

if __name__ == '__main__':
    n = 1000000
    if len(sys.argv) == 2:
        n = int(sys.argv[1])

    print(nth_permutation(n))