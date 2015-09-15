#!/usr/bin/env python

# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
# answer = 21124

import sys

WORDS = {
    1 : 'one',
    2 : 'two',
    3 : 'three',
    4 : 'four',
    5 : 'five',
    6 : 'six',
    7 : 'seven',
    8 : 'eight',
    9 : 'nine',
    10 : 'ten',
    11 : 'eleven',
    12 : 'twelve',
    13 : 'thirteen',
    15 : 'fifteen',
    18 : 'eighteen',
    20 : 'twenty',
    30 : 'thirty',
    40 : 'forty',
    50 : 'fifty',
    60 : 'sixty',
    70 : 'seventy',
    80 : 'eighty',
    90 : 'ninety'
}

def letters(n):
    if n > 1000:
        print('pick a number between 1 and 1000')
        return 0

    count = 0
    
    for i in range(1, n + 1):
        word = ''

        if i in WORDS:
            word = WORDS[i]
        else:
            
            if i > 13 and i < 20:
                ones = i % 10
                word = WORDS[ones] + 'teen'

            elif i >= 20 and i < 100:
                ones = i % 10
                tens = i - ones
                word = WORDS[tens] + WORDS[ones]

            elif i >= 100 and i < 1000:
                ones = i % 10
                tens = (i - ones) % 100
                hundreds = (i - tens - ones) / 100

                word = WORDS[hundreds] + 'hundred'

                rest = tens + ones
                if rest in WORDS:
                    word += 'and' + WORDS[rest]
                else:
                    if tens == 10:
                        word += 'and' + WORDS[ones] + 'teen'
                    else:
                        if tens > 10:
                            word += 'and' + WORDS[tens]
                        if ones:
                            if tens:
                                word += WORDS[ones]
                            else:
                                word += 'and' + WORDS[ones]

            elif i >= 1000:
                word = 'onethousand'

        count += len(word)

    return count

if __name__ == '__main__':
    n = 1000
    if len(sys.argv) == 2:
        n = int(sys.argv[1])

    print(letters(n))