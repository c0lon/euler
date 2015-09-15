#!/usr/bin/env python

# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
# answer = 171

from pprint import pprint

DAYS = [
    'Sunday',
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday'
]

MONTHS = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December'
]

MONTH_LENGTHS = [
    31,
    28,
    31, 
    30,
    31,
    30,
    31,
    31,
    30,
    31,
    30,
    31
]

def is_leap_year(date):
    if not date['year'] % 100:
        return not date['year'] % 400

    return not date['year'] % 4

def sunday_count():
    global MONTH_LENGTHS

    date = {
        'day'   : 1,
        'date'  : 1,
        'month' : 0,
        'year'  : 1900
    }
    first_sundays = 0

    while date['year'] <= 2000:

        # twentieth century
        if date['year'] > 1900 and date['year'] <= 2000:
            # first sunday
            if date['day'] == 0 and date['date'] == 1:
                first_sundays += 1

        # handle leap years
        leap_year = is_leap_year(date)
        if leap_year and MONTH_LENGTHS[1] == 28:
            MONTH_LENGTHS[1] = 29
        elif not leap_year and MONTH_LENGTHS[1] == 29:
            MONTH_LENGTHS[1] = 28

        # handle day of week
        date['day'] = (date['day'] + 1) % len(DAYS)

        # handle day of month
        if date['date'] < MONTH_LENGTHS[date['month']]:
            date['date'] += 1
        elif date['date'] == MONTH_LENGTHS[date['month']]:
            date['date'] = 1

            # new year
            if date['month'] == 11:
                date['year'] += 1

            # new month
            date['month'] = (date['month'] + 1) % len(MONTHS)

    return first_sundays

if __name__ == '__main__':
    print(sunday_count())