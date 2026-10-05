import csv
import random
import math
def fonk1(data):
    b1 = {}
    for i in range(len(data)):
        b2 = data[i]
        if b2[-1] not in b1:
            b1[b2[-1]] = []
        b1[b2[-1]].append(b2)
    return b1
def fonk2(numbers):
    return sum(numbers) / float(len(numbers))
def fonk3(numbers):
    b3 = fonk2(numbers)
    b4 = sum([pow(b10 - b3, 2) for b10 in numbers]) / float(len(numbers) - 1)
    return math.sqrt(b4)
def fonk4(data):
    b5 = [(fonk2(feature), fonk3(feature)) for feature in zip(*data)]
    del b5[-1]
    return b5
def fonk5(data):
    b6 = fonk1(data)
    b5 = {}
    for clsslabel, instances in b6.items():
        b5[clsslabel] = fonk4(instances)
    return b5
def fonk6(b10, mean, b9):
    b7 = math.exp(-(math.pow(b10 - mean, 2) / (2 * math.pow(b9, 2))))
    return (1 / (math.sqrt(2 * math.pi) * b9)) * b7
def fonk7(b20, sample):
    b8 = {}
    for clsslabel, b5 in b20.items():
        b8[clsslabel] = 1
        for i in range(len(b5)):
            mean, b9 = b5[i]
            b10 = sample[i]
            b11 = fonk6(b10, mean, b9)
            print('prob densities')
            print(b11)
            b8[clsslabel] *= b11
    print('ClssProbabilities(b10/c)')
    print(b8)
    return b8
def fonk8(b20, sample):
    b12 = fonk7(b20, sample)
    b14, b13 = None, -1
    for clsslabel, probability in b12.items():
        if b14 is None or probability > b13:
            b13 = probability
            b14 = clsslabel
    return b14
def fonk9(b20, b21):
    b15 = fonk8(b20, b21)
    return b15
def fonk10():
    b16 = []
    with open('data.csv', 'r') as csvfile:
        b17 = csv.reader(csvfile)
        b18 = list(b17)
        for b10 in range(len(b18)):
            for b19 in range(4):
                if b19 = = 3:
                    if b18[b10][b19] == 'M':
                        b18[b10][b19] = 1
                    else:
                        b18[b10][b19] = 2
                b18[b10][b19] = float(b18[b10][b19])
            b16.append(b18[b10])
    b20 = fonk5(b16)
    print('Summary by class class1: {0}'.format(b20))
    b21 = []
    for i in range(4):
        b21.append(float(input('Enter data for b22: ')))
    b22 = fonk9(b20, b21)
    if b22 = = 1:
        print('M')
    else:
        print('W')
if b23 = = "__main__":
    fonk10()