import unicodedata

s1 = 'Spicy Jalape\u00f1o'
s2 = 'Spicy Jalapen\u0303o'

print(s1)
print(s2)
print(s1 == s2)

# NFC normalization ('C'omposed)
t1 = unicodedata.normalize('NFC', s1)
t2 = unicodedata.normalize('NFC', s2)

print(ascii(t1))
print(ascii(t2))
print(t1 == t2)

# NFC normalization ('D'ecomposed)
t1 = unicodedata.normalize('NFD', s1)
t2 = unicodedata.normalize('NFD', s2)

print(ascii(t1))
print(ascii(t2))
print(t1 == t2)

# NFKC, NFKD normalization
s3 = '\ufb01'

print(s3)
print(unicodedata.normalize('NFC', s3))
print(unicodedata.normalize('NFD', s3))
print(unicodedata.normalize('NFKC', s3))
print(unicodedata.normalize('NFKD', s3))

# removing diacritical marks
t1 = unicodedata.normalize('NFD', s1)
print(''.join(c for c in t1 if not unicodedata.combining(c)))
