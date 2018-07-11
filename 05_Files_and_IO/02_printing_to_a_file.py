import os

RELATIVE_PATH = 'samples/somefile.txt'

file_dir = os.path.dirname(os.path.realpath(__file__))
file_path = os.path.join(file_dir, RELATIVE_PATH)

with open(file_path, 'wt') as f:
    print('Hello World!', file=f)
