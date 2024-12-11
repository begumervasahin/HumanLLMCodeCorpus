import csv
import random
import math
import operator
def fonk1(instance1, instance2, b2):
    a1 = 0
    for x in range(b2):
        a1 += pow((float(instance1[x]) - float(instance2[x])), 2)
    return math.sqrt(a1)
def fonk2(b11, testInstance, a4):
    b1 = []
    b2 = len(testInstance) - 1
    for x in range(len(b11)):
        b3 = fonk1(testInstance, b11[x], b2)
        b1.append((b11[x], b3))
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
def fonk4(b12, b15):
    a2 = 0
    for x in range(len(b12)):
        if b12[x][-1] == b15[x]:
            a2 += 1
    return (a2 / float(len(b12))) * 100.0
def fonk5():
    b9 = []
    with open('1.data', 'r') as csvfile:
        b10 = csv.reader(csvfile, delimiter='     ')
        b9.append(list(b10))
    with open('2.data', 'r') as csvfile:
        b10 = csv.reader(csvfile, delimiter='     ')
        b9.append(list(b10))
    with open('3.data', 'r') as csvfile:
        b10 = csv.reader(csvfile, delimiter='     ')
        b9.append(list(b10))
    print('Number of data sets:', len(b9))
    for i, data in enumerate(b9):
        print('Data set {}: {}'.format(i+1, len(data)))
    for data_set in b9:
        for data_instance in data_set:
            for i in range(len(data_instance)):
                data_instance[i] = float(data_instance[i])
    a3 = 0
    for i in range(10):
        b11 = []
        b12 = []
        for data_set in b9:
            b13 = int(0.1 * len(data_set))
            b14 = random.sample(range(len(data_set)), b13)
            for j, instance in enumerate(data_set):
                if j in b14:
                    b12.append(instance)
                else:
                    b11.append(instance)
        print("Training set size:", len(b11))
        print("Test set size:", len(b12))
        b15 = []
        a4 = 1
        for instance in b12:
            b5 = fonk2(b11, instance, a4)
            b16 = fonk3(b5)
            b15.append(b16)
        b17 = fonk4(b12, b15)
        print("Fold {} - Accuracy: {:.2f}%".format(i+1, b17))
        a3 += b17
    print("Average b17 over 10 folds:", a3 / 10)
if b18 = = "__main__":
    fonk5()