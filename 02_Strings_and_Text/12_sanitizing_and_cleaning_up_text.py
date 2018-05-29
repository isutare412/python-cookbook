import unicodedata
import sys

s = 'pýtĥöñ\fis\tawesome\r\n'

print(s)

# remove tabs and carriage return
remap = {
    ord('\f'): ' ',
    ord('\t'): ' ',
    ord('\r'): None,
}

a = s.translate(remap)
print(a)

# remove all combining characters
cmb_chrs = dict.fromkeys(
    (c for c in range(sys.maxunicode) if unicodedata.combining(chr(c))),
    None
)

b = unicodedata.normalize('NFD', a)
c = b.translate(cmb_chrs)
print(c)

c = b.encode('ascii', 'ignore').decode('ascii')
print(c)

# maps all Unicode decimal digits into ASCII digits
digitmap = {
    c: ord('0') + unicodedata.digit(chr(c))
    for c in range(sys.maxunicode) if unicodedata.category(chr(c)) == 'Nd'
}

print(len(digitmap))

x = '\u0661\u0662\u0663'
print(x.translate(digitmap))
