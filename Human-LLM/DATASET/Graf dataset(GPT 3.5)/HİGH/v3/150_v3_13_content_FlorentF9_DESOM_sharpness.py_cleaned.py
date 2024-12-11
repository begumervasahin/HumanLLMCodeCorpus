import numpy as np
def fonk1(data):
    a1 = 0.0
    for sample in data:
        gradient_x, b1 = np.gradient(sample[:, :, 0])
        b2 = np.sqrt(gradient_x ** 2 + b1 ** 2)
        a1 += np.mean(b2)
    return a1 / data.shape[0]
def fonk2(b4, b5):
    b3 = int(np.sqrt(b4.shape[-1]))
    b4 = b4.reshape(-1, b3, b3, 1)
    b5 = b5.reshape(-1, b3, b3, 1)
    b6 = fonk1(b4)
    b7 = fonk1(b5)
    return b7 / b6
if b8 = = "__main__":
    b4 = np.random.rand(100, 64)
    b5 = np.random.rand(10, 64)
    b9 = fonk2(b4, b5)
    print("Sharpness Ratio:", b9)