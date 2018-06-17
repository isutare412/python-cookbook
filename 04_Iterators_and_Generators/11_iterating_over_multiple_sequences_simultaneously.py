from itertools import zip_longest

xpts = [1, 5, 4, 2, 10, 7]
ypts = [101, 78, 37, 15, 62, 99]
for x, y in zip(xpts, ypts):
    print(x, y)
print()

# zip() stops iterating whenever on of the input sequences is exhausted
zpts = [1, 2, 3]
for y, z in zip(ypts, zpts):
    print(y, z)
print()

for y, z in zip_longest(ypts, zpts):
    print(y, z)
print()

headers = ['name', 'shares', 'price']
values = ['ACME', 100, 490.1]
print(dict(zip(headers, values)))
