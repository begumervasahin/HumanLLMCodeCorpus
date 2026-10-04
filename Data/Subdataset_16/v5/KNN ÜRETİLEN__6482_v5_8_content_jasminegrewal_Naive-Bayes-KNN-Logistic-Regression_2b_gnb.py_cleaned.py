import csv
import random
import math
def fonk1(b13):
    b1 = {}
    for element in b13:
        b2 = element[-1]
        if b2 not in b1:
            b1[b2] = []
        b1[b2].append(element)
    return b1
def fonk2(numbers):
    return sum(numbers) / float(len(numbers))
def fonk3(numbers):
    b3 = fonk2(numbers)
    b4 = sum([pow(b10 - b3, 2) for b10 in numbers]) / float(len(numbers) - 1)
    return math.sqrt(b4)
def fonk4(b13):
    b5 = [(fonk2(feature), fonk3(feature)) for feature in zip(*b13)]
    del b5[-1]
    return b5
def fonk5(b13):
    b6 = fonk1(b13)
    b5 = {}
    for b2, instances in b6.items():
        b5[b2] = fonk4(instances)
    return b5
def fonk6(b10, mean, b9):
    b7 = math.exp(-(math.pow(b10 - mean, 2) / (2 * math.pow(b9, 2))))
    return (1 / (math.sqrt(2 * math.pi) * b9)) * b7
def fonk7(b17, sample):
    b8 = {}
    for b2, class_params in b17.items():
        b8[b2] = 1
        for i in range(len(class_params)):
            mean, b9 = class_params[i]
            b10 = sample[i]
            b8[b2] *= fonk6(b10, mean, b9)
    return b8
def fonk8(b17, sample):
    b8 = fonk7(b17, sample)
    b12, b11 = None, -1
    for b2, probability in b8.items():
        if b12 is None or probability > b11:
            b11 = probability
            b12 = b2
    return b12
def fonk9(b17, b18):
    return fonk8(b17, b18)
def fonk10():
    b13 = []
    with open('b13.csv', 'r') as csvfile:
        b14 = csv.b14(csvfile)
        b15 = list(b14)
        for b16 in b15:
            b16 = [float(item) if i != 3 else (1 if item == 'M' else 2) for i, item in enumerate(b16)]
            b13.append(b16)
    b17 = fonk5(b13)
    print(f'Summary by class class1: {b17}')
    b18 = list(map(float, input('Enter b13 for b19 (space-separated): ').split()))
    b19 = fonk9(b17, b18)
    print('M' if b19 = = 1 else 'W')
if b20 = = "__main__":
    fonk10()