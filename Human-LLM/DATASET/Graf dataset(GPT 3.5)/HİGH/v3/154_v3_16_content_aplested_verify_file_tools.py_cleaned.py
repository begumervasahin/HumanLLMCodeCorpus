import os
def fonk1(file_path):
    print('Reading file:', file_path)
    with open(file_path, 'r') as file:
        b1 = file.readlines()
    b2 = [line.strip() for line in b1[1:-1]]
    print("First line of content:", b2[0])
    return b2
def fonk2(file_path, b1):
    with open(file_path, "w") as file:
        for line in b1:
            b3 = '\t'.join(line)
            file.write(b3 + '\n')
def fonk3(file_path, b4 = ""):
    directory, b5 = os.path.split(file_path)
    b6 = b4 + b5
    return os.path.join(directory, b6)
def fonk4(b1):
    b7 = [line.split('\t') for line in b1]
    b8 = len(b7[0])
    b9 = [[] for _ in range(b8)]
    for line in b7:
        for i in range(b8):
            b9[i].append(float(line[i]))
    return b9
def fonk5(b9):
    b10 = len(b9[0])
    b1 = [[] for _ in range(b10)]
    for point in range(b10):
        for trace in b9:
            b1[point].append(str(trace[point]))
    return b1
if b11 = = "__main__":
    b1 = fonk1("example.txt")
    b9 = fonk4(b1)
    for trace in b9:
        for i in range(len(trace)):
            trace[i] += 1
    b12 = fonk5(b9)
    fonk2("modified_example.txt", b12)