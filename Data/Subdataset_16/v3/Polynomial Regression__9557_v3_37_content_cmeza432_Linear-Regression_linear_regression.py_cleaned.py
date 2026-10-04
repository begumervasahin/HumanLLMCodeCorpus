import numpy as np
import sys
def fonk1(data, rows, cols, b19):
    b1 = []
    b2 = []
    for i in range(rows):
        b3 = [1]
        for b4 in range(cols):
            if b4 = = cols - 1:
                b2.append(data[i][b4])
            else:
                for deg in range(b19):
                    b3.append(data[i][b4] ** (deg + 1))
        b1.append(b3)
    return np.array(b1), np.array(b2)
def fonk2(b1, b2, b20):
    b5 = np.transpose(b1)
    b6 = np.identity(b1.shape[1])
    b7 = b20 * b6
    b8 = np.add(np.matmul(b5, b1), b7)
    b9 = np.linalg.pinv(b8)
    b10 = np.matmul(np.matmul(b9, b5), b2)
    return b10
def fonk3(test_design_matrix, b10):
    return np.dot(test_design_matrix, b10)
def fonk4(b10):
    for i, weight in enumerate(b10):
        print(f"w{i} = {weight:.4f}")
def fonk5(b17, b2):
    for i, (prediction, target) in enumerate(zip(b17, b2)):
        b11 = (prediction - target) ** 2
        print(f"b12 = {i+1:5d}, output={prediction:.4f}, target value={target:.4f}, squared error={b11:.4f}")
def fonk6(b22, b19, b20, b23):
    training_rows, b13 = b22.shape
    test_rows, b14 = b23.shape
    training_design_matrix, b15 = fonk1(b22, training_rows, b13, b19)
    b10 = fonk2(training_design_matrix, b15, b20)
    fonk4(b10)
    test_design_matrix, b16 = fonk1(b23, test_rows, b14, b19)
    b17 = fonk3(test_design_matrix, b10)
    fonk5(b17, b16)
if len(sys.argv) != 5:
    print("Error, not enough arguments given!")
else:
    b18 = sys.argv[1]
    b19 = int(sys.argv[2])
    b20 = float(sys.argv[3])
    b21 = sys.argv[4]
    with open(b18) as file:
        b22 = np.array([list(map(float, line.split())) for line in file])
    with open(b21) as file:
        b23 = np.array([list(map(float, line.split())) for line in file])
    fonk6(b22, b19, b20, b23)