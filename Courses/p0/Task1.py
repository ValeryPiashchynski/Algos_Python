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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""


def create_set(file: list, numbers: set) -> set:
    for column in [0, 1]:
        temp_numbers = [data[column] for data in file]
        numbers.update(temp_numbers)
    return numbers


def task():
    tel_numbers = set()

    tel_numbers = create_set(calls, tel_numbers)
    tel_numbers = create_set(texts, tel_numbers)
    print("There are {} different telephone numbers in the records.".format(len(tel_numbers)))


task()
