import re
from collections import namedtuple

text = 'foo = 23 + 42 * 10'

# (?P<name>) named capture group
NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
TIMES = r'(?P<TIMES>\*)'
EQ = r'(?P<EQ>=)'
WS = r'(?P<WS>\s+)'

master_pat = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))
Token = namedtuple('Token', ['type', 'value'])


def generate_tokens(pat, text):
    scanner = pat.scanner(text)
    for m in iter(scanner.match, None):
        yield Token(m.lastgroup, m.group())


for tok in generate_tokens(master_pat, text):
    print(tok)
print()

without_ws = (
    tok
    for tok
    in generate_tokens(master_pat, text)
    if tok.type != 'WS'
)

for tok in without_ws:
    print(tok)
print()

LT = r'(?P<LT><'
LE = r'(?P<LE><='
GT = r'(?P<GT>>'

# regex matches in order specified...!
# master_pat = re.compile('|'.join([LT, LE, GT]))  # Incorrect
master_pat = re.compile('|'.join([LE, LT, GT]))  # Correct
