import csv
import math
import operator
b1 = []
def fonk1(b10):
    try:
        with open(b10) as train:
            b2 = csv.reader(train)
            for rec in b2:
                b3 = []
                for cols in rec:
                    if rec.index(cols) != len(rec) - 1:
                        b3.append(float(cols))
                    else:
                        b3.append(cols)
                b1.append(b3)
        print("Training b2 loaded")
    except IOError:
        print("File not available. Please check the filename")
        exit()
def fonk2(train, b11):
    b4 = []
    for rec in train:
        if len(rec[0:len(rec)-1]) != len(b11):
            print("Dimensions of b11 and train do not match")
            break
        else:
            a1 = 0
            for i in range(0, len(b11)):
                a1 += (b11[i] - rec[i]) ** 2
        print(f"Distance between the b11 point and training b2 {train.index(rec) + 1}: {round(math.sqrt(a1), 3)}")
        b4.append(round(math.sqrt(a1), 3))
    return b4
def fonk3(a1, numofneighbors):
    b5 = sorted(range(len(a1)), key=lambda x: a1[x])
    b6 = b5[:numofneighbors]
    b7 = {}
    for n in b6:
        if b1[n][-1] in b7:
            b7[b1[n][-1]] += 1
        else:
            b7.update({b1[n][-1]: 1})
    b8 = sorted(b7.items(), key=operator.itemgetter(1), reverse=True)[0][0]
    print(b8)
if b9 = = "__main__":
    print("Place the input dataset csv file in the same directory of the python module")
    b10 = input("Enter the name of the training dataset csv file: ")
    fonk1(b10)
    b11 = [float(x) for x in input("Enter the values separated by ',': ").split(",")]
    b12 = int(input("Enter the number of b6 to consider: "))
    b13 = fonk2(b1, b11)
    fonk3(b13, b12)