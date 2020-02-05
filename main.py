""" Palindrome days sense 'date' / set it manual """
import datetime

# initializing the global variables
date = datetime.datetime(2020, 1, 1)
old_date = datetime.datetime(2020, 1, 1)
max_date = datetime.datetime(3020, 12, 30)


def is_palindrome(d):
    """ Checks if the date is a Palindrome day """

    f = False
    # Distract the date (year - mount - day)
    year = d.strftime("%Y")
    mount = d.strftime("%m")
    day = d.strftime("%d")
    # Check if it is a Palindrome day
    if (year[0] == day[1]) and \
        (year[1] == day[0]) and \
        (year[2] == mount[1]) and \
        (year[3] == mount[0]):
        f = True
    return f


def diff_years(date1, date2):
    """ Calculate the diff between the years"""

    # Convert the years data in to a digit
    y1 = int(date1.strftime("%Y"))
    y2 = int(date2.strftime("%Y"))
    # print the difference
    print("After ", y2-y1, " years:")


def duration(old_d, d):
    """ go throughout all days """

    # set td to one day timedelta
    td = datetime.timedelta(1)

    # Go through all days to find a Palindrome day and print it
    while d < max_date:
        if is_palindrome(d):
            diff_years(old_d, d)
            print(d.date(), "\n")
            old_d = d

        d += td


duration(old_date, date)
