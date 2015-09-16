#!/usr/bin/env python

# Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:
# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13
# It can be verified that the sum of the numbers on the diagonals is 101.
# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
# answer = 669171001

import sys
import utils
from pprint import pprint

def spiral_diagonal_sum(n):
    if not n & 1:
        print('n must be odd')
        return 0

    total = 1

    level = 2
    offset = 1
    while level <= int(n/2) + 1:
        square = pow(level+offset, 2)
        total += square

        inc = level + offset - 1
        for i in range(1, 4):
            total += square - i*inc

        offset = level
        level += 1

    return total

if __name__ == '__main__':
    n = 1001
    if len(sys.argv) == 2:
        n = int(sys.argv[1])

    print(spiral_diagonal_sum(n))