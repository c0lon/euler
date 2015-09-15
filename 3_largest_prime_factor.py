#!/usr/bin/env python

# What is the largest prime factor of the number 600851475143?
# answer = 6857

import sys
from pprint import pprint

def is_prime(x):
    if x < 2 or not x & 1:
        return False

    for i in range(3, int(x**0.5), 2):
        if not x % i: return False

    return True

def largest_prime_factor(x):
    for i in range(int(x**0.5), 0, -1):
        if not x % i and is_prime(i):
            return i

if __name__ == '__main__':
    n = 600851475143
    if len(sys.argv) == 2:
        n = int(sys.argv[1])

    print(largest_prime_factor(n))