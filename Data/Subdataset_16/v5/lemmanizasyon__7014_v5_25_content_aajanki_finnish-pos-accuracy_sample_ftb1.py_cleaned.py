import hashlib
import re
def fonk1():
    b1 = 'data/test/ftb1/ftb1u.tsv'
    b2 = 'data/test/ftb1/ftb1u_sample.tsv'
    with open(b1) as file:
        b3 = file.readlines()
        b4 = list(fonk2(b3))
    b5 = fonk3(b4)
    print(f'Sampled {len(b5)} out of {len(b4)} b4')
    fonk4(b2, b5)
    print(f'Wrote samples to {b2}')
def fonk2(b3):
    b6 = re.compile(r'^')
    b7 = []
    for line in b3:
        if b6.match(line):
            if b7:
                yield ''.join(b7)
                b7 = []
        if line.strip():
            b7.append(line)
    if b7:
        yield ''.join(b7)
def fonk3(b4):
    b8 = []
    for b7 in b4:
        b9 = hashlib.sha256(b7.encode('utf-8')).hexdigest()
        if b9.startswith('0'):
            b8.append(b7)
    return b8
def fonk4(b2, b5):
    with open(b2, 'w') as file:
        file.write('\n'.join(b5))
if b10 = = '__main__':
    fonk1()