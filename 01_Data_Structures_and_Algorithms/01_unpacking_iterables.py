'''unpacking iterables'''

data = ['ACME', 50, 91.1, (2012, 12, 21)]

name, shares, price, (year, month, day) = data
print(name)
print(shares)
print(price)
print(year)
print(month)
print(day)

'''strings are also unpackable'''

s = 'Hello'

a, b, c, d, e = s
print(a, b, c, d, e)

'''unpacking iterables of arbitrary length'''

record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')

name, mail, *phone_numbers = record
print(name)
print(mail)
print(phone_numbers)

'''throwaway variable'''

name, *_, (year, *_) = data

print(name)
print(year)
