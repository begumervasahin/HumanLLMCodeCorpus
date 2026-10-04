import csv
import math
from operator import itemgetter
def fonk1(set1, set2):
    return math.sqrt(sum((set1[i] - set2[i]) ** 2 for i in range(len(set1))))
def fonk2(training_data, b9, b7):
    b1 = [(data, fonk1(b9, data)) for data in training_data]
    b1.sort(b2 = itemgetter(1))
    return [b1[i][0] for i in range(b7)]
def fonk3(neighbors):
    b3 = {}
    for neighbor in neighbors:
        b4 = neighbor[-1]
        b3[b4] = b3.get(b4, 0) + 1
    return max(b3.items(), b2 = itemgetter(1))[0]
def fonk4(filename):
    b5 = []
    with open(filename, 'r') as csvfile:
        b6 = csv.reader(csvfile)
        for row in b6:
            for i in range(len(row) - 1):
                row[i] = float(row[i])
            row[-1] = 1 if row[-1] == 'M' else 2
            b5.append(row)
    return b5
def fonk5():
    b5 = fonk4('data.csv')
    b7 = int(input('Enter number of neighbors to use: '))
    b8 = input('Enter data to be predicted (comma-separated): ')
    b9 = list(map(float, b8.split(',')))
    b10 = fonk2(b5, b9, b7)
    b11 = fonk3(b10)
    print('Nearest neighbors are:')
    for neighbor in b10:
        print(neighbor)
    b12 = 'M' if b11 == 1 else 'W'
    print(f'Prediction for b12 with given data is: {b12}')
if b13 = = "__main__":
    fonk5()