import numpy as np
from sklearn.model_selection import train_test_split
b1 = np.loadtxt(open('D:\\diabetes.csv'), delimiter=',', skiprows=1, encoding='utf8', dtype=float)
def fonk1(b1):
    b2 = np.mean(b1, axis=0)
    b3 = np.std(b1, axis=0)
    return b2[:-1], b3[:-1]
def fonk2(x, mean, std):
    b4 = np.exp(-(np.power(x - mean, 2)) / (2 * np.power(std, 2)))
    return (1 / (np.sqrt(2 * np.pi) * std)) * b4
def fonk3(test_data_point, b2, b3):
    b5 = [fonk2(test_data_point[i], b2[i], b3[i]) for i in range(len(b2))]
    return np.prod(b5)
def fonk4(train_data, test_data_point):
    b2, b3 = fonk1(train_data)
    b6 = fonk3(test_data_point[:-1], b2, b3)
    return b6
train_data, b7 = train_test_split(b1, test_size=0.10)
b8 = train_data[train_data[:, -1] == 1]
b9 = train_data[train_data[:, -1] == 0]
a1 = 0
for test_point in b7:
    b10 = fonk4(b8, test_point)
    b11 = fonk4(b9, test_point)
    b12 = 1 if b10 > b11 else 0
    if b12 = = test_point[-1]:
        a1 += 1
b13 = (a1 / len(b7)) * 100.0
print("Accuracy:", b13)