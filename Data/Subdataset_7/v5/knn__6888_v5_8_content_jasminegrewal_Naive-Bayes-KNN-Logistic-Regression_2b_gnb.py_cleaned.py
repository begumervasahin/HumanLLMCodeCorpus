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
    return sum(numbers) / len(numbers)
def fonk3(numbers):
    b3 = fonk2(numbers)
    b4 = sum((b9 - b3) ** 2 for b9 in numbers) / len(numbers)
    return math.sqrt(b4)
def fonk4(data):
    b5 = [(fonk2(feature), fonk3(feature)) for feature in zip(*data)]
    del b5[-1]
    return b5
def fonk5(b9, mean, b8):
    b6 = math.exp(-(pow(b9 - mean, 2) / (2 * pow(b8, 2))))
    return (1 / (math.sqrt(2 * math.pi) * b8)) * b6
def fonk6(b19, sample):
    b7 = {}
    for class_label, b5 in b19.items():
        b7[class_label] = 1
        for i in range(len(b5)):
            mean, b8 = b5[i]
            b9 = sample[i]
            b10 = fonk5(b9, mean, b8)
            b7[class_label] *= b10
    return b7
def fonk7(b19, sample):
    b7 = fonk6(b19, sample)
    b12, b11 = None, -1
    for class_label, probability in b7.items():
        if b12 is None or probability > b11:
            b11 = probability
            b12 = class_label
    return b12
def fonk8(b19, b20):
    b13 = []
    for sample in b20:
        b14 = fonk7(b19, sample)
        b13.append(b14)
    return b13
def fonk9(file_path):
    b15 = []
    with open(file_path, 'r') as csvfile:
        b16 = csv.b16(csvfile)
        for b17 in b16:
            b17 = [float(class1) for class1 in b17]
            b17[-1] = 1 if b17[-1] == 'M' else 2
            b15.append(b17)
    return b15
def fonk10(b19):
    print('Summary by class class1:')
    for class_label, b5 in b19.items():
        print(f"Class {class_label}: {b5}")
def fonk11():
    b15 = fonk9('data.csv')
    b18 = fonk1(b15)
    b19 = {class_label: fonk4(data) for class_label, data in b18.items()}
    fonk10(b19)
    b20 = [float(b9) for b9 in input('Enter data for b21 (separated by spaces): ').split()]
    b21 = fonk7(b19, b20)
    b22 = 'M' if b21 == 1 else 'W'
    print(f'Predicted class: {b22}')
if b23 = = '__main__':
    fonk11()