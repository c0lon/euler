#!/usr/bin/env python

# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
# answer = 4613732

def sum_even_fibs(limit):
	
	f = [1, 1]
	total = 0
	while f[-1] < limit:
		f.append(f[-1] + f[-2])
		if not f[-1] % 2:
			total += f[-1]

	return total

if __name__ == '__main__':
	print(sum_even_fibs(4000000))