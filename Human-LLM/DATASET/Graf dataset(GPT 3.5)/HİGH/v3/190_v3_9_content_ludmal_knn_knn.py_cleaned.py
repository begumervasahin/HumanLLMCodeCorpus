import csv
import random
import math
import operator
def fonk1(filename, a1, b1 = 4):
    b2 = []
    b3 = []
    with open(filename, 'r') as csvfile:
        b4 = csv.reader(csvfile)
        b5 = list(b4)
        for b6 in b5:
            b6 = [float(value) for value in b6[:b1]]
            if random.random() < a1:
                b2.append(b6)
            else:
                b3.append(b6)
    return b2, b3
def fonk2(instance1, instance2):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(instance1, instance2)))
def fonk3(b2, test_instance, k):
    b7 = [(train_instance, fonk2(test_instance, train_instance)) for train_instance in b2]
    b7.sort(b8 = operator.itemgetter(1))
    return [distance[0] for distance in b7[:k]]
def fonk4(b13):
    b9 = {}
    for neighbor in b13:
        b10 = neighbor[-1]
        b9[b10] = b9.get(b10, 0) + 1
    return max(b9.items(), b8 = operator.itemgetter(1))[0]
def fonk5(b3, b12):
    b11 = sum(1 for actual, predicted in zip(b3, b12) if actual[-1] == predicted)
    return (b11 / len(b3)) * 100.0
def fonk6():
    a1 = 0.67
    b2, b3 = fonk1('traindata.csv', a1, b1=4)
    print('Train set size:', len(b2))
    print('Test set size:', len(b3))
    b12 = []
    a2 = 3
    for test_instance in b3:
        b13 = fonk3(b2, test_instance, a2)
        b14 = fonk4(b13)
        b12.append(b14)
        print('> Predicted Decision:', b14, ', Actual Decision:', test_instance[-1])
    b15 = fonk5(b3, b12)
    print('Accuracy:', b15, '%')
if b16 = = "__main__":
    fonk6()