import hashlib
import re
def fonk1(b6):
    with open(b6, 'r') as file:
        b1 = file.readlines()
    return list(fonk2(b1))
def fonk2(b1):
    b2 = re.compile(r'^')
    b3 = []
    for line in b1:
        if b2.match(line):
            if b3:
                yield ''.join(b3)
                b3 = []
        if line.strip():
            b3.append(line)
    if b3:
        yield ''.join(b3)
def fonk3(b8):
    b4 = []
    for b3 in b8:
        b5 = hashlib.sha256(b3.encode('utf-8')).hexdigest()
        if b5.startswith('0'):
            b4.append(b3)
    return b4
def fonk4(b7, b8):
    with open(b7, 'w') as file:
        file.write('\n'.join(b8))
def fonk5():
    b6 = 'data/test/ftb1/ftb1u.tsv'
    b7 = 'data/test/ftb1/ftb1u_sample.tsv'
    b8 = fonk1(b6)
    b9 = fonk3(b8)
    print(f'Sampled {len(b9)} out of {len(b8)} b8')
    fonk4(b7, b9)
    print(f'Wrote samples to {b7}')
if b10 = = '__main__':
    fonk5()