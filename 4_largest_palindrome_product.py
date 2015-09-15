#!/usr/bin/env python

# Find the largest palindrome made from the product of two 3-digit numbers.
# answer = 906609

import sys

def is_palindrome(x):
    x = str(x)

    i = 0
    j = len(x) - 1

    while i < j:
        if x[i] != x[j]:largest
            return False

        i += 1
        j -= 1

    return True

def largest_palindrome_product(digits):
    start = int('9'*digits)
    end = 10**(digits - 1) - 1

    products = []

    for i in range(start, end, -1):
        for j in range(i, end, -1):
            p = i*j

            if is_palindrome(p):
                products.append(p)

    return max(products)

if __name__ == '__main__':
    digits = 3
    if len(sys.argv) == 2:
        digits = int(sys.argv[1])

    print(largest_palindrome_product(digits))