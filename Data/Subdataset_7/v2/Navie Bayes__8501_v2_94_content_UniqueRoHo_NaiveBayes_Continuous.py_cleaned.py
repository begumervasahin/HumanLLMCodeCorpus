import numpy as np
from sklearn.model_selection import train_test_split
b1 = np.loadtxt(open('D:\\diabetes.csv'), delimiter=',', skiprows=1, encoding='utf8', dtype=float)
def fonk1(b1):
    b2 = len(b1[0]) - 1
    b3 = []
    b4 = []
    for i in range(b2):
        b5 = [row[i] for row in b1]
        b3.append(np.mean(b5))
        b4.append(np.std(b5))
    return b3, b4, b2
def fonk2(x, mean, stdev):
    b6 = np.exp(-(np.power(x - mean, 2)) / (2 * np.power(stdev, 2)))
    return (1 / (np.sqrt(2 * np.pi) * stdev)) * b6
def fonk3(test_data_point, mean, std):
    a1 = 1
    for i in range(0, 8):
        a1 *= fonk2(test_data_point[i], mean[i], std[i])
    return a1
def fonk4(train_data, test_data_point):
    train_mean, train_std, b7 = fonk1(train_data)
    a1 = fonk3(test_data_point, train_mean, train_std)
    return a1
train_data, b8 = train_test_split(b1, test_size=0.10)
b9 = [row for row in train_data if row[-1] == 1.0]
b10 = [row for row in train_data if row[-1] == 0.0]
a2 = 0
for test_point in b8:
    b11 = fonk4(b9, test_point)
    b12 = fonk4(b10, test_point)
    b13 = 1 if b11 > b12 else 0
    if b13 = = test_point[-1]:
        a2 += 1
b14 = (a2 / float(len(b8))) * 100.0
print("Accuracy:", b14)