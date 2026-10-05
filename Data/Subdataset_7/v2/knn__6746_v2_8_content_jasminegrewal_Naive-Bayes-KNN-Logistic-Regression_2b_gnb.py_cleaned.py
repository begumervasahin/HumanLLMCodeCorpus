import csv
import random
import math
def fonk1(b16):
    b1 = {}
    for instance in b16:
        b2 = instance[-1]
        if b2 not in b1:
            b1[b2] = []
        b1[b2].append(instance)
    return b1
def fonk2(numbers):
    return sum(numbers) / len(numbers)
def fonk3(numbers):
    b3 = fonk2(numbers)
    b4 = sum((b9 - b3) ** 2 for b9 in numbers) / (len(numbers) - 1)
    return math.sqrt(b4)
def fonk4(b16):
    b5 = [(fonk2(feature), fonk3(feature)) for feature in zip(*b16)]
    del b5[-1]
    return b5
def fonk5(b9, mean, b8):
    b6 = math.exp(-(math.pow(b9 - mean, 2) / (2 * math.pow(b8, 2))))
    return (1 / (math.sqrt(2 * math.pi) * b8)) * b6
def fonk6(b5, sample):
    b7 = {}
    for class_label, params in b5.items():
        b7[class_label] = 1
        for b17 in range(len(params)):
            mean, b8 = params[b17]
            b9 = sample[b17]
            b10 = fonk5(b9, mean, b8)
            b7[class_label] *= b10
    return b7
def fonk7(b5, sample):
    b7 = fonk6(b5, sample)
    b12, b11 = None, -1
    for class_label, probability in b7.items():
        if b12 is None or probability > b11:
            b11 = probability
            b12 = class_label
    return b12
def fonk8(b5, b18):
    b13 = fonk7(b5, b18)
    return b13
def fonk9():
    b14 = []
    with open('b16.csv', 'r') as csvfile:
        b15 = csv.b15(csvfile)
        b16 = list(b15)
        for row in b16:
            for b17 in range(4):
                if b17 = = 3:
                    row[b17] = 1 if row[b17] == 'M' else 2
                row[b17] = float(row[b17])
            b14.append(row)
    b5 = fonk1(b14)
    print('Summary by class class1: {0}'.format(b5))
    b18 = [float(input('Enter b16 for b19: ')) for _ in range(4)]
    b19 = fonk8(b5, b18)
    print('Predicted class:', 'M' if b19 = = 1 else 'W')
if b20 = = "__main__":
    fonk9()