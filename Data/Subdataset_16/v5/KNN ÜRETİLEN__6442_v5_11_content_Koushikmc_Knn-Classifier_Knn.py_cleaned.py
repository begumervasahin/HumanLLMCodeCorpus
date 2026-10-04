import csv
import math
import operator
def fonk1(b13):
    b1 = []
    try:
        with open(b13, b2 = 'r') as train_file:
            b3 = csv.reader(train_file)
            for rec in b3:
                b4 = [float(cols) if i != len(rec) - 1 else cols for i, cols in enumerate(rec)]
                b1.append(b4)
        print("Training b3 loaded")
    except IOError:
        print("File not available. Please check the filename")
        exit()
    return b1
def fonk2(train, b14):
    if any(len(rec) - 1 != len(b14) for rec in train):
        print("Dimensions of b14 and train do not match")
        return []
    b5 = []
    for idx, rec in enumerate(train):
        b6 = sum((b14[i] - rec[i]) ** 2 for i in range(len(b14)))
        b7 = round(math.sqrt(b6), 3)
        print(f"Distance between the b14 point and training b3 {idx + 1}: {b7}")
        b5.append(b7)
    return b5
def fonk3(b1, b16, num_neighbors):
    b8 = sorted(range(len(b16)), key=lambda x: b16[x])
    b9 = b8[:num_neighbors]
    b10 = {}
    for n in b9:
        b11 = b1[n][-1]
        b10[b11] = b10.get(b11, 0) + 1
    b12 = sorted(b10.items(), key=operator.itemgetter(1), reverse=True)[0][0]
    print(f"Predicted class: {b12}")
    return b12
def fonk4():
    print("Place the input dataset CSV file in the same directory as the Python module.")
    b13 = input("Enter the name of the training dataset CSV file: ")
    b1 = fonk1(b13)
    b14 = [float(x) for x in input("Enter the values separated by ',': ").split(",")]
    b15 = int(input("Enter the number of neighbors to consider: "))
    b16 = fonk2(b1, b14)
    if b16:
        fonk3(b1, b16, b15)
if b17 = = "__main__":
    fonk4()