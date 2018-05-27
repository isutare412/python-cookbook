import re

line = 'asdf fjdk; afed, fjek,asdf, foo'

splitted = re.split(r'[;,\s]+', line)
print(splitted)

splitted = re.split(r'([;,\s]+)', line)
print(splitted)

contents = splitted[::2]
delimiters = splitted[1::2] + ['']

restored = ''.join(x + y for x, y in zip(contents, delimiters))
print(restored)
