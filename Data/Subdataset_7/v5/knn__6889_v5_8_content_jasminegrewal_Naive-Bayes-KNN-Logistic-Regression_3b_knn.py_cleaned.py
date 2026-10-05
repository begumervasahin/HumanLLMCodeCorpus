import csv
import math
import operator
def fonk1(point1, point2):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(point1, point2)))
def fonk2(b8, sample, b9):
    b1 = [(data, fonk1(sample, data[:-1])) for data in b8]
    b1.sort(b2 = operator.itemgetter(1))
    b3 = [data for data, _ in b1[:b9]]
    return b3
def fonk3(neighbors):
    b4 = {}
    for neighbor in neighbors:
        b5 = neighbor[-1]
        b4[b5] = b4.get(b5, 0) + 1
    b6 = sorted(b4.items(), b2=operator.itemgetter(1), reverse=True)
    return b6[0][0]
def fonk4(data):
    for entry in data:
        entry[2] = 1 if entry[2] == 'M' else 0
        entry[:2] = map(float, entry[:2])
    return data
def fonk5():
    with open('data.csv', 'r') as csvfile:
        b7 = csv.reader(csvfile)
        b8 = fonk4(list(b7))
    b9 = int(input('Enter the number of neighbors to use: '))
    b10 = list(map(float, input('Enter the data to be predicted: ').split()))
    b3 = fonk2(b8, b10, b9)
    b11 = fonk3(b3)
    print('Nearest neighbors are:')
    for neighbor in b3:
        print(neighbor)
    print('Prediction for gender with given data is:')
    print('Male' if b11 = = 1 else 'Female')
if b12 = = '__main__':
    fonk5()