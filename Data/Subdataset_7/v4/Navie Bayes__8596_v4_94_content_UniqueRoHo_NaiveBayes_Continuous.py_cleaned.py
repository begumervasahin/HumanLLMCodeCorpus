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
    b7 = (1 / (np.sqrt(2 * np.pi) * stdev)) * b6
    return b7
def fonk3(b10, mean, std):
    a1 = 1
    for i in range(0, 8):
        a1 *= fonk2(b10[i], mean[i], std[i])
    return a1
def fonk4(train_data, b10):
    train_mean, train_std, b8 = fonk1(train_data)
    b9 = fonk3(b10, train_mean, train_std)
    return b9
train_data, b10 = train_test_split(b1, test_size=0.10)
b11 = [tip for tip in train_data if tip[-1] == 1.0]
b12 = [tip for tip in train_data if tip[-1] != 1.0]
a2 = 0
for test_instance in b10:
    b13 = fonk4(b11, test_instance)
    b14 = fonk4(b12, test_instance)
    if b13 > b14:
        a3 = 1
        if a3 = = test_instance[-1]:
            a2 += 1
    else:
        a3 = 0
        if a3 = = test_instance[-1]:
            a2 += 1
b15 = (a2 / float(len(b10))) * 100.0
print("Accuracy:", b15)