import re

text = 'yeah, but no, but yeah, but no, but yeah'

# exact match
print(text == 'yeah')

# match at start or end
print(text.startswith('yeah'))
print(text.endswith('no'))

# search for the location of the first occurrence
print(text.find('no'))


# regex for complex pattern matching
text1 = '11/27/2012'
text2 = 'Nov 27, 2012'

print(bool(re.match(r'\d+/\d+/\d+', text1)))
print(bool(re.match(r'\d+/\d+/\d+', text2)))

# if you need to perform a lot of matches with same regex pattern,
# precompile it!
datepat = re.compile(r'\d+/\d+/\d+')
print(bool(datepat.match(text1)))
print(bool(datepat.match(text2)))

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
print(datepat.findall(text))

# capture group
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
fresult = datepat.findall(text)
print(fresult)

for found in datepat.finditer(text):
    month, day, year = found.groups()
    print('{}-{}-{}'.format(year, month, day))
