text = 'Hello world'

print(text.ljust(20))
print(text.rjust(20))
print(text.center(20))

print(text.ljust(20, '*'))
print(text.rjust(20, '='))
print(text.center(20, '-'))

print('{:<20}'.format(text))
print('{:>20}'.format(text))
print('{:^20}'.format(text))

print('{:*<20}'.format(text))
print('{:=>20}'.format(text))
print('{:-^20}'.format(text))

print('{:>10}{:>10}'.format('Hello', 'world'))

x = 1.2345
print('{:20.3f}'.format(x))
