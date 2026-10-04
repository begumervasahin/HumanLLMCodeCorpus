import csv
import math
import operator
def fonk1(instance1, instance2, b2):
    a1 = 0
    for x in range(b2):
        a1 += pow((float(instance1[x]) - float(instance2[x])), 2)
    return math.sqrt(a1)
def fonk2(b16, test_instance, a3):
    b1 = []
    b2 = len(test_instance) - 1
    for x in range(len(b16)):
        b3 = fonk1(test_instance, b16[x], b2)
        b1.append((b16[x], b3))
    b1.sort(b4 = operator.itemgetter(1))
    b5 = [b1[x][0] for x in range(a3)]
    return b5
def fonk3(b5):
    b6 = {}
    for neighbor in b5:
        b7 = neighbor[-1]
        b6[b7] = b6.get(b7, 0) + 1
    b8 = sorted(b6.items(), b4=operator.itemgetter(1), reverse=True)
    return b8[0][0]
def fonk4(b17, b18):
    b9 = sum(1 for x in range(len(b17)) if b17[x][-1] == b18[x])
    return (b9 / float(len(b17))) * 100.0
def fonk5(filename):
    b10 = []
    with open(filename, 'r') as csvfile:
        b11 = csv.reader(csvfile, delimiter='\t')
        b12 = list(b11)
        for row in b12:
            b10.append([float(attr) for attr in row])
    return b10
def fonk6():
    b13 = fonk5('1.b10')
    b14 = fonk5('2.b10')
    b15 = fonk5('3.b10')
    print(f'Dataset 1 size: {len(b13)}')
    print(f'Dataset 2 size: {len(b14)}')
    print(f'Dataset 3 size: {len(b15)}')
    a2 = 0
    for i in range(10):
        b16 = []
        b17 = []
        for x in range(len(b13)):
            if (x >= (0.1 * len(b13)) * i) and (x < (0.1 * len(b13)) * (i + 1)):
                b17.append(b13[x])
            else:
                b16.append(b13[x])
        for x in range(len(b14)):
            if (x >= (0.1 * len(b14)) * i) and (x < (0.1 * len(b14)) * (i + 1)):
                b17.append(b14[x])
            else:
                b16.append(b14[x])
        for x in range(len(b15)):
            if (x >= (0.1 * len(b15)) * i) and (x < (0.1 * len(b15)) * (i + 1)):
                b17.append(b15[x])
            else:
                b16.append(b15[x])
        print(f"Training set size: {len(b16)}")
        print(f"Test set size: {len(b17)}")
        b18 = []
        a3 = 1
        for x in range(len(b17)):
            b5 = fonk2(b16, b17[x], a3)
            b19 = fonk3(b5)
            b18.append(b19)
        b20 = fonk4(b17, b18)
        print(f"Fold {i}    Accuracy: {b20:.2f}%")
        a2 += b20
    print(f"Average b20: {a2 / 10:.2f}%")
if b21 = = "__main__":
    fonk6()