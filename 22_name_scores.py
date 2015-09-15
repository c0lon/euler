#!/usr/bin/env python

# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
# So, COLIN would obtain a score of 938 × 53 = 49714.

# What is the total of all the name scores in the file?
# answer = 871198282

import sys
from pprint import pprint

ALPHA = {}
i = 1
for c in 'abcdefghijklmnopqrstuvwxyz':
    ALPHA[c] = i
    i += 1

def name_scores(raw_names):
    names = []
    for raw_name in raw_names.split(','):
        names.append(raw_name[1:-1].lower())
    names = sorted(names)

    total_score = 0
    for name in names:
        value = sum([ALPHA[c] for c in name])
        score = value * (names.index(name) + 1)
        total_score += score

    return total_score

if __name__ == '__main__':
    filename = '22_names.txt'
    if len(sys.argv) == 2:
        filename = sys.argv[1]

    with open(filename, 'r') as f:
        print(name_scores(f.read()))