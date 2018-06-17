from itertools import permutations, combinations

items = ['a', 'b', 'c']
for p in permutations(items):
    print(p)
print()

for p in permutations(items, 2):
    print(p)
print()

for p in combinations(items, 2):
    print(p)
print()
