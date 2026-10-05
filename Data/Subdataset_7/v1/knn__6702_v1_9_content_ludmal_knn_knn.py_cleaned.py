import csv
import random
import math
import operator
def fonk1(filename, a3, b1 = [], b12=[], signal=4):
    with open(filename, 'r') as csvfile:
        b2 = csv.reader(csvfile)
        b3 = list(b2)
        for x in range(len(b3)-1):
            for y in range(signal):
                b3[x][y] = float(b3[x][y])
            if random.random() < a3:
                b1.append(b3[x])
            else:
                b12.append(b3[x])
def fonk2(instance1, instance2, b5):
    a1 = 0
    for x in range(b5):
        a1 += pow((instance1[x] - instance2[x]), 2)
    return math.sqrt(a1)
def fonk3(b1, test_instance, a4):
    b4 = []
    b5 = len(test_instance) - 1
    for x in range(len(b1)):
        b6 = fonk2(test_instance, b1[x], b5)
        b4.append((b1[x], b6))
    b4.sort(b7 = operator.itemgetter(1))
    b8 = []
    for x in range(a4):
        b8.append(b4[x][0])
    return b8
def fonk4(b8):
    b9 = {}
    for x in range(len(b8)):
        b10 = b8[x][-1]
        if b10 in b9:
            b9[b10] += 1
        else:
            b9[b10] = 1
    b11 = sorted(b9.items(), b7=operator.itemgetter(1), reverse=True)
    return b11[0][0]
def fonk5(b12, b13):
    a2 = 0
    for x in range(len(b12)):
        if b12[x][-1] == b13[x]:
            a2 += 1
    return (a2 / float(len(b12))) * 100.0
def fonk6():
    b1 = []
    b12 = []
    a3 = 0.67
    fonk1('traindata.csv', a3, b1, b12, 4)
    print('Train set: ' + repr(len(b1)))
    print('Test set: ' + repr(len(b12)))
    b13 = []
    a4 = 3
    for x in range(len(b12)):
        b8 = fonk3(b1, b12[x], a4)
        b14 = fonk4(b8)
        b13.append(b14)
        print('> Predicted b15 = ' + repr(b14) + ', Actual b15=' + repr(b12[x][-1]))
    b16 = fonk5(b12, b13)
    print('Accuracy: ' + repr(b16) + '%')
if b17 = = "__main__":
    fonk6()