#!/usr/bin/env python

# A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

# 1/2= 0.5
# 1/3= 0.(3)
# 1/4= 0.25
# 1/5= 0.2
# 1/6= 0.1(6)
# 1/7= 0.(142857)
# 1/8= 0.125
# 1/9= 0.(1)
# 1/10= 0.1

# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.
# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
# answer = 983

# notes
# http://mathworld.wolfram.com/FullReptendPrime.html
# full reptend primes
# A prime p is full reptend iff 10 is a primitive root modulo p, which means that
# 10^k = 1(mod p)     
# for k = p - 1 and no k less than this
#
# for k in range(1, p):
#    pow(10, k, p) must be unique
#    since the first modulo, 1 % p, is always 1, we can do while(pow(10, k, p) != 1)
#    
# since we're doing this in reverse order, the first full reptend prime is the answer
# a full reptend prime p has a cyclic period of length p-1

import sys
from pprint import pprint
import utils

def longest_recurring_cycle(n):
    for denom in utils.primes(n)[::-1]:
        period_length = 1

        # 1 % denom is always 1, so when it's seen again we know the period is over
        while pow(10, period, denom) != 1:
            period_length += 1

        # reptend prime check
        if denom - 1 == period_length:
            return denom

if __name__ == '__main__':
    n = 1000
    if len(sys.argv) == 2:
        n = int(sys.argv[1])

    print(longest_recurring_cycle(n))