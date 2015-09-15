#!/usr/bin/env python

# What is the 10 001st prime number?
# ansewr = 104743

import sys

def primes(n):
    xs = {}
    for i in range(2, n+1):
        xs[i] = False

    primes = []

    p = 2
    pp = 0
    while p != pp:
        pp = p

        for x in range(p, n, p):
            xs[x] = True

        while xs[p]:
            p += 1

        if pp != p:
            primes.append(pp)

    return primes

def nth_prime(n):
    _n = n
    ps = primes(_n)
    while len(ps) < n:
        _n *= 2
        ps = primes(_n)

    return ps[n-1]

if __name__ == '__main__':
    n = 10001
    if len(sys.argv) == 2:
        n = int(sys.argv[1])

    print(nth_prime(n))