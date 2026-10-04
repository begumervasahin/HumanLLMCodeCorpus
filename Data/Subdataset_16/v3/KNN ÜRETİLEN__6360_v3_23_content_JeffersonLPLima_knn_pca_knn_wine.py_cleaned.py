import csv
import math
import operator
def fonk1(instance1, instance2, length):
    return math.sqrt(sum((float(instance1[x]) - float(instance2[x])) ** 2 for x in range(length)))
def fonk2(training_set, test_instance, k):
    b1 = [(train_instance, fonk1(test_instance, train_instance, len(test_instance) - 1)) for train_instance in training_set]
    b1.sort(b2 = operator.itemgetter(1))
    return [b1[x][0] for x in range(k)]
def fonk3(neighbors):
    b3 = {}
    for neighbor in neighbors:
        b4 = neighbor[-1]
        b3[b4] = b3.get(b4, 0) + 1
    b5 = sorted(b3.items(), b2=operator.itemgetter(1), reverse=True)
    return b5[0][0]
def fonk4(b11, b13):
    b6 = sum(1 for x in range(len(b11)) if b11[x][-1] == b13[x])
    return (b6 / float(len(b11))) * 100.0
def fonk5(filename):
    b7 = []
    with open(filename, 'r') as csvfile:
        b8 = csv.b8(csvfile, delimiter='\t')
        for row in b8:
            b7.append([float(attr) for attr in row])
    return b7
def fonk6():
    b9 = [fonk5(f'{i}.b7') for i in range(1, 4)]
    for i, dataset in enumerate(b9, b10 = 1):
        print(f'Dataset {i} size: {len(dataset)}')
    a1 = 0
    for i in range(10):
        training_set, b11 = [], []
        for dataset in b9:
            b12 = len(dataset)
            b11.extend(dataset[i * b12: (i + 1) * b12])
            training_set.extend(dataset[:i * b12] + dataset[(i + 1) * b12:])
        print(f"Fold {i + 1}")
        print(f"Training set size: {len(training_set)}")
        print(f"Test set size: {len(b11)}")
        b13 = [fonk3(fonk2(training_set, test_instance, k=1)) for test_instance in b11]
        b14 = fonk4(b11, b13)
        print(f"Accuracy: {b14:.2f}%")
        a1 += b14
    print(f"Average b14: {a1 / 10:.2f}%")
if b15 = = "__main__":
    fonk6()