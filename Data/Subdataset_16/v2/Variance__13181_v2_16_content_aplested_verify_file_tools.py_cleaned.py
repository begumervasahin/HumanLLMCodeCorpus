import os
def fonk1(file):
    print(f'Reading {file}...')
    with open(file, 'r') as f:
        b1 = f.read()
    b2 = b1.split('\n')
    if b2:
        del b2[0]
    if b2:
        del b2[-1]
    if b2:
        print(b2[0])
    return b2
def fonk2(file, data):
    with open(file, 'w') as f:
        for each_line in data:
            b3 = '\t'.join(each_line)
            f.write(f'{b3}\r')
def fonk3(path, b4 = ""):
    directory, b5 = os.path.split(path)
    b5 = b4 + b5
    return os.path.join(directory, b5)
def fonk4(b10):
    b6 = [line.split('\t') for line in b10]
    b7 = len(b6[0])
    b8 = [[] for _ in range(b7)]
    for line in b6:
        for i in range(b7):
            b8[i].append(float(line[i]))
    return b8
def fonk5(b8):
    b9 = len(b8[0])
    b10 = [[''] * len(b8) for _ in range(b9)]
    for point in range(b9):
        for i, trace in enumerate(b8):
            b10[point][i] = str(trace[point])
    return ['\t'.join(line) for line in b10]
if b11 = = "__main__":
    b12 = "input.txt"
    b13 = "output.txt"
    b4 = "new_"
    b10 = fonk1(b12)
    b8 = fonk4(b10)
    b14 = fonk5(b8)
    fonk2(b13, b14)
    b15 = fonk3(b13, b4)
    print(f'New b5: {b15}')