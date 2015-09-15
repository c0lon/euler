#!/usr/bin/env python

# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
# answer = 4782

import sys

def n_digit_fibonacci(n):
    fibs = [1, 1]
    while len(str(fibs[-1])) < n:
        fibs.append(fibs[-1] + fibs[-2])

    return len(fibs)

if __name__ == '__main__':
    n = 1000
    if len(sys.argv) == 2:
        n = int(sys.argv[1])

    print(n_digit_fibonacci(n))