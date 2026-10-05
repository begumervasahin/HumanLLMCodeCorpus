import csv
import math
import operator
b1 = []
def fonk1(b12):
    try:
        with open(b12, 'r') as train_file:
            b2 = csv.reader(train_file)
            for row in b2:
                b3 = [float(value) for value in row[:-1]]
                b3.append(row[-1])
                b1.append(b3)
        print("Training data loaded")
    except IOError:
        print("File not available. Please check the filename")
        exit()
def fonk2(train_data, test_data):
    b4 = []
    for record in train_data:
        if len(record[:-1]) != len(test_data):
            print("Dimensions of test and train do not match")
            break
        else:
            b5 = sum((x - y) ** 2 for x, y in zip(test_data, record[:-1]))
            b5 = round(math.sqrt(b5), 3)
            print("Distance between the test point and training data {}: {}".format(train_data.index(record) + 1,
                                                                                     b5))
            b4.append(b5)
    return b4
def fonk3(b15, num_of_neighbors):
    b6 = sorted(range(len(b15)), key=lambda x: b15[x])
    b7 = b6[:num_of_neighbors]
    b8 = {}
    for neighbor_index in b7:
        b9 = b1[neighbor_index][-1]
        b8[b9] = b8.get(b9, 0) + 1
    b10 = max(b8.items(), key=operator.itemgetter(1))[0]
    print("Predicted class:", b10)
if b11 = = "__main__":
    print("Place the input dataset CSV file in the same directory as the Python module")
    b12 = input("Enter the name of the training dataset CSV file: ")
    fonk1(b12)
    b13 = [float(value) for value in input("Enter the values separated by ',': ").split(",")]
    b14 = int(input("Enter the number of b7 to consider: "))
    b15 = fonk2(b1, b13)
    fonk3(b15, b14)