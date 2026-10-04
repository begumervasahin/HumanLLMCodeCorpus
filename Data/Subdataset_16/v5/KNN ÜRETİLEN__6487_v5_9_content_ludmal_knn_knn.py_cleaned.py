import csv
import random
import math
import operator
def fonk1(b13, a1, b1 = 4):
    b2 = []
    b3 = []
    with open(b13, 'r') as csvfile:
        b4 = csv.reader(csvfile)
        b5 = list(b4)
        for row in b5[:-1]:
            for i in range(b1):
                row[i] = float(row[i])
            if random.random() < a1:
                b2.append(row)
            else:
                b3.append(row)
    return b2, b3
def fonk2(instance1, instance2, b6):
    return math.sqrt(sum((instance1[i] - instance2[i]) ** 2 for i in range(b6)))
def fonk3(b2, test_instance, a2):
    b6 = len(test_instance) - 1
    b7 = [(train_instance, fonk2(test_instance, train_instance, b6)) for train_instance in b2]
    b7.sort(b8 = operator.itemgetter(1))
    return [b7[i][0] for i in range(a2)]
def fonk4(b15):
    b9 = {}
    for neighbor in b15:
        b10 = neighbor[-1]
        b9[b10] = b9.get(b10, 0) + 1
    b11 = sorted(b9.items(), b8=operator.itemgetter(1), reverse=True)
    return b11[0][0]
def fonk5(b3, b14):
    b12 = sum(1 for i in range(len(b3)) if b3[i][-1] == b14[i])
    return (b12 / float(len(b3))) * 100.0
def fonk6():
    a1 = 0.67
    b13 = 'traindata.csv'
    b1 = 4
    a2 = 3
    b2, b3 = fonk1(b13, a1, b1)
    print(f'Train set: {len(b2)}')
    print(f'Test set: {len(b3)}')
    b14 = []
    for test_instance in b3:
        b15 = fonk3(b2, test_instance, a2)
        b16 = fonk4(b15)
        b14.append(b16)
        print(f'> Predicted b17 = {b16}, Actual b17={test_instance[-1]}')
    b18 = fonk5(b3, b14)
    print(f'Accuracy: {b18:.2f}%')
if b19 = = "__main__":
    fonk6()