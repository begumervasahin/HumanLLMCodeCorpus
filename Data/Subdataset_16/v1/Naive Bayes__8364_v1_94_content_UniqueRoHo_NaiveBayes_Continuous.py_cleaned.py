
import numpy as np
from sklearn.model_selection import train_test_split
def fonk1(filepath):
    return np.loadtxt(open(filepath), b1 = ',', skiprows=1, dtype=float)
def fonk2(b9):
    b2 = b9.shape[1] - 1
    b3 = []
    b4 = []
    for i in range(b2):
        b5 = b9[:, i]
        b3.append(np.mean(b5))
        b4.append(np.std(b5))
    return b3, b4, b2
def fonk3(x, mean, std):
    b6 = np.exp(-(np.power(x - mean, 2)) / (2 * np.power(std, 2)))
    return (1 / (np.sqrt(2 * np.pi) * std)) * b6
def fonk4(b10, b3, b4):
    a1 = 1
    for i in range(len(b3)):
        a1 *= fonk3(b10[i], b3[i], b4[i])
    return a1
def fonk5(train_data, b10):
    b3, b4, b7 = fonk2(train_data)
    return fonk4(b10, b3, b4)
def fonk6():
    b8 = 'D:\\diabetes.csv'
    b9 = fonk1(b8)
    train_data, b10 = train_test_split(b9, test_size=0.10)
    b11 = train_data[train_data[:, -1] == 1.0]
    b12 = train_data[train_data[:, -1] == 0.0]
    a2 = 0
    for test_instance in b10:
        b13 = fonk5(b11, test_instance)
        b14 = fonk5(b12, test_instance)
        b15 = 1 if b13 > b14 else 0
        if b15 = = test_instance[-1]:
            a2 += 1
    b16 = (a2 / len(b10)) * 100.0
    print(f'Accuracy: {b16:.2f}%')
if b17 = = "__main__":
    fonk6()