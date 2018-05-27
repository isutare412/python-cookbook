from collections import ChainMap

a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}

c = ChainMap(a, b)
print(c)
print(c['x'])
print(c['y'])
print(c['z'])
print(len(c))
print(list(c.items()))

# ChainMap can only change the first dict
c['x'] = 10
print(a['x'])  # changed

# ChainMap cannot change all but the first dict
c['y'] = 20
print(b['y'])  # unchanged
