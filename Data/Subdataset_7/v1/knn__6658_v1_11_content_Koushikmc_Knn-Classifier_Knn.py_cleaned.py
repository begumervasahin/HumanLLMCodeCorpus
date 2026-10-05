import csv
import math
import operator
b1 = []
def fonk1(b12):
    try:
        with open(b12, 'r') as train:
            b2 = csv.reader(train)
            for rec in b2:
                b3 = [float(cols) for cols in rec[:-1]]
                b3.append(rec[-1])
                b1.append(b3)
        print("Training b2 loaded")
    except IOError:
        print("File not available. Please check the filename")
        exit()
def fonk2(train, b13):
    b4 = []
    for rec in train:
        if len(rec[:-1]) != len(b13):
            print("Dimensions of b13 and train do not match")
            break
        else:
            b5 = sum((x - y) ** 2 for x, y in zip(b13, rec[:-1]))
            b5 = round(math.sqrt(b5), 3)
            print("Distance between the b13 point and training b2 {}: {}".format(train.index(rec) + 1, b5))
            b4.append(b5)
    return b4
def fonk3(b5, num_of_neighbors):
    b6 = sorted(range(len(b5)), key=lambda x: b5[x])
    b7 = b6[:num_of_neighbors]
    b8 = {}
    for n in b7:
        b9 = b1[n][-1]
        b8[b9] = b8.get(b9, 0) + 1
    b10 = max(b8.items(), key=operator.itemgetter(1))[0]
    print("Predicted class:", b10)
if b11 = = "__main__":
    print("Place the input dataset CSV file in the same directory as the Python module")
    b12 = input("Enter the name of the training dataset CSV file: ")
    fonk1(b12)
    b13 = [float(x) for x in input("Enter the values separated by ',': ").split(",")]
    b14 = int(input("Enter the number of b7 to consider: "))
    b15 = fonk2(b1, b13)
    fonk3(b15, b14)