#!/usr/bin/env python

# Find the sum of all the primes below two million.
# answer = 142913828922

import sys

def primes(n):
	xs = {}
	for x in range(1, n+1):
		xs[x] = False

	primes = []

	p = 2
	pp = 0
	while p != pp:
		pp = p

		for x in range(p, len(xs), p):
			xs[x] = True

		while xs[p]:
			p += 1

		if pp != p:
			primes.append(pp)

	return primes

def sum_primes(n):
	ps = primes(n)
	return sum(ps)

if __name__ == '__main__':
	n = 2000000
	if len(sys.argv) == 2:
		n = int(sys.argv[1])

	print(sum_primes(n))