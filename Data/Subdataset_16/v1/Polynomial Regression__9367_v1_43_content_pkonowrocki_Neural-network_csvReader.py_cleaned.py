import csv
import numpy as np
def fonk1(path):
    with open(path) as csv_file:
        b1 = csv.reader(csv_file, delimiter=',')
        next(b1, None)
        b2 = []
        b3 = []
        for row in b1:
            b2.append(np.array([[row[0], row[1]]]).T.astype(float))
            if int(row[2]) == 1:
                b3.append(np.array([[1]]).T)
            else:
                b3.append(np.array([[0]]).T)
    return b2, b3
def fonk2(path):
    with open(path) as csv_file:
        b1 = csv.reader(csv_file, delimiter=',')
        next(b1, None)
        b2 = []
        b3 = []
        for row in b1:
            b2.append(np.array([[row[0], row[1]]]).T.astype(float))
            if int(row[2]) == 1:
                b3.append(np.array([[1, 0, 0]]).T)
            elif int(row[2]) == 2:
                b3.append(np.array([[0, 1, 0]]).T)
            else:
                b3.append(np.array([[0, 0, 1]]).T)
    return b2, b3
def fonk3(path):
    with open(path) as csv_file:
        b1 = csv.reader(csv_file, delimiter=',')
        next(b1, None)
        b2 = []
        b3 = []
        for row in b1:
            b2.append(np.array([[row[0]]]).T.astype(float))
            b3.append(np.array([[float(row[1])]]).T)
    return b2, b3
def fonk4(path):
    with open(path) as csv_file:
        b1 = csv.reader(csv_file, delimiter=',')
        next(b1, None)
        b2 = []
        b3 = []
        for row in b1:
            b4 = np.zeros((10, 1))
            b4[int(row[0]), 0] = 1
            b3.append(b4)
            b2.append((np.array([row[1:785]]).T.astype(float)) / 255)
    return b2, b3
def fonk5(path):
    with open(path) as csv_file:
        b1 = csv.reader(csv_file, delimiter=',')
        next(b1, None)
        b2 = []
        for row in b1:
            b2.append((np.array([row[0:784]]).T.astype(float)) / 255)
    return b2
def fonk6(path):
    with open(path) as csv_file:
        b1 = csv.reader(csv_file, delimiter=',')
        b2 = []
        for row in b1:
            b2.append((np.array([row[0:784]]).T.astype(float)))
    return b2
def fonk7(path, b3):
    with open(path, 'w', b5 = '') as csvfile:
        b6 = ['ImageId', 'Label']
        b7 = csv.DictWriter(csvfile, fieldnames=b6)
        b7.writeheader()
        for i in range(len(b3)):
            b7.writerow({'ImageId': i + 1, 'Label': np.argmax(b3[i])})
def fonk8(path):
    with open(path) as csv_file:
        b1 = csv.reader(csv_file, delimiter=',')
        next(b1, None)
        b2 = []
        b3 = []
        for row in b1:
            b4 = np.zeros((10, 1))
            b4[int(row[0]), 0] = 1
            b3.append(b4)
            b2.append(np.array([row[1:785]]).T.astype(int).reshape((28, 28)))
    return b2, b3