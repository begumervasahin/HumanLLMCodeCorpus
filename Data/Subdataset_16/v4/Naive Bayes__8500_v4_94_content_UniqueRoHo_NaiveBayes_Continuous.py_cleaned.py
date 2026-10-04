
import numpy as np
from sklearn.model_selection import train_test_split
b1 = np.loadtxt(open('D:\\diabetes.csv'), delimiter=',', skiprows=1, encoding='utf8', dtype=float)
def fonk1(b1):
    b2 = b1.shape[1] - 1
    b3 = []
    b4 = []
    for i in range(b2):
        b5 = b1[:, i]
        b3.append(np.mean(b5))
        b4.append(np.std(b5))
    return b3, b4, b2
def fonk2(x, mean, std):
    b6 = np.exp(-((x - mean) ** 2) / (2 * (std ** 2)))
    return (1 / (np.sqrt(2 * np.pi) * std)) * b6
def fonk3(b8, b3, b4):
    a1 = 1
    for i in range(len(b3)):
        a1 *= fonk2(b8[i], b3[i], b4[i])
    return a1
def fonk4(train_data, b8):
    b3, b4, b7 = fonk1(train_data)
    return fonk3(b8, b3, b4)
train_data, b8 = train_test_split(b1, test_size=0.10)
b9 = [row for row in train_data if row[-1] == 1.0]
b10 = [row for row in train_data if row[-1] == 0.0]
a2 = 0
for test_instance in b8:
    b11 = fonk4(b9, test_instance)
    b12 = fonk4(b10, test_instance)
    b13 = 1.0 if b11 > b12 else 0.0
    if b13 = = test_instance[-1]:
        a2 += 1
b14 = (a2 / float(len(b8))) * 100.0
print(f"Accuracy: {b14:.2f}%")