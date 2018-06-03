import cmath

a = complex(2, 4)
b = 3 - 5j

print(a, a.real, a.imag)
print(b, b.real, b.imag)
print(a.conjugate())

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(abs(a))

print(cmath.sin(a))
print(cmath.cos(a))
print(cmath.exp(a))

# print(math.sqrt(-1))  # ERROR
print(cmath.sqrt(-1))
