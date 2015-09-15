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

# return a list of all permutations of a range up to and including n
# given an list, maps the numerical permutations to the list
def permutations(n, obj=None):

    # nested recursive function
    def _permutations(curr, perms):
        for i in range(n):
            if i not in curr:
                curr.append(i)

                if len(curr) == n:
                    perms.append([x for x in curr])
                else:
                    perms = _permutations(curr, perms)

                curr.remove(i)

        return perms

    perms = _permutations([], [])

    if obj:
        pass

    return perms