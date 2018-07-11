import os

RELATIVE_PATH = 'samples/existfile.txt'

file_dir = os.path.dirname(os.path.realpath(__file__))
file_path = os.path.join(file_dir, RELATIVE_PATH)

with open(file_path, 'wt') as f:
    f.write('Hello World!')

# Raise FileExistsError when the file exists
with open(file_path, 'xt') as f:
    f.write('Hello World!')
