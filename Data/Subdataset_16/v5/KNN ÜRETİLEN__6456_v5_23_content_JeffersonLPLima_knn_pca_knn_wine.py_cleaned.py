import csv
import math
import operator
def fonk1(instance1, instance2, length):
    return math.sqrt(sum((float(instance1[x]) - float(instance2[x])) ** 2 for x in range(length)))
def fonk2(training_set, test_instance, a2):
    b1 = [(training_instance, fonk1(test_instance, training_instance, len(test_instance) - 1))
                 for training_instance in training_set]
    b1.sort(b2 = operator.itemgetter(1))
    return [b1[x][0] for x in range(a2)]
def fonk3(b18):
    b3 = {}
    for neighbor in b18:
        b4 = neighbor[-1]
        b3[b4] = b3.get(b4, 0) + 1
    b5 = sorted(b3.items(), b2=operator.itemgetter(1), reverse=True)
    return b5[0][0]
def fonk4(b13, b17):
    b6 = sum(1 for x in range(len(b13)) if b13[x][-1] == b17[x])
    return (b6 / float(len(b13))) * 100.0
def fonk5(filename, b7 = '\t'):
    b8 = []
    with open(filename, 'r') as csvfile:
        b9 = csv.reader(csvfile, b7=b7)
        for line in b9:
            b8.append([float(value) for value in line])
    return b8
def fonk6():
    b10 = fonk5('1.b8')
    b11 = fonk5('2.b8')
    b12 = fonk5('3.b8')
    print(f'Training set size: {len(b10)}')
    print(f'Set 1 size: {len(b10)}')
    print(f'Set 2 size: {len(b11)}')
    print(f'Set 3 size: {len(b12)}')
    a1 = 0
    for fold in range(10):
        training_set, b13 = [], []
        for b8 in (b10, b11, b12):
            b14 = len(b8)
            b15 = b14 * fold
            b16 = b15 + b14
            for index, instance in enumerate(b8):
                if b15 <= index < b16:
                    b13.append(instance)
                else:
                    training_set.append(instance)
        print(f"Fold {fold}: Training set size: {len(training_set)}, Test set size: {len(b13)}")
        b17 = []
        a2 = 1
        for test_instance in b13:
            b18 = fonk2(training_set, test_instance, a2)
            b19 = fonk3(b18)
            b17.append(b19)
        b20 = fonk4(b13, b17)
        print(f"Fold {fold} Accuracy: {b20:.2f}%")
        a1 += b20
    print(f"Average Accuracy: {a1 / 10:.2f}%")
if b21 = = "__main__":
    fonk6()