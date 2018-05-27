import re

s = '   hello world  \n'
print(s.strip())
print(s.lstrip())
print(s.rstrip())

t = '-----hello world====='
print(t.lstrip('-'))
print(t.rstrip('='))
print(t.strip('-='))

u = '    hello     world       '
print(u.strip())  # not what i wanted...
print(re.sub('\s+', ' ', u.strip()))
print(' '.join(u.split()))
