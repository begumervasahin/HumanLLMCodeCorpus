import csv
import math
import operator
def fonk1(b14):
    b1 = []
    try:
        with open(b14, b2 = 'r') as train_file:
            b3 = csv.reader(train_file)
            for rec in b3:
                b4 = [float(cols) if i != len(rec) - 1 else cols for i, cols in enumerate(rec)]
                b1.append(b4)
        print("Training b3 loaded")
    except IOError:
        print("File not available. Please check the filename")
        exit()
    return b1
def fonk2(train, b15):
    if any(len(rec) - 1 != len(b15) for rec in train):
        print("Dimensions of b15 and train do not match")
        return []
    b5 = []
    for rec in train:
        b6 = sum((b15[i] - rec[i]) ** 2 for i in range(len(b15)))
        b7 = round(math.sqrt(b6), 3)
        print(f"Distance between the b15 point and training b3 {train.index(rec) + 1}: {b7}")
        b5.append(b7)
    return b5
def fonk3(b1, b17, num_neighbors):
    b8 = sorted(range(len(b17)), key=lambda x: b17[x])
    b9 = b8[:num_neighbors]
    b10 = {}
    for n in b9:
        b11 = b1[n][-1]
        b10[b11] = b10.get(b11, 0) + 1
    b12 = sorted(b10.items(), key=operator.itemgetter(1), reverse=True)[0][0]
    print(b12)
    return b12
if b13 = = "__main__":
    print("Place the input dataset CSV file in the same directory as the Python module.")
    b14 = input("Enter the name of the training dataset CSV file: ")
    b1 = fonk1(b14)
    b15 = [float(x) for x in input("Enter the values separated by ',': ").split(",")]
    b16 = int(input("Enter the number of neighbors to consider: "))
    b17 = fonk2(b1, b15)
    if b17:
        fonk3(b1, b17, b16)