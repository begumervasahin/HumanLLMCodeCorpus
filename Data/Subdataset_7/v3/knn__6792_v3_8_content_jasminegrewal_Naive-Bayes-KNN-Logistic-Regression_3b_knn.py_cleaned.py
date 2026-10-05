import csv
import math
import operator
def fonk1(set1, set2):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(set1, set2)))
def fonk2(b6, b8, b7):
    b1 = [(train_sample, fonk1(b8, train_sample[:-1])) for train_sample in b6]
    b1.sort(b2 = operator.itemgetter(1))
    return [distance[0] for distance in b1[:b7]]
def fonk3(neighbors):
    b3 = {}
    for neighbor in neighbors:
        b4 = neighbor[-1]
        b3[b4] = b3.get(b4, 0) + 1
    return max(b3.items(), b2 = operator.itemgetter(1))[0]
def fonk4():
    with open('data.csv', 'r') as csvfile:
        b5 = csv.reader(csvfile)
        b6 = [list(map(float, row)) for row in b5]
    b7 = int(input('Enter the number of neighbors to consider: '))
    b8 = [float(x) for x in input('Enter data to be predicted (separated by spaces): ').split()]
    b9 = fonk2(b6, b8, b7)
    b10 = fonk3(b9)
    print('Nearest neighbors are:')
    print(b9)
    print('Predicted class class1 on given data is:', 'M' if b10 = = 1 else 'W')
if b11 = = "__main__":
    fonk4()