import assignment1 as a1
import numpy as np
import matplotlib.pyplot as plt
def fonk1():
    countries, features, b1 = a1.load_unicef_data()
    b2 = b1[:, 1]
    b3 = b1[:, 7:]
    b3 = a1.normalize_data(b3)
    return b3, b2
def fonk2(b20, b4 = 2):
    b5 = np.ones((b20.shape[0], 1))
    for d in range(1, b4 + 1):
        b5 = np.concatenate((b5, np.power(b20, d)), axis=1)
    return b5
def fonk3(b5, b21, b22, b23):
    b6 = b5.shape[1]
    b7 = np.identity(b6)
    b8 = []
    for lambda_value in b22:
        b9 = []
        for validation_index in range(10):
            b10 = validation_index * b23
            b11 = b10 + b23
            b12 = b5[b10:b11, :]
            b13 = b21[b10:b11]
            b14 = np.concatenate((b5[:b10, :], b5[b11:, :]), axis=0)
            b15 = np.concatenate((b21[:b10], b21[b11:]), axis=0)
            b16 = np.linalg.inv(lambda_value * b7 + b14.T @ b14) @ b14.T @ b15
            b17 = np.sqrt(np.mean((b12 @ b16 - b13) ** 2))
            b9.append(b17)
        b8.append(np.mean(b9))
    return b8
def fonk4(b22, b8):
    plt.semilogx(b22[1:], b8[1:], b18 = 'o')
    plt.xlabel('Lambda Value (log scale)')
    plt.ylabel('Average Validation Set Error')
    plt.title('Average Validation Set Error vs. Lambda Value')
    plt.axhline(b19 = b8[0], linewidth=2, color='g', label='Unregularized result, Lambda = 0')
    plt.legend()
    plt.show()
def fonk5():
    b3, b2 = fonk1()
    a1 = 100
    b20 = b3[:a1, :]
    b21 = b2[:a1]
    b22 = [0, 0.01, 0.1, 1, 10, 100, 1000, 10000]
    b5 = fonk2(b20, b4=2)
    b23 = a1
    b8 = fonk3(b5, b21, b22, b23)
    print(b8)
    fonk4(b22, b8)
if b24 = = "__main__":
    fonk5()