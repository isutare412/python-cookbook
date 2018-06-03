import numpy as np

x = [1, 2, 3, 4]
y = [5, 6, 7, 8]

print(x * 2)  # not what i wanted...
print(x + y)  # not what i wanted too

ax = np.array([1, 2, 3, 4])
ay = np.array([5, 6, 7, 8])

print(ax * 2)
print(ax + 10)
print(ax + ay)


def f(x: "numpy.array") -> "numpy.array":
    return 3 * x**2 - 2 * x + 7


print(f(ax))
print(np.sqrt(ax))
print(np.cos(ax))

grid = np.zeros(shape=(1000, 1000), dtype=float)
print(grid)
grid += 10
print(grid)

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a)
print(a[1])  # row 1
print(a[:, 1])  # column 1

a[1:, 1:3] += 10
print(a)

print(np.where(a < 10, a, 10))
