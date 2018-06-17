import os
from itertools import dropwhile, islice

RELATIVE_PATH = 'inputs/test.txt'

file_dir = os.path.dirname(os.path.realpath(__file__))
file_path = os.path.join(file_dir, RELATIVE_PATH)

with open(file_path) as f:
    for line in dropwhile(lambda line: line.strip().isdigit(), f):
        print(line, end='')
    print('\n')

with open(file_path) as f:
    for line in islice(f, 18, None):
        print(line, end='')
    print('\n')

with open(file_path) as f:
    lines = (line.strip() for line in f if line.strip().isalpha())
    for line in lines:
        print(line)
