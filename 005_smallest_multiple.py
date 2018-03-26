#!/usr/bin/env python
import sys

from utils import (
    factors,
    is_prime,
    )


def main():
    n = int(sys.argv[1])
    must_be_divisible = set(range(2, n+1))

    p = 1
    for prime in [x for x in must_be_divisible if is_prime(x)]:
        p *= prime

    x = p
    while True:
        x_factors = set(factors(x))
        if must_be_divisible.issubset(x_factors):
            print(x)
            break
        x += p


if __name__ == '__main__':
    main()
