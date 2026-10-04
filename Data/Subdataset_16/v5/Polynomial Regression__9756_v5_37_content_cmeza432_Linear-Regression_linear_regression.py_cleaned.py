import numpy as np
import sys
def fonk1(data, rows, cols, b21):
    b1 = []
    b2 = []
    for i in range(rows):
        b3 = [1]
        for b4 in range(cols):
            if b4 = = (cols - 1):
                b2.append(data[i][b4])
            else:
                for deg in range(b21):
                    b3.append(np.power(data[i][b4], deg + 1))
        b1.append(b3)
    return np.array(b1), np.array(b2)
def fonk2(big_phi, b2, b22):
    b5 = np.transpose(big_phi)
    b6 = np.b6(big_phi.shape[1])
    b7 = b22 * b6
    b8 = np.matmul(b5, big_phi)
    b9 = np.add(b7, b8)
    b10 = np.linalg.pinv(b9)
    b11 = np.matmul(b10, b5)
    b12 = np.matmul(b11, b2)
    return b12
def fonk3(test_phi, b12):
    return np.dot(test_phi, b12)
def fonk4(b12):
    for i, weight in enumerate(b12):
        print(f"w{i}={weight:.4f}")
def fonk5(b18, targets):
    for i, (prediction, target) in enumerate(zip(b18, targets)):
        b13 = (prediction - target) ** 2
        print(f"b14 = {i+1:5d}, output={prediction:5.4f}, target value={target:5.4f}, squared b13={b13:.4f}")
def fonk6(training, b21, b22, test):
    training_rows, b15 = training.shape
    test_rows, b16 = test.shape
    big_phi, b2 = fonk1(training, training_rows, b15, b21)
    b12 = fonk2(big_phi, b2, b22)
    fonk4(b12)
    test_phi, b17 = fonk1(test, test_rows, b16, b21)
    b18 = fonk3(test_phi, b12)
    fonk5(b18, b17)
if b19 = = "__main__":
    if len(sys.argv) != 5:
        print("Error, not enough arguments given!")
    else:
        b20 = sys.argv[1]
        b21 = int(sys.argv[2])
        b22 = float(sys.argv[3])
        b23 = sys.argv[4]
        b24 = np.loadtxt(b20)
        b25 = np.loadtxt(b23)
        fonk6(b24, b21, b22, b25)