#!/usr/bin/env python

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
# answer = 25164150

'''
sum of squares
    x_1^2 + x_2^2 + ... + x_n^2

square of sum
    (x_1 + x_2 + ... + x_n)^2
    -> x_1(x_1 + x_2 + ... + x_n) + x_2(x_1 + x_2 + ... + x_n) + ... + x_n(x_1 + x_2 + ... + x_n)
    -> x_1^2 + x_1*x_2 + ... + x_1*x_n + x_2*x_1 + x_2^2 + ... + x_2*x_n + ... + x_n*x_1 + x_n*x_2 + ... + x_n^2
'''

import sys

def sum_square_difference(n):
    return sum([x*y for x in range(1, n+1) for y in range(1, n+1) if x!= y])

if __name__ == '__main__':
    n = 100
    if len(sys.argv) == 2:
        n = int(sys.argv[1])

    print(sum_square_difference(n))