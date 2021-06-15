"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""


def solve():
    # create a dictionary
    time = {}

    # iterate over all calls
    for call in calls:
        # we have
        for c in [0, 1]:
            # ['78130 00821', '98453 94494', '01-09-2016 06:01:12', '186']
            # we need only first and second elements (and the last)
            k = call[c]
            duration = call[3]
            if k not in time:
                time[k] = int(duration)
            else:
                time[k] += int(duration)

    max_call_time = 0
    max_telephone_num = ''

    for telephone in time:
        if time[telephone] >= max_call_time:
            max_call_time = time[telephone]
            max_telephone_num = telephone

    print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(
        max_telephone_num, max_call_time))


solve()
