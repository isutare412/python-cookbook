from collections import Counter

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under',
]

word_counts = Counter(words)

print(word_counts.most_common(3))
print('around: {}'.format(word_counts['around']))


morewords = ['why', 'are', 'you', 'not', 'looking', 'in', 'my', 'eyes']

word_counts.update(morewords)
# for word in morewords:
#     word_counts[word] += 1

print(word_counts)


a = Counter(words)
b = Counter(morewords)

print(a + b)
print(a - b)
