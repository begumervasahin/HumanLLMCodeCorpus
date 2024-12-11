import sys
import os
def fonk1(file_path):
    print('Reading ' + file_path + '...')
    with open(file_path, 'r') as file:
        b1 = file.readlines()
    b1 = [line.strip() for line in b1]
    del b1[0]
    del b1[-1]
    print(b1[0])
    return b1
def fonk2(file_path, data):
    with open(file_path, "w") as file:
        for line in data:
            b2 = '\t'.join(line)
            file.write(b2 + '\n')
def fonk3(path, b3 = ""):
    directory, b4 = os.path.split(path)
    b4 = b3 + b4
    return os.path.join(directory, b4)
def fonk4(b1):
    b5 = [line.split('\t') for line in b1]
    b6 = [[] for _ in range(len(b5[0]))]
    for line in b5:
        for i, value in enumerate(line):
            b6[i].append(float(value))
    return b6
def fonk5(b6):
    b7 = len(b6[0])
    b1 = [[] for _ in range(b7)]
    for point in range(b7):
        for trace in b6:
            b1[point].append(str(trace[point]))
    return b1