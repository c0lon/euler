#!/usr/bin/env python

# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
# For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24.
# By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers.

# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
# answer = 4179871

import sys
import utils

def is_abundant(x):
    return sum(utils.factors(x, True)) > x

def non_abundant_sum(n):
    # generate abundant numbers
    abundance = []
    for x in range(n):
        if is_abundant(x):
            abundance.append(x)
    abundance = sorted(list(set(abundance)))

    abundant_sums = []
    for i in range(len(abundance)):
        for j in range(i, len(abundance)):
            abundant_sums.append(
                abundance[i] + abundance[j])
    abundant_sums = sorted(list(set(abundant_sums)))
    
    index = 0
    non_abundant_sums = []
    for i in range(n+1):
        if i == abundant_sums[index]:
            index += 1
        else:
            non_abundant_sums.append(i)

    return sum(non_abundant_sums)

if __name__ == '__main__':
    n = 28123
    if len(sys.argv) == 2:
        n = int(sys.argv[1])

    print(non_abundant_sum(n))