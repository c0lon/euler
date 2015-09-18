#!/usr/bin/env python

# In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:
# 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
# It is possible to make £2 in the following way:
# 1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
# How many different ways can £2 be made using any number of coins?
# answer = 73682

import sys
import utils
from pprint import pprint

coins = [
    1,
    2,
    5,
    10,
    20,
    50,
    100,
    200
]

def _coin_sums(x, curr):

    if sum(curr) == x:
        return 1

    sums = 0
    try:
        start = coins.index(curr[-1])
    except IndexError:
        start = -1
        for coin in coins:
            if coin <= x: start += 1

    for i in range(start, -1, -1):
        added = 0
        while sum(curr) + coins[i] <= x:
            curr.append(coins[i])
            added += 1

        if sum(curr) == x:
            sums += 1

        while added:
            if sum(curr) < x:
                for j in range(i-1, -1, -1):
                    curr.append(coins[j])
                    sums += _coin_sums(x, curr)
                    curr.pop()
            curr.pop()
            added -= 1

    return sums

def coin_sums(x):
    return _coin_sums(x, [])

if __name__ == '__main__':
    x = 200
    if len(sys.argv) == 2:
        x = int(sys.argv[1])

    print(coin_sums(x))