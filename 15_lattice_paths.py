#!/usr/bin/env python

# starting from top left, move to bottom right, can only go right or down
# How many such routes are there through a 20×20 lattice?
# answer = 137846528820

import sys

'''def _lattice_paths(lattice, start, end, visited, routes):
    visited.append(start)
    if start == end:
        return routes + 1

    for v in lattice[start]:
        if v not in visited:
            routes = _lattice_paths(lattice, v, end, visited, routes)
            visited.remove(v)

    return routes

def lattice_paths(lattice):
    vs = [v for v in lattice.keys()]
    start, end = vs[0], vs[-1]

    return _lattice_paths(lattice, start, end, [], 0)

if __name__ == '__main__':
    n = 20
    if len(sys.argv) == 2:
        n = int(sys.argv[1])

    lattice = {}
    N = n + 1
    for i in range(N**2):
        row = int(i/N)
        col = i % N

        v = lattice[i] = []

        # right
        if col < n:
            v.append(i+1)

        # down
        if row < n:
            v.append(i+N)

    print(lattice_paths(lattice))'''

# use math

def lattice_paths(n):
    lattice = []
    for i in range(0, n+1):
        lattice.append([])
        row = lattice[i]

        for j in range(0, i+1):

            if j == 0:
                row.append(1)
            elif j < i:
                row.append(row[j-1] + lattice[i-1][j])
            elif j == i:
                row.append(2*row[j-1])

    return lattice[n][n]

if __name__ == '__main__':
    n = 20
    if len(sys.argv) == 2:
        n = int(sys.argv[1])

    print(lattice_paths(n))