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
def fonk5(b11):
    def fonk6(x):
        return fonk7(x, b11)
    return func
def fonk7(x, b11):
    return sum(b11[i] * (x ** i) for i in range(len(b11)))
def fonk8(b6, b11):
    return np.array([fonk7(x, b11) for x in b6])
def fonk9(d, b11, n, b5 = -100, upper=100):
    assert len(b11) == d + 1, "Must pass in d+1 coefficients"
    b6 = np.linspace(b5, upper, n)
    b7 = fonk8(b6, b11)
    return b6, b7
def fonk10(x_train, b12, d, b8 = 0, noise_std=1):
    b9 = np.array([[x ** i for i in range(d + 1)] for x in x_train])
    b10 = b12 + np.random.normal(b8, noise_std, b12.shape)
    b11 = np.linalg.inv(b9.T @ b9) @ (b9.T @ b10)
    return b11
def fonk11(sample_coefficients, model_degree, n, b8 = 0, noise_std=0.5):
    x_train, b12 = fonk9(len(sample_coefficients) - 1, sample_coefficients, n, b5=-5, upper=5)
    b13 = fonk10(x_train, b12, model_degree, b8, noise_std)
    b14 = fonk5(sample_coefficients)
    b15 = fonk5(b13)
    b16 = fonk8(x_train, b13)
    b17 = np.mean((b16 - b12) ** 2)
    print("\nVariance of the b18 = " + str(b17) + "\n")
    fonk1(x_train, b12)
    fonk2(x_train, b14, '-', b2 = 'r', label='ground truth function')
    fonk2(x_train, b15, '--', b2 = 'b', label='model fit function')
    fonk3(x_train, b12, '.', b2 = 'g', label='sample points')
    fonk4(b3 = 'upper right')
def fonk12():
    b11 = [3, 1, 1, -2]
    fonk11(b11, 3, 6, b8 = 0, noise_std=0.5)
if b19 = = "__main__":
    fonk12()