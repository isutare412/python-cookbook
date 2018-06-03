import numpy as np
import numpy.linalg

m = np.matrix([
    [1, -2, 3],
    [0, 4, 5],
    [7, 8, -9],
])

print(m)
print(m.T)  # traspose
print(m.I)  # inverse

# create a vector and multiply
v = np.matrix([
    [2],
    [3],
    [4],
])
print(m * v)

print(numpy.linalg.det(m))  # determinant
print(numpy.linalg.eigvals(m))  # eigenvalues

# solve x for mx = v
x = numpy.linalg.solve(m, v)
print(x)
