import hashlib
import re
def fonk1():
    b1 = 'data/test/ftb1/ftb1u.tsv'
    b2 = 'data/test/ftb1/ftb1u_sample.tsv'
    b3 = fonk2(b1)
    b4 = fonk4(b3)
    print(f'Sampled {len(b4)} out of {len(b3)} b3')
    fonk5(b2, b4)
    print(f'Wrote samples to {b2}')
def fonk2(b1):
    with open(b1, 'r') as file:
        b5 = file.readlines()
    return list(fonk3(b5))
def fonk3(b5):
    b6 = []
    for line in b5:
        if not line.strip() and b6:
            yield ''.join(b6).strip()
            b6 = []
        else:
            b6.append(line)
    if b6:
        yield ''.join(b6).strip()
def fonk4(b3):
    b7 = []
    for b6 in b3:
        b8 = hashlib.sha256(b6.encode('utf-8')).hexdigest()
        if b8.startswith('0'):
            b7.append(b6)
    return b7
def fonk5(b2, b3):
    with open(b2, 'w') as file:
        for b6 in b3:
            file.write(f"{b6}\n")
if b9 = = '__main__':
    fonk1()