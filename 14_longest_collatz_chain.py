#!/usr/bin/env

# n_1 = n_0/2    (even)
# n_1 = 3n_0 + 1 (odd)
# Which starting number, under one million, produces the longest chain?

import sys

CHAINS = {}

def collatz_chain(n_0):
    global CHAINS
    
    n = n_0
    length = 1
    while n != 1:
        if n in CHAINS:
            length += CHAINS[n]
            break

        if not n & 1:
            n = int(n/2)
        else:
            n = 3*n + 1

        length += 1

    CHAINS[n_0] = length

def longest_collatz_chain(n):
    for i in range(1, n):
        collatz_chain(i)

    m, n = 0, 0
    for n_0, length in CHAINS.items():
        if length > m:
            n, m = n_0, length

    return n

if __name__ == '__main__':
    n = 1000000
    if len(sys.argv) == 2:
        n = int(sys.argv[1])

    print(longest_collatz_chain(n))