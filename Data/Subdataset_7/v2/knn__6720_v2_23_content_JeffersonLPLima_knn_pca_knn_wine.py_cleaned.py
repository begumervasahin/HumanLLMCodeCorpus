import csv
import math
import operator
import random
def fonk1(instance1, instance2):
    a1 = 0
    for x in range(len(instance1) - 1):
        a1 += pow((float(instance1[x]) - float(instance2[x])), 2)
    return math.sqrt(a1)
def fonk2(b13, testInstance, a4):
    b1 = []
    for x in range(len(b13)):
        b2 = fonk1(testInstance, b13[x])
        b1.append((b13[x], b2))
    b1.sort(b3 = operator.itemgetter(1))
    b4 = []
    for x in range(a4):
        b4.append(b1[x][0])
    return b4
def fonk3(b4):
    b5 = {}
    for x in range(len(b4)):
        b6 = b4[x][-1]
        if b6 in b5:
            b5[b6] += 1
        else:
            b5[b6] = 1
    b7 = sorted(b5.items(), b3=operator.itemgetter(1), reverse=True)
    return b7[0][0]
def fonk4(b14, b16):
    a2 = 0
    for x in range(len(b14)):
        if b14[x][-1] == b16[x]:
            a2 += 1
    return (a2 / float(len(b14))) * 100.0
def fonk5(filename):
    b8 = []
    with open(filename, 'r') as csvfile:
        b9 = csv.reader(csvfile, delimiter=' ')
        for row in b9:
            b8.append([float(x) for x in row])
    return b8
def fonk6():
    b10 = fonk5('1.data')
    b11 = fonk5('2.data')
    b12 = fonk5('3.data')
    print('Dataset lengths:')
    print('Data 1:', len(b10))
    print('Data 2:', len(b11))
    print('Data 3:', len(b12))
    a3 = 0
    for i in range(10):
        b13 = []
        b14 = []
        for data in [b10, b11, b12]:
            random.shuffle(data)
            b15 = int(0.1 * len(data))
            b14.extend(data[i * b15: (i + 1) * b15])
            b13.extend(data[:i * b15] + data[(i + 1) * b15:])
        print("\nFold", i)
        print("Training set:", len(b13))
        print("Test set:", len(b14))
        b16 = []
        a4 = 1
        for instance in b14:
            b4 = fonk2(b13, instance, a4)
            b17 = fonk3(b4)
            b16.append(b17)
        b18 = fonk4(b14, b16)
        print("Accuracy:", b18)
        a3 += b18
    print("\nAverage b18 over 10 folds:", a3 / 10)
if b19 = = "__main__":
    fonk6()