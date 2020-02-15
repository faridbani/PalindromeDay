""" All Palindrome days between tow dates """
import datetime


# Help function to calculate how many years have gone between tow palindrome days
def diff_years(date1, date2):
    """ Calculate the diff between the years"""

    # Convert the years data in to a digit
    y1 = int(date1.strftime("%Y"))
    y2 = int(date2.strftime("%Y"))
    # Put the difference to String s and return it
    s = "After " + str(y2-y1) + " years:"
    return s


# Help function to check if a date is a palindrome day
def is_palindrome(d):
    """ Checks if the date is a Palindrome day """

    f = False
    # Distract the date (year - mount - day from d (datetime)
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


class Logic:
    def __init__(self, d, m_d):
        # initializing the instance variables
        self.date = datetime.datetime(d, 1, 1)
        self.max_date = datetime.datetime(m_d, 12, 31)
        self.result = []

    def run(self):
        """ go throughout all days """

        # set the date and old date to the given date to begin with
        old_date = self.date
        date = self.date
        # set td to one day timedelta
        td = datetime.timedelta(1)

        # Go through all days to find a Palindrome day, put it in result[] and return result[]
        while date < self.max_date:
            if is_palindrome(date):
                dif = diff_years(old_date, date)
                s = str(dif) + "\n" + date.strftime("%Y%m%d")
                self.result.append(s)

                old_date = date
            # increase the date with one day
            date += td
        return self.result


