import re

# '\d' also includes unicode digits
num = re.compile(r'\d+')
print(bool(num.match('123')))  # ASCII digits
print(bool(num.match('\u0661\u0662\u0663')))  # Arabic digits

# case folding
s = 'stra\u00dfe'

print(s)
print(s.upper())

pat = re.compile('stra\u00dfe', re.IGNORECASE)
print(bool(pat.match(s)))
print(bool(pat.match(s.upper())))

# re module cannot handle case folding...
# consider using the third-party regex library
