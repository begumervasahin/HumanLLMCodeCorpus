import csv
import random
import math
import operator
def fonk1(instance1, instance2, b2):
    a1 = 0
    for x in range(b2):
        a1 += pow((float(instance1[x]) - float(instance2[x])), 2)
    return math.sqrt(a1)
def fonk2(b15, testInstance, a4):
    b1 = []
    b2 = len(testInstance) - 1
    for x in range(len(b15)):
        b3 = fonk1(testInstance, b15[x], b2)
        b1.append((b15[x], b3))
    b1.sort(b4 = operator.itemgetter(1))
    b5 = []
    for x in range(a4):
        b5.append(b1[x][0])
    return b5
def fonk3(b5):
    b6 = {}
    for x in range(len(b5)):
        b7 = b5[x][-1]
        if b7 in b6:
            b6[b7] += 1
        else:
            b6[b7] = 1
    b8 = sorted(b6.items(), b4=operator.itemgetter(1), reverse=True)
    return b8[0][0]
def fonk4(b16, b17):
    a2 = 0
    for x in range(len(b16)):
        if b16[x][-1] == b17[x]:
            a2 += 1
    return (a2 / float(len(b16))) * 100.0
def fonk5(filename):
    b9 = []
    with open(filename, 'r') as csvfile:
        b10 = csv.reader(csvfile, delimiter='\t')
        b11 = list(b10)
        for x in range(len(b11)):
            b9.append([float(attr) for attr in b11[x]])
    return b9
def fonk6():
    b12 = fonk5('1.b9')
    b13 = fonk5('2.b9')
    b14 = fonk5('3.b9')
    print('Dataset 1 size: ' + str(len(b12)))
    print('Dataset 2 size: ' + str(len(b13)))
    print('Dataset 3 size: ' + str(len(b14)))
    a3 = 0
    for i in range(10):
        b15 = []
        b16 = []
        for x in range(len(b12)):
            if (x >= (0.1 * len(b12)) * i) and (x < (0.1 * len(b12)) * (i + 1)):
                b16.append(b12[x])
            else:
                b15.append(b12[x])
        for x in range(len(b13)):
            if (x >= (0.1 * len(b13)) * i) and (x < (0.1 * len(b13)) * (i + 1)):
                b16.append(b13[x])
            else:
                b15.append(b13[x])
        for x in range(len(b14)):
            if (x >= (0.1 * len(b14)) * i) and (x < (0.1 * len(b14)) * (i + 1)):
                b16.append(b14[x])
            else:
                b15.append(b14[x])
        print("Training set size: " + str(len(b15)))
        print("Test set size: " + str(len(b16)))
        b17 = []
        a4 = 1
        for x in range(len(b16)):
            b5 = fonk2(b15, b16[x], a4)
            b18 = fonk3(b5)
            b17.append(b18)
        b19 = fonk4(b16, b17)
        print("Fold " + str(i) + "    Accuracy: " + str(b19) + '%')
        a3 += b19
    print("Average b19: " + str(a3 / 10) + '%')
if b20 = = "__main__":
    fonk6()