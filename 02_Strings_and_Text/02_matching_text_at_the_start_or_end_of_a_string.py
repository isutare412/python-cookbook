import os

filename = 'spam.txt'

print(filename.endswith('.txt'))
print(filename.startswith('http:'))


filenames = os.listdir('.')
print([f for f in filenames if f.endswith('.py')])
