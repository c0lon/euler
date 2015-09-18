#!/usr/bin/env python

# a collection of utilities that are commonly used in project euler challenges

import argparse
import os.path
import re
import sys

from bs4 import BeautifulSoup as bs
import requests

# return a list of primes up to n
def primes(n):
    if n < 2:
        return []

    if n == 2:
        return [2]

    xs = {}
    for i in range(2, n+1):
        xs[i] = False

    ps = []

    p = 2
    pp = 0
    while p != pp:
        pp = p

        for x in range(p, len(xs), p):
            xs[x] = True

        while xs[p]:
            p += 1

        if pp != p:
            ps.append(pp)

    return ps

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
    arg_parser.add_argument('-m', '--method')
    arg_parser.add_argument('-v', '--variable')
    arg_parser.add_argument('-d', '--default')
    args = arg_parser.parse_args()

    if os.path.exists(args.filename):
        print('file <{}> already exists.'.format(args.filename))
        overwrite = input('overwrite? [y/n] ')
        if 'y' not in overwrite.lower():
            sys.exit()

    problem_number = re.match(r'(\d+)', args.filename).group(1)
    problem_url = 'https://projecteuler.net/problem={}'.format(problem_number)
    soup = bs(requests.get(problem_url).text, 'html5lib')
    problem = soup('div', class_='problem_content')[0].text.strip()

    with open(args.filename, 'w+') as f:
        f.write('#!/usr/bin/env python\n\n')

        for line in problem.splitlines():
            if not line.strip():
                f.write('\n')
            else:
                f.write('# {}\n'.format(line.strip()))
        f.write('# answer = \n\n')

        f.write('import sys\n')
        f.write('import utils\n')
        f.write('from pprint import pprint\n')

        if args.method:
            variable = args.variable if args.variable else ''
            f.write('\ndef {}({}):\n    return 0\n'.format(
                args.method, variable))

        f.write('\nif __name__ == \'__main__\':\n')
        if args.default:
            if args.variable:
                f.write('    {} = {}\n'.format(args.variable, args.default))
            else:
                f.write('    n = {}\n'.format(args.default))

            f.write('    if len(sys.argv) == 2:\n')
            if args.variable:
                f.write('        {} = int(sys.argv[1])\n\n'.format(args.variable))
            else:
                f.write('        n = int(sys.argv[1])\n\n')

        if args.method:
            variable = args.variable if args.variable else ''
            f.write('    print({}({}))'.format(args.method, variable))