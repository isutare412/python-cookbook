import heapq

a = [1, 4, 7, 10]
b = [2, 5, 6, 11]

# a, b must be sorted before merge()
# better than "sorted(itertools.chain(*iterables))" in memory usage
for c in heapq.merge(a, b):
    print(c)
