""" Palindrome days sense 0001 01 01 """
import datetime


# initializing the global variables
date = datetime.datetime(1000, 1, 1)
old_date = datetime.datetime(1000, 1, 1)
t_date = datetime.datetime(1200, 12, 30)

def is_palindrome(d):
    """ Checks if the date is a Palindrome day """

    f = False
    year = d.strftime("%Y")
    mount = d.strftime("%m")
    day = d.strftime("%d")
    #print(year, mount, day)

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
    print(y2-y1, "years after.\n")


def duration(old_d, d):
    """ go throughout all days """

    max_y = datetime.MAXYEAR
    min_y = datetime.MINYEAR
    td = datetime.timedelta(1)

    while d < t_date:
        if is_palindrome(d):
            print(d.date())
            diff_years(old_d, d)
            old_d = d

        d += td


duration(t_date, date)
