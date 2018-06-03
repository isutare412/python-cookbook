import re

print('Hello World'.encode('ASCII'))

data = b'Hello World'
print(data)
print(data[0:5])
print(data.startswith(b'Hello'))
print(data.split())
data.replace(b'Hello', b'Hello Cruel')
print()

bdata = bytearray(data)
print(data[0:5])
print(data.startswith(b'Hello'))
print(data.split())
data.replace(b'Hello', b'Hello Cruel')

data = b'FOO:BAR,SPAM'
print(re.split(b'[:,]', data))  # pattern also needs to be specified as bytes
print()

a = 'Hello World'
b = b'Hello World'
print(a[0], a[1])
print(b[0], b[1])

print(b)
print(b.decode('ascii'))
