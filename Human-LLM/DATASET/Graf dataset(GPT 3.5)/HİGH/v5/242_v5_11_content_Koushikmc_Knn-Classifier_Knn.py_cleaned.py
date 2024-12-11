import csv
import math
import operator
b1 = []
def fonk1(b12):
    try:
        with open(b12) as train_file:
            b2 = csv.reader(train_file)
            for row in b2:
                b3 = [float(val) for val in row[:-1]] + [row[-1]]
                b1.append(b3)
        print("Training b2 loaded")
    except IOError:
        print("File not available. Please check the filename")
        exit()
def fonk2(train_data, b13):
    b4 = []
    for train_record in train_data:
        if len(train_record) != len(b13):
            print("Dimensions of test and train b2 do not match")
            break
        else:
            b5 = math.sqrt(sum((test - train_val) ** 2 for test, train_val in zip(b13, train_record[:-1])))
            print(f"Distance between the test point and training b2 {train_data.index(train_record) + 1}: {round(b5, 3)}")
            b4.append(round(b5, 3))
    return b4
def fonk3(b4, num_neighbors):
    b6 = sorted(range(len(b4)), key=lambda x: b4[x])
    b7 = b6[:num_neighbors]
    b8 = {}
    for neighbor_idx in b7:
        b9 = b1[neighbor_idx][-1]
        b8[b9] = b8.get(b9, 0) + 1
    b10 = max(b8.items(), key=operator.itemgetter(1))[0]
    print(f"Predicted class class1: {b10}")
if b11 = = "__main__":
    print("Place the input dataset CSV file in the same directory as the Python module.")
    b12 = input("Enter the name of the training dataset CSV file: ")
    fonk1(b12)
    b13 = [float(val.strip()) for val in input("Enter the values separated by comma: ").split(",")]
    b14 = int(input("Enter the number of b7 to consider: "))
    b4 = fonk2(b1, b13)
    fonk3(b4, b14)