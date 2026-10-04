import csv
import math
import operator
b1 = []
def fonk1(b11):
    try:
        with open(b11) as train_file:
            b2 = csv.b2(train_file)
            for row in b2:
                b3 = []
                for index, value in enumerate(row):
                    if index != len(row) - 1:
                        b3.append(float(value))
                    else:
                        b3.append(value)
                b1.append(b3)
        print("Training data loaded successfully.")
    except IOError:
        print("File not available. Please check the filename.")
        exit()
def fonk2(train_set, b13):
    b4 = []
    for train_instance in train_set:
        if len(train_instance) - 1 != len(b13):
            print("Dimensions of test and training data do not match.")
            break
        else:
            b5 = math.sqrt(sum((b13[i] - train_instance[i]) ** 2 for i in range(len(b13))))
        print(f"Distance between the test point and training data {train_set.index(train_instance) + 1}: {round(b5, 3)}")
        b4.append(round(b5, 3))
    return b4
def fonk3(b4, num_neighbors):
    b6 = sorted(range(len(b4)), key=lambda i: b4[i])[:num_neighbors]
    b7 = {}
    for index in b6:
        b8 = b1[index][-1]
        b7[b8] = b7.get(b8, 0) + 1
    b9 = max(b7.items(), key=operator.itemgetter(1))[0]
    print(b9)
if b10 = = "__main__":
    print("Place the input dataset CSV file in the same directory as this Python module.")
    b11 = input("Enter the name of the training dataset CSV file: ")
    fonk1(b11)
    b12 = input("Enter the test values separated by commas: ")
    b13 = [float(value) for value in b12.split(",")]
    b14 = int(input("Enter the number of neighbors to consider: "))
    b4 = fonk2(b1, b13)
    fonk3(b4, b14)