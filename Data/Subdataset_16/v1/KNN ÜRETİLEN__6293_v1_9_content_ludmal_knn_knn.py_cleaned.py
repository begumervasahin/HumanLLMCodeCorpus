import csv
import random
import math
import operator
def fonk1(filename, a1, b1 = None, b2=None, signal=4):
    if b1 is None:
        b1 = []
    if b2 is None:
        b2 = []
    with open(filename, 'r') as csvfile:
        b3 = csv.reader(csvfile)
        b4 = list(b3)
        for x in range(len(b4) - 1):
            for y in range(signal):
                b4[x][y] = float(b4[x][y])
            if random.random() < a1:
                b1.append(b4[x])
            else:
                b2.append(b4[x])
    return b1, b2
def fonk2(instance1, instance2, length):
    return math.sqrt(sum(pow(instance1[x] - instance2[x], 2) for x in range(length)))
def fonk3(b1, test_instance, a2):
    b5 = [(train_instance, fonk2(test_instance, train_instance, len(test_instance) - 1)) for train_instance in b1]
    b5.sort(b6 = operator.itemgetter(1))
    return [b5[x][0] for x in range(a2)]
def fonk4(b12):
    b7 = {}
    for neighbor in b12:
        b8 = neighbor[-1]
        b7[b8] = b7.get(b8, 0) + 1
    b9 = sorted(b7.items(), b6=operator.itemgetter(1), reverse=True)
    return b9[0][0]
def fonk5(b2, b11):
    b10 = sum(1 for x in range(len(b2)) if b2[x][-1] == b11[x])
    return (b10 / float(len(b2))) * 100.0
def fonk6():
    b1, b2 = [], []
    a1 = 0.67
    b1, b2 = fonk1('traindata.csv', a1, b1, b2, 4)
    print('Train set:', len(b1))
    print('Test set:', len(b2))
    b11 = []
    a2 = 3
    for test_instance in b2:
        b12 = fonk3(b1, test_instance, a2)
        b13 = fonk4(b12)
        b11.append(b13)
        print(f'> predicted b14 = {b13}, Actual b14={test_instance[-1]}')
    b15 = fonk5(b2, b11)
    print(f'Accuracy: {b15}%')
if b16 = = '__main__':
    fonk6()