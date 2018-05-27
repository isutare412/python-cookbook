from collections import defaultdict

pairs = {
    'a': [1, 2],
    'b': [3],
    'c': [4, 5, 6],
}

d = {}
for key, value in pairs.items():
    if key not in d:
        d[key] = []
    d[key] += value

d = defaultdict(list)  # better at initialization
for key, value in pairs.items():
    d[key] += value

print(d)
