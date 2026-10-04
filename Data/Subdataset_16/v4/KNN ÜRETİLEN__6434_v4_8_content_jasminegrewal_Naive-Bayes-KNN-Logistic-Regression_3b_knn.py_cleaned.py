import csv
import math
import operator
def fonk1(set1, set2, b2):
    a1 = 0
    for x in range(b2):
        a1 += (set1[x] - set2[x]) ** 2
    return math.sqrt(a1)
def fonk2(b10, b12, b11):
    b1 = []
    b2 = len(b12)
    for data in b10:
        b3 = fonk1(b12, data, b2)
        b1.append((data, b3))
    b1.sort(b4 = operator.itemgetter(1))
    b5 = [b1[x][0] for x in range(b11)]
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
def fonk4():
    with open('data.csv', 'r') as csvfile:
        b9 = csv.b9(csvfile)
        b10 = []
        for row in b9:
            for y in range(3):
                row[y] = float(row[y])
            if row[3] == 'M':
                row[3] = 1
            else:
                row[3] = 2
            b10.append(row)
    b11 = int(input('Enter number of neighbors to use: '))
    b12 = [float(x) for x in input('Enter data to be predicted (comma separated values): ').split(',')]
    b5 = fonk2(b10, b12, b11)
    b13 = fonk3(b5)
    print('Nearest neighbors:')
    for neighbor in b5:
        print(neighbor)
    print('Prediction for gender with given data:')
    if b13 = = 1:
        print('M')
    else:
        print('F')
if b14 = = "__main__":
    fonk4()