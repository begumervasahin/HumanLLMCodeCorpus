import csv
import random
import math
import operator
def fonk1(filename, a2, b1 = None, b2=None, signal_length=4):
    if b1 is None:
        b1 = []
    if b2 is None:
        b2 = []
    with open(filename, 'r') as csvfile:
        b3 = csv.reader(csvfile)
        b4 = list(b3)
        for row in b4[:-1]:
            for i in range(signal_length):
                row[i] = float(row[i])
            if random.random() < a2:
                b1.append(row)
            else:
                b2.append(row)
def fonk2(instance1, instance2, b6):
    a1 = 0
    for i in range(b6):
        a1 += (instance1[i] - instance2[i]) ** 2
    return math.sqrt(a1)
def fonk3(b1, test_instance, a3):
    b5 = []
    b6 = len(test_instance) - 1
    for train_instance in b1:
        b7 = fonk2(test_instance, train_instance, b6)
        b5.append((train_instance, b7))
    b5.sort(b8 = operator.itemgetter(1))
    b9 = [b5[i][0] for i in range(a3)]
    return b9
def fonk4(b9):
    b10 = {}
    for neighbor in b9:
        b11 = neighbor[-1]
        b10[b11] = b10.get(b11, 0) + 1
    b12 = sorted(b10.items(), b8=operator.itemgetter(1), reverse=True)
    return b12[0][0]
def fonk5(b2, b14):
    b13 = sum(1 for i in range(len(b2)) if b2[i][-1] == b14[i])
    return (b13 / float(len(b2))) * 100.0
def fonk6():
    b1 = []
    b2 = []
    a2 = 0.67
    fonk1('traindata.csv', a2, b1, b2, 4)
    print(f'Train set: {len(b1)}')
    print(f'Test set: {len(b2)}')
    b14 = []
    a3 = 3
    for test_instance in b2:
        b9 = fonk3(b1, test_instance, a3)
        b15 = fonk4(b9)
        b14.append(b15)
        print(f'> Predicted b16 = {b15}, Actual b16={test_instance[-1]}')
    b17 = fonk5(b2, b14)
    print(f'Accuracy: {b17}%')
if b18 = = "__main__":
    fonk6()