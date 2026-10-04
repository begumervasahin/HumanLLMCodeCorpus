
import numpy as np
from sklearn.model_selection import train_test_split
b1 = 'D:\\diabetes.csv'
b2 = np.loadtxt(open(b1), delimiter=',', skiprows=1, encoding='utf8', dtype=float)
def fonk1(b2):
    b3 = b2.shape[1] - 1
    b4 = [np.mean(b2[:, i]) for i in range(b3)]
    b5 = [np.std(b2[:, i]) for i in range(b3)]
    return b4, b5, b3
def fonk2(x, mean, std):
    b6 = np.exp(-((x - mean) ** 2) / (2 * (std ** 2)))
    return (1 / (np.sqrt(2 * np.pi) * std)) * b6
def fonk3(b8, b4, b5):
    a1 = 1.0
    for i in range(len(b4)):
        a1 *= fonk2(b8[i], b4[i], b5[i])
    return a1
def fonk4(train_data, b8):
    b4, b5, b7 = fonk1(train_data)
    return fonk3(b8, b4, b5)
def fonk5():
    train_data, b8 = train_test_split(b2, test_size=0.10, random_state=42)
    b9 = np.array([row for row in train_data if row[-1] == 1.0])
    b10 = np.array([row for row in train_data if row[-1] == 0.0])
    a2 = 0
    for test_instance in b8:
        b11 = fonk4(b9, test_instance)
        b12 = fonk4(b10, test_instance)
        b13 = 1.0 if b11 > b12 else 0.0
        if b13 = = test_instance[-1]:
            a2 += 1
    b14 = (a2 / float(len(b8))) * 100.0
    print(f"Accuracy: {b14:.2f}%")
if b15 = = "__main__":
    fonk5()