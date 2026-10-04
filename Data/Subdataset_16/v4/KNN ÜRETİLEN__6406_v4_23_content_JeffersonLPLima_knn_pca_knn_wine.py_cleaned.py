import csv
import math
import operator
def fonk1(instance1, instance2, b2):
    a1 = 0
    for x in range(b2):
        a1 += pow((float(instance1[x]) - float(instance2[x])), 2)
    return math.sqrt(a1)
def fonk2(b16, test_instance, a3):
    b1 = []
    b2 = len(test_instance) - 1
    for training_instance in b16:
        b3 = fonk1(test_instance, training_instance, b2)
        b1.append((training_instance, b3))
    b1.sort(b4 = operator.itemgetter(1))
    b5 = [b1[x][0] for x in range(a3)]
    return b5
def fonk3(b5):
    b6 = {}
    for neighbor in b5:
        b7 = neighbor[-1]
        b6[b7] = b6.get(b7, 0) + 1
    b8 = sorted(b6.items(), b4=operator.itemgetter(1), reverse=True)
    return b8[0][0]
def fonk4(b17, b18):
    b9 = sum(1 for x in range(len(b17)) if b17[x][-1] == b18[x])
    return (b9 / float(len(b17))) * 100.0
def fonk5(filename, b10 = '\t'):
    b11 = []
    with open(filename, 'r') as csvfile:
        b12 = csv.reader(csvfile, b10=b10)
        for line in b12:
            b11.append([float(value) for value in line])
    return b11
def fonk6():
    b13 = fonk5('1.b11')
    b14 = fonk5('2.b11')
    b15 = fonk5('3.b11')
    print(f'Training set size: {len(b13)}')
    print(f'Set 1 size: {len(b13)}')
    print(f'Set 2 size: {len(b14)}')
    print(f'Set 3 size: {len(b15)}')
    a2 = 0
    for i in range(10):
        b16 = []
        b17 = []
        for b11 in (b13, b14, b15):
            for index, instance in enumerate(b11):
                if (0.1 * len(b11) * i) <= index < (0.1 * len(b11) * (i + 1)):
                    b17.append(instance)
                else:
                    b16.append(instance)
        print(f"Training set size: {len(b16)}")
        print(f"Test set size: {len(b17)}")
        b18 = []
        a3 = 1
        for test_instance in b17:
            b5 = fonk2(b16, test_instance, a3)
            b19 = fonk3(b5)
            b18.append(b19)
        b20 = fonk4(b17, b18)
        print(f"Fold {i} Accuracy: {b20:.2f}%")
        a2 += b20
    print(f"Average Accuracy: {a2 / 10:.2f}%")
if b21 = = "__main__":
    fonk6()