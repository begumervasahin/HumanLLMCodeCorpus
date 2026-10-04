import os
def fonk1(file_path):
    print(f'Reading {file_path}....')
    with open(file_path, 'r') as file:
        b1 = file.read().split('\n')
    if b1:
        del b1[0]
        if b1:
            del b1[-1]
    if b1:
        print(b1[0])
    return b1
def fonk2(file_path, data):
    with open(file_path, 'w') as file:
        for line in data:
            b2 = '\t'.join(line)
            file.write(b2 + '\r')
def fonk3(path, b3 = ""):
    directory, b4 = os.path.split(path)
    b5 = b3 + b4
    return os.path.join(directory, b5)
def fonk4(b1):
    b6 = [line.split('\t') for line in b1]
    b7 = len(b6[0])
    b8 = [[] for _ in range(b7)]
    for line in b6:
        for i in range(b7):
            b8[i].append(float(line[i]))
    return b8
def fonk5(b8):
    b9 = len(b8[0])
    b1 = [[''] * len(b8) for _ in range(b9)]
    for point in range(b9):
        for trace_index, trace in enumerate(b8):
            b1[point][trace_index] = str(trace[point])
    return ['\t'.join(line) for line in b1]
