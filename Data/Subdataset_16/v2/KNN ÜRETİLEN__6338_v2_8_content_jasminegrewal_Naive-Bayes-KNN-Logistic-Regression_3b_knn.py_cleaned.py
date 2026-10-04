import csv
import math
from operator import itemgetter
def fonk1(set1, set2, length):
    b1 = sum((set1[i] - set2[i]) ** 2 for i in range(length))
    return math.sqrt(b1)
def fonk2(training_data, b11, b9):
    b2 = [(data, fonk1(b11, data, len(b11))) for data in training_data]
    b2.sort(b3 = itemgetter(1))
    return [b2[i][0] for i in range(b9)]
def fonk3(neighbors):
    b4 = {}
    for neighbor in neighbors:
        b5 = neighbor[-1]
        b4[b5] = b4.get(b5, 0) + 1
    b6 = sorted(b4.items(), b3=itemgetter(1), reverse=True)
    return b6[0][0]
def fonk4(filename):
    with open(filename, 'r') as csvfile:
        b7 = csv.reader(csvfile)
        b8 = list(b7)
        for row in b8:
            for i in range(len(row) - 1):
                row[i] = float(row[i])
            row[-1] = 1 if row[-1] == 'M' else 2
    return b8
def fonk5():
    b8 = fonk4('data.csv')
    b9 = int(input('Enter number of neighbors to use: '))
    b10 = input('Enter data to be predicted (comma-separated): ')
    b11 = list(map(float, b10.split(',')))
    b12 = fonk2(b8, b11, b9)
    b13 = fonk3(b12)
    print('Nearest neighbors are:')
    for neighbor in b12:
        print(neighbor)
    b14 = 'M' if b13 == 1 else 'W'
    print(f'Prediction for b14 with given data is: {b14}')
if b15 = = "__main__":
    fonk5()