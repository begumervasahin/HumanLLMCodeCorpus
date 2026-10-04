import csv
import random
import math
import operator
def fonk1(b11, a1, b1 = 4):
    train_set, b2 = [], []
    with open(b11, 'r') as csvfile:
        b3 = csv.reader(csvfile)
        b4 = list(b3)
        for row in b4[:-1]:
            for i in range(b1):
                row[i] = float(row[i])
            if random.random() < a1:
                train_set.append(row)
            else:
                b2.append(row)
    return train_set, b2
def fonk2(instance1, instance2, length):
    return math.sqrt(sum(pow(instance1[i] - instance2[i], 2) for i in range(length)))
def fonk3(train_set, test_instance, a2):
    b5 = [(train_instance, fonk2(test_instance, train_instance, len(test_instance) - 1)) for train_instance in train_set]
    b5.sort(b6 = operator.itemgetter(1))
    return [b5[i][0] for i in range(a2)]
def fonk4(b13):
    b7 = {}
    for neighbor in b13:
        b8 = neighbor[-1]
        b7[b8] = b7.get(b8, 0) + 1
    b9 = sorted(b7.items(), b6=operator.itemgetter(1), reverse=True)
    return b9[0][0]
def fonk5(b2, b12):
    b10 = sum(1 for i in range(len(b2)) if b2[i][-1] == b12[i])
    return (b10 / float(len(b2))) * 100.0
def fonk6():
    b11 = 'traindata.csv'
    a1 = 0.67
    a2 = 3
    train_set, b2 = fonk1(b11, a1)
    print(f'Train set: {len(train_set)}')
    print(f'Test set: {len(b2)}')
    b12 = []
    for test_instance in b2:
        b13 = fonk3(train_set, test_instance, a2)
        b14 = fonk4(b13)
        b12.append(b14)
        print(f'> b15 = {b14}, actual={test_instance[-1]}')
    b16 = fonk5(b2, b12)
    print(f'Accuracy: {b16:.2f}%')
if b17 = = '__main__':
    fonk6()