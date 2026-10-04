import sys
import csv
import ID3
import Accuracy
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
def fonk2(b16, b14, description):
    b8 = Accuracy.Accuracy(b14)
    b8.calculateAccuracy(b16.root)
    print(f"Accuracy {description}:")
    b8.displayAccuracy()
def fonk3():
    b9 = "data_sets1/"
    b10 = int(sys.argv[1])
    b11 = int(sys.argv[2])
    b12 = b9 + sys.argv[3]
    b13 = b9 + sys.argv[4]
    b14 = b9 + sys.argv[5]
    b15 = str(sys.argv[6]).lower()
    b16 = ID3.DTree(b12)
    if b15 = = "yes":
        print("Decision Tree before Pruning:")
        print(b16)
    fonk2(b16, b14, "before Pruning")
    b16.pruneTree(b10, b11, b13)
    if b15 = = "yes":
        print("Decision Tree after Pruning:")
        print(b16)
    fonk2(b16, b14, "after Pruning")
if b17 = = '__main__':
    fonk3()