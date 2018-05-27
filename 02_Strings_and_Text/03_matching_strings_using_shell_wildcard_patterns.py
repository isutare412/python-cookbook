from fnmatch import fnmatch

print(fnmatch('foo.txt', '*.txt'))
print(fnmatch('foo.txt', '?oo.txt'))
print(fnmatch('Dat45.csv', 'Dat[0-9]*'))

# for more complex searching using shell wildcard patterns use 'glob' module
