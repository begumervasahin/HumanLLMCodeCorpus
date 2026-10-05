import csv
import math
def fonk1(data):
    b1 = {}
    for element in data:
        b2 = element[-1]
        if b2 not in b1:
            b1[b2] = []
        b1[b2].append(element)
    return b1
def fonk2(numbers):
    return sum(numbers) / float(len(numbers))
def fonk3(numbers):
    b3 = fonk2(numbers)
    b4 = sum(pow(b9 - b3, 2) for b9 in numbers) / float(len(numbers) - 1)
    return math.sqrt(b4)
def fonk4(data):
    b5 = [(fonk2(feature), fonk3(feature)) for feature in zip(*data)]
    del b5[-1]
    return b5
def fonk5(b9, mean, b8):
    b6 = math.exp(-(math.pow(b9 - mean, 2) / (2 * math.pow(b8, 2))))
    return (1 / (math.sqrt(2 * math.pi) * b8)) * b6
def fonk6(b18, sample):
    b7 = {}
    for class_label, b5 in b18.items():
        b7[class_label] = 1
        for b17 in range(len(b5)):
            mean, b8 = b5[b17]
            b9 = sample[b17]
            b10 = fonk5(b9, mean, b8)
            b7[class_label] *= b10
    return b7
def fonk7(b18, sample):
    b7 = fonk6(b18, sample)
    b12, b11 = None, -1
    for class_label, probability in b7.items():
        if b12 is None or probability > b11:
            b11 = probability
            b12 = class_label
    return b12
def fonk8(b18, b19):
    b13 = []
    for sample in b19:
        b14 = fonk7(b18, sample)
        b13.append(b14)
    return b13
def fonk9():
    b15 = []
    with open('data.csv', 'r') as csvfile:
        b16 = csv.b16(csvfile)
        for row in b16:
            for b17 in range(4):
                if b17 = = 3:
                    row[b17] = 1 if row[b17] == 'M' else 2
                row[b17] = float(row[b17])
            b15.append(row)
    b18 = fonk1(b15)
    print('Summary by class class1:')
    for class_label, b5 in b18.items():
        print(f"Class {class_label}: {b5}")
    b19 = [float(b9) for b9 in input('Enter data for b20 (separated by spaces): ').split()]
    b20 = fonk7(b18, b19)
    if b20 = = 1:
        print('Predicted class: M')
    else:
        print('Predicted class: W')
if b21 = = '__main__':
    fonk9()