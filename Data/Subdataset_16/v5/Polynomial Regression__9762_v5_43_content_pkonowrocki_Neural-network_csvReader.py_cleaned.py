import csv
import numpy as np
def fonk1(path):
    b7, b1 = [], []
    with open(path) as csv_file:
        b2 = csv.reader(csv_file, delimiter=',')
        next(b2, None)
        for row in b2:
            b3 = np.array([[row[0], row[1]]], dtype=float).T
            b4 = np.array([[1]] if int(row[2]) == 1 else [[0]], dtype=int).T
            b7.append(b3)
            b1.append(b4)
    return b7, b1
def fonk2(path):
    b7, b1 = [], []
    with open(path) as csv_file:
        b2 = csv.reader(csv_file, delimiter=',')
        next(b2, None)
        for row in b2:
            b3 = np.array([[row[0], row[1]]], dtype=float).T
            b5 = int(row[2])
            if b5 = = 1:
                b4 = np.array([[1, 0, 0]], dtype=int).T
            elif b5 = = 2:
                b4 = np.array([[0, 1, 0]], dtype=int).T
            else:
                b4 = np.array([[0, 0, 1]], dtype=int).T
            b7.append(b3)
            b1.append(b4)
    return b7, b1
def fonk3(path):
    b7, b1 = [], []
    with open(path) as csv_file:
        b2 = csv.reader(csv_file, delimiter=',')
        next(b2, None)
        for row in b2:
            b3 = np.array([[row[0]]], dtype=float).T
            b6 = np.array([[float(row[1])]], dtype=float).T
            b7.append(b3)
            b1.append(b6)
    return b7, b1
def fonk4(path):
    b7, b1 = [], []
    with open(path) as csv_file:
        b2 = csv.reader(csv_file, delimiter=',')
        next(b2, None)
        for row in b2:
            b4 = np.zeros((10, 1), dtype=int)
            b4[int(row[0]), 0] = 1
            b3 = np.array(row[1:785], dtype=float).reshape(-1, 1) / 255
            b7.append(b3)
            b1.append(b4)
    return b7, b1
def fonk5(path):
    b7 = []
    with open(path) as csv_file:
        b2 = csv.reader(csv_file, delimiter=',')
        next(b2, None)
        for row in b2:
            b3 = np.array(row[0:784], dtype=float).reshape(-1, 1) / 255
            b7.append(b3)
    return b7
def fonk6(path):
    b7 = []
    with open(path) as csv_file:
        b2 = csv.reader(csv_file, delimiter=',')
        for row in b2:
            b3 = np.array(row[0:784], dtype=float).reshape(-1, 1)
            b7.append(b3)
    return b7
def fonk7(path, b1):
    with open(path, 'w', b8 = '') as csvfile:
        b9 = ['ImageId', 'Label']
        b10 = csv.DictWriter(csvfile, b9=b9)
        b10.writeheader()
        for i, b4 in enumerate(b1):
            b10.writerow({'ImageId': i + 1, 'Label': np.argmax(b4)})
def fonk8(path):
    b7, b1 = [], []
    with open(path) as csv_file:
        b2 = csv.reader(csv_file, delimiter=',')
        next(b2, None)
        for row in b2:
            b4 = np.zeros((10, 1), dtype=int)
            b4[int(row[0]), 0] = 1
            b3 = np.array(row[1:785], dtype=int).reshape(28, 28)
            b7.append(b3)
            b1.append(b4)
    return b7, b1