import re

findquote = re.compile(r'"(.*)"')

text1 = 'Computer says "no."'
print(findquote.findall(text1))

# * is too greedy...
text2 = 'Computer says "no." Phone says "yes."'
print(findquote.findall(text2))

# make non-greedy (*?, +?)
print(re.findall(r'"(.*?)"', text2))
