x = 1234
print(x)
print(bin(x))
print(oct(x))
print(hex(x))

print('{:b}'.format(x))
print('{:o}'.format(x))
print('{:x}'.format(x))

x = -1234
print('{:b}'.format(2**32 + x))  # shows unsigned representation
print('{:x}'.format(2**32 + x))

print(int('4d2', 16))
print(int('10011010010', 2))
