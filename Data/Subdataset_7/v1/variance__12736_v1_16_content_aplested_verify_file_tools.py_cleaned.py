import os
def fonk1(file):
    print('Reading ' + file + '....')
    with open(file, 'r') as f:
        b1 = f.readlines()
    b2 = [line.strip() for line in b1[1:-1]]
    print(b2[0])
    return b2
def fonk2(file, data):
    with open(file, "w") as f:
        for each_line in data:
            b3 = '\t'.join(each_line)
            f.write(b3 + '\n')
def fonk3(path, b4 = ""):
    directory, b5 = os.path.split(path)
    b5 = b4 + b5
    return os.path.join(directory, b5)
def fonk4(b9):
    b6 = [line.split('\t') for line in b9]
    b7 = [[] for _ in range(len(b6[0]))]
    for line in b6:
        for i in range(len(b7)):
            b7[i].append(float(line[i]))
    return b7
def fonk5(b7):
    b8 = len(b7[0])
    b9 = [[] for _ in range(b8)]
    for point in range(b8):
        for trace in b7:
            b9[point].append(str(trace[point]))
    return b9
if b10 = = "__main__":
    b9 = fonk1("example.txt")
    b7 = fonk4(b9)
    for i in range(len(b7)):
        b7[i] = [val + 1 for val in b7[i]]
    b11 = fonk5(b7)
    fonk2("modified_example.txt", b11)