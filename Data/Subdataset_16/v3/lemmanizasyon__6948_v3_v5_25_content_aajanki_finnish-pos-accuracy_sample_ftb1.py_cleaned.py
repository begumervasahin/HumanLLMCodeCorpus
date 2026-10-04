import hashlib
import re
def fonk1():
    b1 = 'data/test/ftb1/ftb1u.tsv'
    b2 = 'data/test/ftb1/ftb1u_sample.tsv'
    b3 = fonk2(b1)
    b4 = fonk4(b3)
    fonk7(b4, b3)
    fonk6(b2, b4)
    print(f'Sentences written to {b2}')
def fonk2(file_path):
    with open(file_path, 'r') as file:
        b5 = file.readlines()
    return list(fonk3(b5))
def fonk3(b5):
    b6 = []
    for line in b5:
        if not line.strip() and b6:
            yield ''.join(b6).strip()
            b6 = []
        elif line.strip():
            b6.append(line)
    if b6:
        yield ''.join(b6).strip()
def fonk4(b3):
    return [b6 for b6 in b3 if fonk5(b6)]
def fonk5(b6):
    b7 = hashlib.sha256(b6.encode('utf-8')).hexdigest()
    return b7.startswith('0')
def fonk6(file_path, b3):
    with open(file_path, 'w') as file:
        file.write('\n'.join(b3))
def fonk7(b4, all_sentences):
    b8 = len(all_sentences)
    b9 = len(b4)
    print(f'Sampled {b9} out of {b8} b3')
if b10 = = '__main__':
    fonk1()