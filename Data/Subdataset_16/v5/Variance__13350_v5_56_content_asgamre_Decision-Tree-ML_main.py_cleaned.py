import sys
import csv
from collections import defaultdict
import ID3
import Node
import Accuracy
def fonk1(filename):
    b1 = []
    with open(filename, 'r') as csvfile:
        b2 = csv.reader(csvfile, delimiter=',')
        b3 = next(b2)[:-1]
        for row in b2:
            b1.append([int(i) for i in row])
    b4 = list(range(len(b3)))
    b5 = [row[-1] for row in b1]
    return b3, b1, b4, b5
def fonk2():
    b6 = int(sys.argv[1])
    b7 = int(sys.argv[2])
    b8 = "data_sets1/"
    b9 = b8 + sys.argv[3]
    b10 = b8 + sys.argv[4]
    b11 = b8 + sys.argv[5]
    b12 = sys.argv[6].lower() == 'yes'
    b13 = ID3.DTree(b9)
    if b12:
        print("Decision Tree before Pruning:")
        print(b13)
    b14 = Accuracy.Accuracy(b11)
    b14.calculateAccuracy(b13.root)
    print("Accuracy before Pruning:")
    b14.displayAccuracy()
    b13.pruneTree(b6, b7, b10)
    if b12:
        print("Decision Tree after Pruning:")
        print(b13)
    b14.calculateAccuracy(b13.root)
    print("Accuracy after Pruning:")
    b14.displayAccuracy()
if b15 = = '__main__':
    fonk2()