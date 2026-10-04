import hashlib
def fonk1():
    b1 = 'data/test/ftb1/ftb1u.tsv'
    b2 = 'data/test/ftb1/ftb1u_sample.tsv'
    b3 = fonk2(b1)
    b3 = fonk3(b3)
    b4 = fonk4(b3)
    print(f'Sampled {len(b4)} out of {len(b3)} b3')
    fonk5(b2, b4)
    print(f'Wrote samples to {b2}')
def fonk2(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()
def fonk3(lines):
    b3 = []
    b5 = []
    for line in lines:
        b6 = line.strip()
        if not b6 and b5:
            b3.append(' '.join(b5).strip())
            b5 = []
        else:
            b5.append(line.strip())
    if b5:
        b3.append(' '.join(b5).strip())
    return b3
def fonk4(b3):
    b7 = []
    for sentence in b3:
        b8 = hashlib.sha256(sentence.encode('utf-8')).hexdigest()
        if b8.startswith('0'):
            b7.append(sentence)
    return b7
def fonk5(file_path, b3):
    with open(file_path, 'w') as file:
        file.write('\n'.join(b3) + '\n')
if b9 = = '__main__':
    fonk1()