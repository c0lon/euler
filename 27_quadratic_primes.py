#!/usr/bin/env python

# Euler discovered the remarkable quadratic formula:
# n² + n + 41
# It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41² + 41 + 41 is clearly divisible by 41.
# The incredible formula  n² − 79n + 1601 was discovered, which produces 80 primes for the consecutive values n = 0 to 79. The product of the coefficients, −79 and 1601, is −126479.
# Considering quadratics of the form:

# n² + an + b, where |a| < 1000 and |b| < 1000where |n| is the modulus/absolute value of ne.g. |11| = 11 and |−4| = 4

# Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.
# answer = -59231

import sys
import utils
from pprint import pprint

def most_consecutive_primes(n):
    # given n^2 + ax + b, assume the highest result we can get is 2n^2 + n
    # generate all primes up to that
    _primes = utils.primes(2*pow(n, 2) + n)
    primes = {}
    for p in _primes:
        primes[p] = True

    a, b = 0, 0
    ps = 0

    for _a in range(n):
        for _b in range(n):

            # consider all combos of positive/negative
            for __a, __b in [(_a, _b), (-_a, _b), (-_a, -_b), (_a, -_b)]:
                # create the function
                def f(x):
                    return pow(x, 2) + __a*x + __b

                # look for primes
                x = 0
                _ps = -1
                while primes.get(f(x)):
                    _ps += 1
                    x += 1

                if _ps > ps:
                    a, b = __a, __b
                    ps = _ps

    return a*b

if __name__ == '__main__':
    n = 1000
    if len(sys.argv) == 2:
        n = int(sys.argv[1])

    print(most_consecutive_primes(n))