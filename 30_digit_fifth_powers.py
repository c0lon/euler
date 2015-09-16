#!/usr/bin/env python

# Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
# 1634 = 14 + 64 + 34 + 44
# 8208 = 84 + 24 + 04 + 84
# 9474 = 94 + 44 + 74 + 44
# As 1 = 14 is not a sum it is not included.
# The sum of these numbers is 1634 + 8208 + 9474 = 19316.
# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
# answer = 

import sys
import utils
from pprint import pprint

def digit_power_sums(n):
    if n < 2:
        return 0

    end = int('1'+'0'*n)
    power_sums = []

    for x in range(2, (n+1)*pow(9, n)):
        if sum([pow(int(d), n) for d in str(x)]) == x:
            power_sums.append(x)

            s = ' + '.join(['{}^{}'.format(d, n) for d in str(x)])
            s += ' = {}'.format(sum([pow(int(d), n) for d in str(x)]))
            print('{}\n{}\n'.format(x, s))

    return sum(power_sums)

if __name__ == '__main__':
    n = 5
    if len(sys.argv) == 2:
        n = int(sys.argv[1])

    print(digit_power_sums(n))