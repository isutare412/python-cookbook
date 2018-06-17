CHUNK_SIZE = 128

'''
with open('/etc/passwd') as f:
    while True:
        chunk = f.read(CHUNK_SIZE)
        if chunk == '':
            break
        print(chunk, end='')
'''

with open('/etc/passwd') as f:
    for chunk in iter(lambda: f.read(CHUNK_SIZE), ''):
        print(chunk, end='')
