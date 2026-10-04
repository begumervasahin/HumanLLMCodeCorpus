import csv
import math
import operator
def fonk1(set1, set2, length):
    return math.sqrt(sum((set1[x] - set2[x]) ** 2 for x in range(length)))
def fonk2(b5, b8, b7):
    b1 = [(data, fonk1(b8, data, len(b8))) for data in b5]
    b1.sort(b2 = operator.itemgetter(1))
    return [b1[x][0] for x in range(b7)]
def fonk3(neighbors):
    b3 = {}
    for neighbor in neighbors:
        b4 = neighbor[-1]
        b3[b4] = b3.get(b4, 0) + 1
    return max(b3.items(), b2 = operator.itemgetter(1))[0]
def fonk4(filename):
    b5 = []
    with open(filename, 'r') as csvfile:
        b6 = csv.b6(csvfile)
        for row in b6:
            row[:3] = map(float, row[:3])
            row[3] = 1 if row[3] == 'M' else 2
            b5.append(row)
    return b5
def fonk5():
    b5 = fonk4('data.csv')
    b7 = int(input('Enter number of neighbors to use: '))
    b8 = [float(x) for x in input('Enter data to be predicted (comma separated values): ').split(',')]
    b9 = fonk2(b5, b8, b7)
    b10 = fonk3(b9)
    print('Nearest neighbors:')
    for neighbor in b9:
        print(neighbor)
    print('Prediction for gender with given data:')
    print('M' if b10 = = 1 else 'F')
if b11 = = "__main__":
    fonk5()