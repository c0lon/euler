#!/usr/bin/env python

# Find the sum of all the multiples of 3 or 5 below 1000.
# answer = 233168

def sum_multiples_of_3_and_5(n):
	total = 0

	for x in range(n):
		if not x % 3:
			total += x
		elif not x % 5:
			total += x

	return total

if __name__ == '__main__':
	print(sum_multiples_of_3_and_5(1000))