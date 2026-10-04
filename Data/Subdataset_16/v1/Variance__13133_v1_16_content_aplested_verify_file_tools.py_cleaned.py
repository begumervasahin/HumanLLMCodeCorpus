import os
def fonk1(file_path):
    print(f'Reading {file_path}....')
    with open(file_path, 'r') as f:
        b1 = f.read().split('\n')
    if b1:
        del b1[0]
        if b1:
            del b1[-1]
    if b1:
        print(b1[0])
    return b1
def fonk2(file_path, data):
    with open(file_path, 'w') as f:
        for each_line in data:
            b2 = '\t'.join(each_line)
            f.write(b2 + '\r')
def fonk3(path, b3 = ""):
    directory, b4 = os.path.split(path)
    b4 = b3 + b4
    return os.path.join(directory, b4)
def fonk4(b1):
    b5 = [line.split('\t') for line in b1]
    b6 = len(b5[0])
    b7 = [[] for _ in range(b6)]
    for line in b5:
        for i in range(b6):
            b7[i].append(float(line[i]))
    return b7
def fonk5(b7):
    b8 = len(b7[0])
    b1 = [[''] * len(b7) for _ in range(b8)]
    for point in range(b8):
        for trace_index, trace in enumerate(b7):
            b1[point][trace_index] = str(trace[point])
    return b1