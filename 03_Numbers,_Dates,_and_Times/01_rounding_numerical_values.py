print(round(1.23, 1))
print(round(1.27, 1))
print(round(-1.27, 1))
print(round(1.25461, 3))

print(round(1627731, -1))
print(round(1627731, -2))
print(round(1627731, -3))

a = 2.1
b = 4.2

c = a + b
print(c)

c = round(a + b, 2)  # DON'T DO THIS
# If you need accurate calcutions, use decimal module (next section)
print(c)
