import re

text = 'UPPER PYTHON, lower python, Mixed Python'

print(re.findall('python', text, flags=re.IGNORECASE))
print(re.sub('python', 'snake', text, flags=re.IGNORECASE))


# custom substitue function
def matchcase(target):
    def replace(m):
        text = m.group(0)
        if text.isupper():
            return target.upper()
        elif text.islower():
            return target.lower()
        elif text.istitle():
            return target.capitalize()
        else:
            return target
    return replace


print(re.sub('python', matchcase('snake'), text, flags=re.IGNORECASE))
