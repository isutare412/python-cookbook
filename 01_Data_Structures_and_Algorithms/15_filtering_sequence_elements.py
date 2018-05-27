from itertools import compress


def isint(val) -> bool:
    try:
        int(val)
        return True
    except ValueError:
        return False


'''
basic filtering
'''

mylist = [1, 4, -5, 10, -7, 2, 3, -1]

sortedlist = [n for n in mylist if n > 0]
print(sortedlist)

# if memory is a concern, you can use generator expression
positive = (n for n in mylist if n > 0)
print(positive)
for n in positive:
    print(n, end=' ')
print()

'''
filter using built-in filter function
'''

values = ['1', '2', '-3', '-', '4', 'N/A', '5']

ivals = list(filter(isint, values))
print(ivals)

'''
filter without discard
'''

clip_neg = [n if n > 0 else 0 for n in mylist]
print(clip_neg)

'''
filtering with built-in compress function
'''

addresses = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK'
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE',
]

contents = [0, 3, 10, 4, 1, 7, 6, 1]

more5 = [n > 5 for n in contents]
print(list(compress(addresses, more5)))
