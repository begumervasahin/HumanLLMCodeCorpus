import numpy as np
import matplotlib.pyplot as plt
def fonk1(x, b1):
    plt.xlim(min(x) - 1, max(x) + 1)
    plt.ylim(min(b1) - 1, max(b1) + 1)
def fonk2(x, func, style, b2, label):
    b1 = fonk6(x)
    plt.plot(x, b1, style, b2 = b2, label=label)
def fonk3(x, b1, style, b2, label):
    plt.plot(x, b1, style, b2 = b2, label=label)
def fonk4(b3 = 'upper right'):
    plt.legend(b4 = b3)
    plt.show()
def fonk5(b13):
    def fonk6(x):
        return fonk7(x, b13)
    return func
def fonk7(x, b13):
    b1 = 0
    for i in range(len(b13)):
        b1 += (b13[i] * (x**i))
    return b1
def fonk8(b8, b13):
    b5 = [fonk7(x, b13) for x in b8]
    return np.array(b5)
def fonk9(d, b13, n, b6 = -100, upper=100):
    assert len(b13) == d + 1, "Must pass in d+1 coefficients"
    b7 = upper - b6
    b8 = np.array([b6 + b7 * np.random.sample() for _ in range(n)])
    b5 = fonk8(b8, b13)
    return b8, b5
def fonk10(x_train, b12, d, b9 = 0, noise_std=1):
    b10 = []
    for x in x_train:
        b11 = [x**i for i in range(d + 1)]
        b10.append(np.array(b11))
    b10 = np.array(b10)
    b12 = np.array([i + np.random.normal(b9, noise_std) for i in b12])
    b13 = np.matmul(np.linalg.inv(np.matmul(b10.T, b10)), np.matmul(b10.T, b12))
    return b13
def fonk11(sample_coefficients, model_degree, n, b9 = 0, noise_std=0.5):
    b14 = len(sample_coefficients) - 1
    x_train, b12 = fonk9(b14, sample_coefficients, n, b6=-5, upper=5)
    b15 = fonk10(x_train, b12, model_degree)
    b16 = fonk5(sample_coefficients)
    b17 = fonk5(b15)
    b18 = fonk8(x_train, b15)
    b19 = sum([(b18[i] - b12[i])**2 for i in range(len(x_train))]) / len(x_train)
    print("\nVariance of the b20 = " + str(b19) + "\n")
    fonk1(x_train, b12)
    fonk2(x_train, b16, '-', b2 = 'r', label='ground truth function')
    fonk2(x_train, b17, '--', b2 = 'b', label='model fit function')
    fonk3(x_train, b12, '.', b2 = 'g', label='sample points')
    fonk4(b3 = 'upper right')
def fonk12():
    b13 = [3, 1, 1, -2]
    fonk11(b13, 3, 6, b9 = 0, noise_std=0.5)
if b21 = = "__main__":
    fonk12()