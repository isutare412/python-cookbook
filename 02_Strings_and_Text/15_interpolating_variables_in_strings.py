import sys

s = '{name} has {n} messages.'
print(s.format(name='Guido', n=37))

name = 'Guido'
n = 37
print(s.format_map(vars()))


class Info:
    def __init__(self, name, n):
        self.name = name
        self.n = n


a = Info('Guido', 37)
print(s.format_map(vars(a)))


class safesub(dict):
    def __missing__(self, key):
        return '{{{}}}'.format(key)  # double curly brace escapes


del n
# print(s.format_map(vars()))  # KeyError
print(s.format_map(safesub(vars())))


def sub(text):
    # sys._getframe(n) rewinds stack backward 'n' times
    return text.format_map(safesub(sys._getframe(1).f_locals))


name = 'Suhyuk'
n = 412
print(sub(s))

del name
print(sub(s))
