#!/usr/bin/env python

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
# answer = 232792560

import sys

def reduce_factors(xs):
    ys = [x for x in xs]

    for i in range(len(xs)-1, 0, -1):
        for j in range(i-1, 0, -1):
            x = xs[i]
            y = xs[j]

            if not x % y and y in ys: ys.remove(y)

    return ys

def divisible_by_all(x, ys):
    for y in ys:
        if x % y: return False

    return True

def smallest_multiple(n):
    xs = reduce_factors([x for x in range(2, n+1)])

    m = max(xs)
    p = m
    while not divisible_by_all(p, xs):
        p += m

    return p

if __name__ == '__main__':
    n = 20
    if len(sys.argv) == 2:
        n = int(sys.argv[1])

    print(smallest_multiple(n))