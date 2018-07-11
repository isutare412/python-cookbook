import os

RELATIVE_PATH = 'samples/somefile.bin'

file_dir = os.path.dirname(os.path.realpath(__file__))
file_path = os.path.join(file_dir, RELATIVE_PATH)

with open(file_path, 'wb') as f:
    # byte string
    f.write(b'Hello World\n')

with open(file_path, 'rb') as f:
    bindata = f.read()
    text = bindata.decode('utf-8')

for b, c in zip(bindata, text):
    print('{}({})'.format(repr(chr(b)), b), end=' ')
    print(repr(c))
