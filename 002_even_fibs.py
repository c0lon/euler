#!/usr/bin/env python
import sys


def fib():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b


def main():
    limit = int(sys.argv[1])
    s = 0
    for x in fib():
        if x > limit:
            break
        if not x % 2:
            s += x

    print(s)


if __name__ == '__main__':
    main()
