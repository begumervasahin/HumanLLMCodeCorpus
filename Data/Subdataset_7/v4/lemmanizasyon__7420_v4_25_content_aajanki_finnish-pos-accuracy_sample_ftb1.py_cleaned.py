import hashlib
import re
def fonk1():
    b1 = 'data/test/ftb1/ftb1u.tsv'
    b2 = 'data/test/ftb1/ftb1u_sample.tsv'
    with open(b1) as file:
        b3 = file.readlines()
        b4 = list(fonk2(b3))
    b5 = []
    for b8 in b4:
        b6 = hashlib.sha256(b8.encode('utf-8')).hexdigest()
        if b6.startswith('0'):
            b5.append(b8)
    print(f'Sampled {len(b5)} out of {len(b4)} b4')
    with open(b2, 'w') as file:
        file.write('\n'.join(b5))
    print(f'Wrote samples to {b2}')
def fonk2(b3):
    b7 = re.compile(r'^')
    b8 = []
    for line in b3:
        if b7.match(line):
            if b8:
                yield ''.join(b8)
                b8 = []
        if line.strip():
            b8.append(line)
    if b8:
        yield ''.join(b8)
if b9 = = '__main__':
    fonk1()