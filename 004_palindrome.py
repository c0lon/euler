#!/usr/bin/env python
import sys

from utils import is_palindrome


def main():
    n = int(sys.argv[1])
    number_range = lambda n: range((10**n)-1, 10**(n-1), -1)

    palindromes = set()
    for x in number_range(n):
        for y in number_range(n):
            z = x * y
            if is_palindrome(z):
                palindromes.add(z)

    print(max(palindromes))


if __name__ == '__main__':
    main()
