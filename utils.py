#!/usr/bin/env python

# a collection of utilities that are commonly used in project euler challenges

# given a positive integer, return all its factors
def factors(x, proper=False):
    if x <= 0:
        return []

    fs = set([1, x])

    if not x & 1:
        fs.add(2)
        fs.add(int(x/2))

    for i in range(3, int(x**0.5)+1):
        if not x % i:
            fs.add(i)
            fs.add(int(x/i))

    if proper:
        fs.remove(x)

    return list(fs)