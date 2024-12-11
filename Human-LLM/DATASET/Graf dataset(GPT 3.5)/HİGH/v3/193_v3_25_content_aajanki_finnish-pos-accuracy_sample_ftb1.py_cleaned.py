import hashlib
import re
def fonk1():
    b1 = 'data/test/ftb1/ftb1u.tsv'
    b2 = 'data/test/ftb1/ftb1u_sample.tsv'
    with open(b1) as file:
        b3 = list(fonk2(file.readlines()))
    b4 = fonk3(b3)
    fonk4(len(b4), len(b3))
    fonk5(b2, b4)
    print(f'Wrote samples to {b2}')
def fonk2(lines):
    b5 = re.compile(r'^')
    b6 = []
    for line in lines:
        if b5.match(line):
            if b6:
                yield ''.join(b6)
                b6 = []
        if line.strip():
            b6.append(line)
    if b6:
        yield ''.join(b6)
def fonk3(b3):
    b7 = []
    for b6 in b3:
        b8 = hashlib.sha256(b6.encode('utf-8')).hexdigest()
        if b8.startswith('0'):
            b7.append(b6)
    return b7
def fonk4(selected_count, total_count):
    print(f'Sampled {selected_count} out of {total_count} b3')
def fonk5(file_path, b3):
    with open(file_path, 'w') as file:
        file.write('\n'.join(b3))
if b9 = = '__main__':
    fonk1()