#!/usr/bin/env python

# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

# Evaluate the sum of all the amicable numbers under 10000.
# answer = 31626

from pprint import pprint
import sys

def sum_factors(x):
    if x == 0:
        return 0

    fs = [1]

    if x == 1:
        return sum(fs)

    if not x & 1:
        fs.append(2)
        fs.append(int(x/2))

    for i in range(3, int(x**0.5)+1):
        if not x % i:
            fs.append(i)
            fs.append(int(x/i))

    if x in fs:
        fs.remove(x)
    return sum(set(fs))

def sum_amicable_numbers(n):
    factor_sums = {0 : []}
    amicables = set()
    
    x = 0
    while True:
        x += 1

        factor_sum = sum_factors(x)
        if factor_sum not in factor_sums:
            factor_sums[factor_sum] = [x]
        else:
            factor_sums[factor_sum].append(x)

        if x != factor_sum and x in factor_sums and factor_sum in factor_sums[x]:
            if factor_sum > n or x > n:
                return sum(amicables)

            amicables.add(factor_sum)
            amicables.add(x)

if __name__ == '__main__':
    n = 10000
    if len(sys.argv) == 2:
        n = int(sys.argv[1])

    print(sum_amicable_numbers(n))