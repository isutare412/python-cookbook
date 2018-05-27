import re

commentpat = re.compile(r'/\*(.*?)\*/')

text = '''/* this is a
multiline comment */
'''

# regex '.' does not include '\n'
print(commentpat.findall(text))

# solution
# p.s. (?:) specifies non-capture group
commentpat = re.compile(r'/\*((?:.|\n)*?)\*/')
print(commentpat.findall(text))
