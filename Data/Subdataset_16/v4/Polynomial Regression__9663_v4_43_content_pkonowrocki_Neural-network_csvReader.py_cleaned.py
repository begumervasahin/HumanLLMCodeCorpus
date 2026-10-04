import csv
import numpy as np
def fonk1(path):
    b4, b1 = [], []
    with open(path) as csv_file:
        b2 = csv.reader(csv_file, delimiter=',')
        next(b2, None)
        for row in b2:
            b4.append(np.array([[row[0], row[1]]]).T.astype(np.float))
            b1.append(np.array([[1]]).T if int(row[2]) == 1 else np.array([[0]]).T)
    return b4, b1
def fonk2(path):
    b4, b1 = [], []
    with open(path) as csv_file:
        b2 = csv.reader(csv_file, delimiter=',')
        next(b2, None)
        for row in b2:
            b4.append(np.array([[row[0], row[1]]]).T.astype(np.float))
            if int(row[2]) == 1:
                b1.append(np.array([[1, 0, 0]]).T)
            elif int(row[2]) == 2:
                b1.append(np.array([[0, 1, 0]]).T)
            else:
                b1.append(np.array([[0, 0, 1]]).T)
    return b4, b1
def fonk3(path):
    b4, b1 = [], []
    with open(path) as csv_file:
        b2 = csv.reader(csv_file, delimiter=',')
        next(b2, None)
        for row in b2:
            b4.append(np.array([[row[0]]]).T.astype(np.float))
            b1.append(np.array([[float(row[1])]]).T)
    return b4, b1
def fonk4(path):
    b4, b1 = [], []
    with open(path) as csv_file:
        b2 = csv.reader(csv_file, delimiter=',')
        next(b2, None)
        for row in b2:
            b3 = np.zeros((10, 1))
            b3[int(row[0]), 0] = 1
            b1.append(b3)
            b4.append(np.array([row[1:785]]).T.astype(float) / 255)
    return b4, b1
def fonk5(path):
    b4 = []
    with open(path) as csv_file:
        b2 = csv.reader(csv_file, delimiter=',')
        next(b2, None)
        for row in b2:
            b4.append(np.array([row[0:784]]).T.astype(float) / 255)
    return b4
def fonk6(path):
    b4 = []
    with open(path) as csv_file:
        b2 = csv.reader(csv_file, delimiter=',')
        for row in b2:
            b4.append(np.array([row[0:784]]).T.astype(float))
    return b4
def fonk7(path, b1):
    with open(path, 'w', b5 = '') as csvfile:
        b6 = ['ImageId', 'Label']
        b7 = csv.DictWriter(csvfile, b6=b6)
        b7.writeheader()
        for i, label in enumerate(b1):
            b7.writerow({'ImageId': i + 1, 'Label': np.argmax(label)})
def fonk8(path):
    b4, b1 = [], []
    with open(path) as csv_file:
        b2 = csv.reader(csv_file, delimiter=',')
        next(b2, None)
        for row in b2:
            b3 = np.zeros((10, 1))
            b3[int(row[0]), 0] = 1
            b1.append(b3)
            b4.append(np.array([row[1:785]]).T.astype(int).reshape((28, 28)))
    return b4, b1