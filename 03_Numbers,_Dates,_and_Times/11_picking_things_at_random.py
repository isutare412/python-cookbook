import random

values = [1, 2, 3, 4, 5, 6]

for i in range(6):
    print(random.choice(values))
print()

print(random.sample(values, 2))
print()

random.shuffle(values)
print(values)
print()

print(random.randint(1, 6))
print(random.random())
print(random.getrandbits(32))
