import csv
import math
import operator
def fonk1(set1, set2, b2):
    a1 = 0
    for x in range(b2):
        a1 += pow((set1[x] - set2[x]), 2)
    return math.sqrt(a1)
def fonk2(b11, sample, b12):
    b1 = []
    b2 = len(sample)
    for x in range(len(b11)):
        b3 = fonk1(sample, b11[x], b2)
        b1.append((b11[x], b3))
    b1.sort(b4 = operator.itemgetter(1))
    b5 = [b3[0] for b3 in b1[:b12]]
    return b5
def fonk3(neighbors):
    b6 = {}
    for neighbor in neighbors:
        b7 = neighbor[-1]
        if b7 in b6:
            b6[b7] += 1
        else:
            b6[b7] = 1
    b8 = sorted(b6.items(), b4=operator.itemgetter(1), reverse=True)
    return b8[0][0]
def fonk4(data):
    for entry in data:
        for b9 in range(3):
            if b9 = = 2:
                if entry[b9] == 'M':
                    entry[b9] = 1
                else:
                    entry[b9] = 0
            entry[b9] = float(entry[b9])
    return data
def fonk5():
    with open('data.csv', 'r') as csvfile:
        b10 = csv.reader(csvfile)
        b11 = list(b10)
        b11 = fonk4(b11)
    b12 = int(input('Enter the number of neighbors to use: '))
    b13 = [float(x) for x in input('Enter the data to be predicted: ').split()]
    b5 = fonk2(b11, b13, b12)
    b14 = fonk3(b5)
    print('Nearest neighbors are:')
    for neighbor in b5:
        print(neighbor)
    print('Prediction for gender with given data is:')
    if b14 = = 1:
        print('Male')
    else:
        print('Female')
if b15 = = '__main__':
    fonk5()