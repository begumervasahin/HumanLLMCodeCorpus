import os
def fonk1(file_path):
    print(f'Reading {file_path}...')
    with open(file_path, 'r') as file:
        b1 = file.read().strip().split('\n')
    if b1:
        b1 = b1[1:]
    if b1:
        b1 = b1[:-1]
    if b1:
        print(b1[0])
    return b1
def fonk2(file_path, data):
    with open(file_path, 'w') as file:
        for line in data:
            file.write(f"{line}\r")
def fonk3(path, b2 = ""):
    directory, b3 = os.path.split(path)
    b4 = b2 + b3
    return os.path.join(directory, b4)
def fonk4(b1):
    b5 = [list(map(float, line.split('\t'))) for line in b1]
    b6 = len(b5[0])
    b7 = [[] for _ in range(b6)]
    for trace in b5:
        for i, value in enumerate(trace):
            b7[i].append(value)
    return b7
def fonk5(b5):
    b8 = len(b5[0])
    b1 = ['\t'.join(map(str, trace_point)) for trace_point in zip(*b5)]
    return b1
if b9 = = "__main__":
    b10 = "input.txt"
    b11 = "output.txt"
    b2 = "new_"
    b1 = fonk1(b10)
    b5 = fonk4(b1)
    b12 = fonk5(b5)
    fonk2(b11, b12)
    b4 = fonk3(b11, b2)
    print(f'New b3: {b4}')