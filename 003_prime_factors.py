#!/usr/bin/env python
import sys

from utils import (
    is_prime,
    factors,
    )


def main():
    n = int(sys.argv[1])
    print(max([x for x in factors(n) if is_prime(x)]))


if __name__ == '__main__':
    main()
