parts = ['Is', 'Chicago', 'Not', 'Chicago?']
print(' '.join(parts))
print(''.join(parts))

a = 'Is Chicago'
b = 'Not Chicago?'
print(a + ' ' + b)
print('{} {}'.format(a, b))

c = 'Hello' 'World'
d = (
    'Hello'
    'World'
)
print(c, d)


def sample():
    yield 'Is'
    yield 'Chicago'
    yield 'Not'
    yield 'Chicago?'


print(''.join(sample()))


def combine(source, maxsize):
    parts = []
    size = 0
    for part in source:
        parts.append(part)
        size += len(part)
        if size > maxsize:
            yield ''.join(parts)
            parts = []
            size = 0
    yield ''.join(parts)


for part in combine(sample(), 32768):
    # f.write(part)
    # write I/O with maxsize
    print(part)
