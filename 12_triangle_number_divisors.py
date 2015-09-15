#!/usr/bin/env python

# What is the value of the first triangle number to have over five hundred divisors?

import sys

def divisors(x):
    ds = 2

    if not x & 1: ds += 2

    for i in range(3, int(x**0.5)):
        if not x % i:
            ds += 2

    return ds

def triangle_number_n_divisors(n):
    x, y = 1, 2
    while divisors(x) <= n:
        x += y
        y += 1

    return x

if __name__ == '__main__':
    n = 500
    if len(sys.argv) == 2:
        n = int(sys.argv[1])

    print(triangle_number_n_divisors(n))