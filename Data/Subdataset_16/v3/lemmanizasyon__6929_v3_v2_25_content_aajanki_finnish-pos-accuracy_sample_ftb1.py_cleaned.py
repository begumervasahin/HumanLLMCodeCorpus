import hashlib
import re
def fonk1():
    b1 = 'data/test/ftb1/ftb1u.tsv'
    b2 = 'data/test/ftb1/ftb1u_sample.tsv'
    b3 = fonk2(b1)
    b4 = fonk5(b3)
    print(f'Sampled {len(b4)} out of {len(b3)} b3')
    fonk6(b2, b4)
    print(f'Wrote samples to {b2}')
def fonk2(file_path):
    with open(file_path, 'r') as file:
        b5 = file.readlines()
    return list(fonk3(b5))
def fonk3(b5):
    b6 = []
    b7 = re.compile(r'^')
    for line in b5:
        if b7.match(line):
            if b6:
                yield ''.join(b6)
                b6 = []
        if line.strip():
            b6.append(line)
    if b6:
        yield ''.join(b6)
def fonk4(b6):
    b8 = hashlib.sha256(b6.encode('utf-8')).hexdigest()
    return b8.startswith('0')
def fonk5(b3):
    return [b6 for b6 in b3 if fonk4(b6)]
def fonk6(file_path, b3):
    with open(file_path, 'w') as file:
        file.write('\n'.join(b3))
if b9 = = '__main__':
    fonk1()