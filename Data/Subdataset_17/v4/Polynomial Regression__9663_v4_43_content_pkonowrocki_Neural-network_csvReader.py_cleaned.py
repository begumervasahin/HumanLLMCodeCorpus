import csv
import numpy as np
def read_classification_file(path):
    X, Y = [], []
    with open(path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader, None)
        for row in csv_reader:
            X.append(np.array([[row[0], row[1]]]).T.astype(np.float))
            Y.append(np.array([[1]]).T if int(row[2]) == 1 else np.array([[0]]).T)
    return X, Y
def read_classification_3_classes_file(path):
    X, Y = [], []
    with open(path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader, None)
        for row in csv_reader:
            X.append(np.array([[row[0], row[1]]]).T.astype(np.float))
            if int(row[2]) == 1:
                Y.append(np.array([[1, 0, 0]]).T)
            elif int(row[2]) == 2:
                Y.append(np.array([[0, 1, 0]]).T)
            else:
                Y.append(np.array([[0, 0, 1]]).T)
    return X, Y
def read_regression_file(path):
    X, Y = [], []
    with open(path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader, None)
        for row in csv_reader:
            X.append(np.array([[row[0]]]).T.astype(np.float))
            Y.append(np.array([[float(row[1])]]).T)
    return X, Y
def read_mnist_as_one_line_training(path):
    X, Y = [], []
    with open(path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader, None)
        for row in csv_reader:
            y = np.zeros((10, 1))
            y[int(row[0]), 0] = 1
            Y.append(y)
            X.append(np.array([row[1:785]]).T.astype(float) / 255)
    return X, Y
def read_mnist_as_one_line_test(path):
    X = []
    with open(path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader, None)
        for row in csv_reader:
            X.append(np.array([row[0:784]]).T.astype(float) / 255)
    return X
def read_mnist_as_one_line_pca(path):
    X = []
    with open(path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            X.append(np.array([row[0:784]]).T.astype(float))
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
        next(csv_reader, None)
        for row in csv_reader:
            y = np.zeros((10, 1))
            y[int(row[0]), 0] = 1
            Y.append(y)
            X.append(np.array([row[1:785]]).T.astype(int).reshape((28, 28)))
    return X, Y