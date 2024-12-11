import csv
import math
import operator
def fonk1(set1, set2, b2):
    a1 = 0
    for x in range(b2):
        a1 += pow((set1[x] - set2[x]), 2)
    return math.sqrt(a1)
def fonk2(b10, b12, b11):
    b1 = []
    b2 = len(b12)
    for x in range(len(b10)):
        b3 = fonk1(b12, b10[x], b2)
        b1.append((b10[x], b3))
    b1.sort(b4 = operator.itemgetter(1))
    b5 = []
    for x in range(b11):
        b5.append(b1[x][0])
    return b5
def fonk3(neighbors):
    b6 = {}
    for x in range(len(neighbors)):
        b7 = neighbors[x][-1]
        if b7 in b6:
            b6[b7] += 1
        else:
            b6[b7] = 1
    b8 = sorted(b6.items(), b4=operator.itemgetter(1), reverse=True)
    return b8[0][0]
def fonk4():
    with open('data.csv', 'r') as csvfile:
        b9 = csv.reader(csvfile)
        b10 = [list(map(float, row)) for row in b9]
    b11 = int(input('Enter the number of neighbors to consider: '))
    b12 = [float(x) for x in input('Enter data to be predicted (separated by spaces): ').split()]
    b13 = fonk2(b10, b12, b11)
    b14 = fonk3(b13)
    print('Nearest neighbors are:')
    print(b13)
    print('Predicted class class1 on given data is:')
    if b14 = = 1:
        print('M')
    else:
        print('W')
if b15 = = "__main__":
    fonk4()