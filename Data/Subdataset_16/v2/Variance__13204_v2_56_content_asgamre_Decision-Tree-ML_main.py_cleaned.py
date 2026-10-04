import sys
import csv
import ID3
import Accuracy
from collections import defaultdict
def fonk1(filename):
    b1 = []
    b2 = []
    with open(filename, 'r') as csvfile:
        b3 = csv.reader(csvfile, delimiter=',')
        for b4, row in enumerate(b3):
            if b4 = = 0:
                b2 = row[:-1]
            else:
                b1.append([int(i) for i in row])
    b5 = list(range(len(b2)))
    b6 = list(range(len(b1)))
    b7 = [row[-1] for row in b1]
    return b1, b5, b6, b7, b2
def fonk2():
    b8 = "data_sets1/"
    b9 = int(sys.argv[1])
    b10 = int(sys.argv[2])
    b11 = b8 + sys.argv[3]
    b12 = b8 + sys.argv[4]
    b13 = b8 + sys.argv[5]
    b14 = str(sys.argv[6])
    b15 = ID3.DTree(b11)
    if b14.lower() == "yes":
        print("Decision Tree before Pruning:")
        print(b15)
    b16 = Accuracy.Accuracy(b13)
    b16.calculateAccuracy(b15.root)
    print("Accuracy before Pruning:")
    b16.displayAccuracy()
    b15.pruneTree(b9, b10, b12)
    if b14.lower() == "yes":
        print("Decision Tree after Pruning:")
        print(b15)
    b16.calculateAccuracy(b15.root)
    print("Accuracy after Pruning:")
    b16.displayAccuracy()
if b17 = = '__main__':
    fonk2()