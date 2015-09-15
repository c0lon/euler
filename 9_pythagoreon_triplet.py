#!/usr/bin/env python

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
# answer = 31875000

import sys

def pythagorean_triplet(x):
	for a in range(1, x):
		for b in range(a, x):
			c = (a**2 + b**2)**0.5

			if c > b and a + b + c == x:
				return int(a*b*c)

if __name__ == '__main__':
	x = 1000
	if len(sys.argv) == 2:
		x = int(sys.argv[1])

	print(pythagorean_triplet(x))