import csv
import numpy as np
def read_classification_file(path):
    X, Y = [], []
    with open(path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)
        for row in csv_reader:
            features = np.array([[row[0], row[1]]], dtype=float).T
            label = np.array([[1]], dtype=int).T if int(row[2]) == 1 else np.array([[0]], dtype=int).T
            X.append(features)
            Y.append(label)
    return X, Y
def read_classification_3_classes_file(path):
    X, Y = [], []
    with open(path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)
        for row in csv_reader:
            features = np.array([[row[0], row[1]]], dtype=float).T
            if int(row[2]) == 1:
                label = np.array([[1, 0, 0]], dtype=int).T
            elif int(row[2]) == 2:
                label = np.array([[0, 1, 0]], dtype=int).T
            else:
                label = np.array([[0, 0, 1]], dtype=int).T
            X.append(features)
            Y.append(label)
    return X, Y
def read_regression_file(path):
    X, Y = [], []
    with open(path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)
        for row in csv_reader:
            feature = np.array([[row[0]]], dtype=float).T
            target = np.array([[float(row[1])]], dtype=float).T
            X.append(feature)
            Y.append(target)
    return X, Y
def read_mnist_as_one_line_training(path):
    X, Y = [], []
    with open(path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)
        for row in csv_reader:
            label = np.zeros((10, 1), dtype=int)
            label[int(row[0]), 0] = 1
            features = np.array([row[1:785]], dtype=float).T / 255
            Y.append(label)
            X.append(features)
    return X, Y
def read_mnist_as_one_line_test(path):
    X = []
    with open(path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)
        for row in csv_reader:
            features = np.array([row[0:784]], dtype=float).T / 255
            X.append(features)
    return X
def read_mnist_as_one_line_pca(path):
    X = []
    with open(path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            features = np.array([row[0:784]], dtype=float)
            X.append(features)
    return X
def save_mnist_result(path, Y):
    with open(path, 'w', newline='') as csvfile:
        fieldnames = ['ImageId', 'Label']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for i, label in enumerate(Y):
            writer.writerow({'ImageId': i + 1, 'Label': np.argmax(label)})
def read_mnist_as_picture_training(path):
    X, Y = [], []
    with open(path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)
        for row in csv_reader:
            label = np.zeros((10, 1), dtype=int)
            label[int(row[0]), 0] = 1
            features = np.array([row[1:785]], dtype=int).T.reshape((28, 28))
            Y.append(label)
            X.append(features)
    return X, Y