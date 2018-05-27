record = '....................100          .......513.25     ..........'

# bad example
cost = int(record[20:32]) * float(record[40:48])

# good example
SHARES = slice(20, 32)
PRICE = slice(40, 48)

cost = int(record[SHARES]) * float(record[PRICE])
print(cost)


s = 'HelloWorld'
a = slice(5, 100, 2)

print(a.indices(len(s)))

for i in range(*a.indices(len(s))):
    print(s[i], end=' ')
