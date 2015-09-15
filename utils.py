#!/usr/bin/env python

# a collection of utilities that are commonly used in project euler challenges

import argparse
import os.path
import sys

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

# generate a new file
if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser(description='generate a template file for a project euler challenge.')
    arg_parser.add_argument('filename')
    args = arg_parser.parse_args()

    if os.path.exists(args.filename):
        print('file <{}> already exists.'.format(args.filename))
        overwrite = input('overwrite? [y/n] ')
        if overwrite.lower()[0] == 'n':
            sys.exit()

    with open(args.filename, 'w+') as f:
        f.write('')