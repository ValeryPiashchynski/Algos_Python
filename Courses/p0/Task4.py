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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""


def solve():
    # we need to read all needed fields
    snd = set([data[0] for data in calls])
    rcv = set([data[1] for data in calls])
    m_snd = set([data[0] for data in texts])
    m_rcv = set([data[1] for data in texts])

    # create a array
    possible_tm = []

    # loop over call senders
    for call_sender in snd:
        if call_sender not in rcv and call_sender not in m_snd and call_sender not in m_rcv:
            possible_tm.append(call_sender)

    # sort because of task
    possible_tm.sort()

    print("\n These numbers could be telemarketers:")
    for tm in possible_tm:
        print(tm)


solve()
