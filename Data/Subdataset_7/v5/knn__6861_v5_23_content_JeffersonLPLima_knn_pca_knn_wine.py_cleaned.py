import csv
import random
import math
import operator
def fonk1(instance1, instance2):
    a1 = 0
    for x in range(len(instance1) - 1):
        a1 += (float(instance1[x]) - float(instance2[x])) ** 2
    return math.sqrt(a1)
def fonk2(b8, test_instance, a3):
    b1 = [(train_instance, fonk1(test_instance, train_instance)) for train_instance in b8]
    b1.sort(b2 = operator.itemgetter(1))
    return [neighbor[0] for neighbor in b1[:a3]]
def fonk3(b13):
    b3 = {}
    for neighbor in b13:
        b4 = neighbor[-1]
        b3[b4] = b3.get(b4, 0) + 1
    return max(b3.items(), b2 = operator.itemgetter(1))[0]
def fonk4(b9, b12):
    b5 = sum(1 for x in range(len(b9)) if b9[x][-1] == b12[x])
    return (b5 / float(len(b9))) * 100.0
def fonk5():
    b6 = []
    for i in range(1, 4):
        with open('{}.data'.format(i), 'r') as csvfile:
            b7 = csv.reader(csvfile, delimiter='     ')
            b6.append([list(map(float, line)) for line in b7])
    print('Number of data sets:', len(b6))
    for i, data_set in enumerate(b6):
        print('Data set {}: {}'.format(i+1, len(data_set)))
    a2 = 0
    for i in range(10):
        b8 = []
        b9 = []
        for data_set in b6:
            b10 = int(0.1 * len(data_set))
            b11 = random.sample(range(len(data_set)), b10)
            for j, instance in enumerate(data_set):
                if j in b11:
                    b9.append(instance)
                else:
                    b8.append(instance)
        print("Training set size:", len(b8))
        print("Test set size:", len(b9))
        b12 = []
        a3 = 1
        for instance in b9:
            b13 = fonk2(b8, instance, a3)
            b14 = fonk3(b13)
            b12.append(b14)
        b15 = fonk4(b9, b12)
        print("Fold {} - Accuracy: {:.2f}%".format(i+1, b15))
        a2 += b15
    print("Average b15 over 10 folds:", a2 / 10)
if b16 = = "__main__":
    fonk5()