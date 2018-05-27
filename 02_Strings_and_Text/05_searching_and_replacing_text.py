import re
from calendar import month_abbr

# simple replace
text = 'yeah, but no, but yeah, but no, but yeah'
print(text.replace('yeah', 'yep'))

# more complicated substitution
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
print(re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text))

# precompile pattern for repeatative use
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
print(datepat.sub(r'\3-\1-\2', text))


# you can use a substitution callback function
def reinterpret_date(matchobj):
    mon_name = month_abbr[int(matchobj.group(1))]
    return '{} {}, {}'.format(matchobj.group(2), mon_name, matchobj.group(3))


print(datepat.sub(reinterpret_date, text))

# show how many substitutions were made
newtext, n = datepat.subn(r'\3-\1-\2', text)
print(newtext, n)
