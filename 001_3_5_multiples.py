#!/usr/bin/env python
import sys


def main():
    n = int(sys.argv[1])
    print(sum([x for x in range(n) if x % 3 == 0 or x % 5 == 0]))


if __name__ == '__main__':
    main()
