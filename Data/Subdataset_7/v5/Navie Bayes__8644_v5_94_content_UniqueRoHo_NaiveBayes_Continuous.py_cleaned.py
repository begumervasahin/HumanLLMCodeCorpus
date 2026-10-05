import numpy as np
from sklearn.model_selection import train_test_split
b1 = np.loadtxt(open('D:\\diabetes.csv'), delimiter=',', skiprows=1, encoding='utf8', dtype=float)
def fonk1(b1):
    b2 = np.mean(b1, axis=0)
    b3 = np.std(b1, axis=0)
    return b2[:-1], b3[:-1]
def fonk2(x, mean, stdev):
    b4 = np.exp(-(np.power(x - mean, 2)) / (2 * np.power(stdev, 2)))
    return (1 / (np.sqrt(2 * np.pi) * stdev)) * b4
def fonk3(b8, b2, b3):
    a1 = 1
    for i in range(len(b8) - 1):
        a1 *= fonk2(b8[i], b2[i], b3[i])
    return a1
def fonk4(train_data, b8):
    train_means, b5 = fonk1(train_data)
    b6 = fonk3(b8, train_means, b5)
    b7 = fonk3(b8, train_means, b5)
    return 1 if b6 > b7 else 0
train_data, b8 = train_test_split(b1, test_size=0.10)
b9 = sum(1 for test_instance in b8 if fonk4(train_data, test_instance) == int(test_instance[-1]))
b10 = (b9 / len(b8)) * 100.0
print("Accuracy:", b10)