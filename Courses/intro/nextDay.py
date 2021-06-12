def nextDay(year, month, day):
    """
    Returns the year, month, day of the next day.
    Simple version: assume every month has 30 days.
    """

    # if day >= than 30, we reset day and increase month number
    if day >= 30:
        day = 1
        month += 1
    else:
        day += 1

    # we may have a case, that after increasing month, we would have month number 13
    # which means, that we should add 1 to a year and reset a month to 1
    if month > 12:
        year += 1
        month = 1

    return year, month, day


def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar, and the first date is not after
       the second."""

    assert (dateIsBefore(year1, month1, day1, year2, month2, day2) is False)

    num = 0
    if year1 == year2 and month1 == month2 and day1 == day2:
        return 0

    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        num += 1

    return num


def dateIsBefore(year1, month1, day1, year2, month2, day2):
    if year1 < year2:
        return True

    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            if day1 < day2:
                return True
    return False


def test():
    # assert (nextDay(1999, 12, 30) == (2000, 1, 1))
    # assert (nextDay(2013, 1, 30) == (2013, 2, 1))
    # assert (nextDay(2012, 1, 1) == (2012, 1, 2))

    test_cases = [((2012, 9, 30, 2012, 10, 30), 30),
                  ((2012, 1, 1, 2013, 1, 1), 360),
                  ((2012, 9, 1, 2012, 9, 4), 3)]

    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print("Test with data:", args, "failed")
        else:
            print("Test case passed!")


test()

### For example:
###    nextDay(1999, 12, 30) => (2000, 1, 1)
###    nextDay(2013, 1, 30) => (2013, 2, 1)
###    nextDay(2012, 12, 30) => (2013, 1, 1)  (even though December really has 31 days)
###
