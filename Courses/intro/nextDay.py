monthM = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}


def monthMap(month):
    return monthM[month]


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


def isLeapYear(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def testIsLeap():
    assert (isLeapYear(1992) is True)
    assert (isLeapYear(2000) is True)
    assert (isLeapYear(1900) is False)


def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar, and the first date is not after
       the second."""

    # assert (dateIsBefore(year1, month1, day1, year2, month2, day2) is True)

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


def testDaysBetweenDates():
    # test same day
    assert (daysBetweenDates(2017, 12, 30,
                             2017, 12, 30) == 0)
    # test adjacent days
    assert (daysBetweenDates(2017, 12, 30,
                             2017, 12, 31) == 1)
    # test new year
    assert (daysBetweenDates(2017, 12, 30,
                             2018, 1, 1) == 2)
    # test full year difference
    assert (daysBetweenDates(2012, 6, 29,
                             2013, 6, 29) == 365)

    print("Congratulations! Your daysBetweenDates")
    print("function is working correctly!")


testIsLeap()
testDaysBetweenDates()
