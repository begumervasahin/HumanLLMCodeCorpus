import ID3
import sys
import Node
import Accuracy
import csv
from collections import defaultdict
def fonk1():
    b1 = "data_sets1/"
    b2 = int(sys.argv[1])
    b3 = int(sys.argv[2])
    b4 = str(sys.argv[2]) ;
    b5 = str(sys.argv[3]);
    b4 = b1 + sys.argv[3]
    b6 = b1 + sys.argv[4]
    b5 = b1 + sys.argv[5]
    b7 = str(sys.argv[6])
    b8 = ID3.DTree(b4)
    if b7 = = "yes":
        print "Decision Tree before Pruning:"
        print b8
    b9 = Accuracy.Accuracy(b5)
    b9.calculateAccuracy(b8.root)
    print "Accuracy before Pruning:"
    b9.displayAccuracy()
    b8.pruneTree(b2, b3, b6)
    if b7 = = "yes":
        print "Decision Tree after Pruning:"
        print b8
    b9.calculateAccuracy(b8.root)
    print "Accuracy after Pruning:"
    b9.displayAccuracy()
def fonk2(self, filename):
    self.b10 = []
    with open(filename,'rb') as csvfile:
        b11 = csv.reader(csvfile, delimiter = ',')
        a1 = 0
        for row in b11:
            if a1 = = 0:
                self.b12 = row[:-1]
            else:
                self.b10.append([int(i) for i in row])
            a1 += 1
    self.b13 = range(len(self.b12))
    self.b14 = range(len(self.b10))
    self.b15 = [row[-1] for row in self.b10]
    return self
if b16 = = '__main__':
    fonk1()