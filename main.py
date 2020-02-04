# PalindromeDay sense 0000 00 00
global data
global old_date

date = [0, 0, 0, 0, 0, 0, 0, 0]
old_date = [0, 0, 0, 0, 0, 0, 0, 0]


def is_palindrome(d):
    """ Checks if the date is a Palindrome day """
    f = False
    d_l = len(d) - 1
    if d_l != 7:
        return f
    print(d_l)
    for i in range(len(d)):
        if d[i] == d[d_l-i]:
            f = True
        else:
            f = False

    return f


test = is_palindrome([2, 0, 2, 0, 0, 2, 0, 2])


print(test)

'''def diff_years(date1, date2):
    """ Calculate the diff between the years"""
    pass


def during(old_da, d):
    """ go throughout all days """
    pass


def go_throu():
    pass
'''

