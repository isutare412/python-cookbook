import os

RELATIVE_PATH = 'samples/somefile.txt'

file_dir = os.path.dirname(os.path.realpath(__file__))
file_path = os.path.join(file_dir, RELATIVE_PATH)

with open(file_path, 'wt', encoding='utf-8') as f:
    f.write('test1\ntest2\ntest3\n')
    print('Spicy Jalape\u00f1o\n', file=f)

# '\r\n' is converted to a '\n' by default
# newline='' stops auto converting
with open(file_path, 'rt', encoding='utf-8', newline='') as f:
    # f.read()
    for line in f:
        print(repr(line), line, end='')
