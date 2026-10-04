import numpy as np
import sys
def fonk1(data, rows, cols, b20):
    b1 = []
    b2 = []
    for i in range(rows):
        b3 = [1]
        for b4 in range(cols):
            if b4 = = (cols - 1):
                b2.append(data[i][b4])
            else:
                for deg in range(b20):
                    b3.append(data[i][b4] ** (deg + 1))
        b1.append(b3)
    return np.array(b1), np.array(b2)
def fonk2(big_phi, b2, b21):
    b5 = np.transpose(big_phi)
    b6 = big_phi.shape[1]
    b7 = np.b7(b6)
    b8 = b21 * b7
    b9 = np.add(np.matmul(b5, big_phi), b8)
    b10 = np.linalg.pinv(b9)
    b11 = np.matmul(b10, b5)
    b12 = np.matmul(b11, b2)
    return b12
def fonk3(test_phi, b12):
    return np.dot(test_phi, b12)
def fonk4(b12):
    for i, w in enumerate(b12):
        print(f"w{i}={w:.4f}")
def fonk5(b18, b17):
    for i, (pred, target) in enumerate(zip(b18, b17)):
        b13 = (pred - target) ** 2
        print(f"b14 = {i+1:5d}, output={pred:.4f}, target value={target:.4f}, squared b13={b13:.4f}")
def fonk6(training, b20, b21, test):
    training_rows, b15 = training.shape
    test_rows, b16 = test.shape
    big_phi, b2 = fonk1(training, training_rows, b15, b20)
    b12 = fonk2(big_phi, b2, b21)
    fonk4(b12)
    test_phi, b17 = fonk1(test, test_rows, b16, b20)
    b18 = fonk3(test_phi, b12)
    fonk5(b18, b17)
if len(sys.argv) != 5:
    print("Error, not enough arguments given!")
else:
    b19 = sys.argv[1]
    b20 = int(sys.argv[2])
    b21 = float(sys.argv[3])
    b22 = sys.argv[4]
    with open(b19) as f:
        b23 = np.array([list(map(float, line.split())) for line in f])
    with open(b22) as f:
        b24 = np.array([list(map(float, line.split())) for line in f])
    fonk6(b23, b20, b21, b24)