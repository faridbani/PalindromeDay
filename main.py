""" Palindrome days sense 0000 00 00 """
import datetime

global data
global old_date

# initializing the global variables
date = datetime.datetime(1020, 2, 1)
old_date = datetime.datetime(1100, 1, 1)


def is_palindrome(d):
    """ Checks if the date is a Palindrome day """

    f = False
    year = d.strftime("%Y")
    mount = d.strftime("%m")
    day = d.strftime("%d")
    print(year, mount, day)

    if (year[0] == day[1]) and \
        (year[1] == day[0]) and \
        (year[2] == mount[1]) and \
        (year[3] == mount[0]):
        f = True
    return f


def diff_years(date1, date2):
    """ Calculate the diff between the years"""

    y1 = int(date1.strftime("%Y"))
    y2 = int(date2.strftime("%Y"))
    print(y2-y1, "years is gone.")


def during(old_da, d):
    """ go throughout all days """
    pass


def go_thr():
    pass


test = is_palindrome(date)
print(test)