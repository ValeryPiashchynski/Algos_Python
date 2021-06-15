"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""


def IsBangalore(c):
    return c[0][0:5] == '(080)'


# according to a task, we have 3 cases:
"""
Fixed lines start with an area code enclosed in brackets. The area codes vary in length but always begin with 0. Example: "(022)40840621".
Mobile numbers have no parentheses, but have a space in the middle of the number to help readability. The mobile code of a mobile number is its first four digits and they always start with 7, 8 or 9. Example: "93412 66159".
Telemarketers' numbers have no parentheses or space, but start with the code 140. Example: "1402316533".
"""


def areaCode(call):
    other = call[1]
    # input ['(080)45291968', '90365 06212', '01-09-2016 06:30:36', '9'] (sample)
    # fixed
    if other[:2] == '(0':
        return other.split(sep=')')[0] + ')'
    # telemarketers
    if other[:3] == '140':
        return other[:3]
    # mobile phone
    else:
        return other[:4]


def solve():
    bangalore_prefix = []
    # Part A
    for call in calls:
        # ['78130 00821', '98453 94494', '01-09-2016 06:01:12', '186'] call
        # check if it from Bangalore
        if IsBangalore(call):
            # if it is, append to the bangalore prefixes extracting area code
            bangalore_prefix.append(areaCode(call))

    b_prefix = list(set(bangalore_prefix))
    b_prefix.sort()

    print("\n The numbers called by people in Bangalore have codes:")
    for b in b_prefix:
        print(b)

    # Part B
    same_country = 0
    for call_prefix in bangalore_prefix:
        if call_prefix == "(080)":
            same_country += 1

    # calculate percentage
    print("\n {} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(round(same_country / len(bangalore_prefix) * 100, 2)))


solve()
