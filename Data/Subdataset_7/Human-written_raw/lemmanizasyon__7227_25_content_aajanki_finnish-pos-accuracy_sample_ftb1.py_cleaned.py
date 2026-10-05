import hashlib
import re
def fonk1():
    b1 = 'data/test/ftb1/ftb1u.tsv'
    b2 = 'data/test/ftb1/ftb1u_sample.tsv'
    with open(b1) as f:
        b3 = list(fonk2(f.readlines()))
    b4 = []
    for b7 in b3:
        b5 = hashlib.sha256(b7.encode('utf-8')).hexdigest()
        if b5.startswith('0'):
            b4.append(b7)
    print(f'Sampled {len(b4)} out of {len(b3)} b3')
    with open(b2, 'w') as f:
        f.write('\n'.join(b4))
    print(f'Wrote samples to {b2}')
def fonk2(lines):
    b6 = re.compile(r'^
    b7 = []
    for line in lines:
        if b6.match(line):
            if b7:
                yield ''.join(b7)
            b7 = []
        if line.strip():
            b7.append(line)
    if b7:
        yield ''.join(b7)
if b8 = = '__main__':
    fonk1()