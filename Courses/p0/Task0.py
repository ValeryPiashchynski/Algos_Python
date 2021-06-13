"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    txt = list(texts[0])
    print(f"First record of texts, {str(txt[0])} texts {str(txt[1])} at time {str(txt[2])}")

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    ll = list(calls)
    # get the last item based on the calls len
    last = ll[len(txt) - 1]
    print(f"Last record of calls, {str(last[0])} calls {str(last[1])} at time {str(last[2])}")
"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""
