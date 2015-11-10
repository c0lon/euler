#!/usr/bin/env python

# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

# The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
# answer = 45228

import sys
import utils
from pprint import pprint

def pandigital_products():
    pan_prods = []

    for _perm in utils.permutations(1, 9):
        perm = ''.join([str(p) for p in _perm])

        for i in range(1, 4):
            x = int(perm[:i])
            for j in range(i + 1, 7):
                y = int(perm[i:j])
                z = int(perm[j:])

                if x * y == z and z not in pan_prods:
                    print('{} * {} = {}'.format(x, y, z))
                    pan_prods.append(z)

    return sum(pan_prods)

if __name__ == '__main__':
    print(pandigital_products())