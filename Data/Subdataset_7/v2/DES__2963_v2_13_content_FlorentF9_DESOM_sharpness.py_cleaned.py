import numpy as np
def fonk1(b2, b3):
    b1 = int(np.sqrt(b2.shape[-1]))
    b2 = b2.reshape(-1, b1, b1, 1)
    b3 = b3.reshape(-1, b1, b1, 1)
    b4 = fonk2(b2)
    b5 = fonk2(b3)
    return b5 / b4
def fonk2(data):
    a1 = 0.0
    for sample in data:
        gx, b6 = np.gradient(sample[:, :, 0])
        b7 = np.sqrt(gx ** 2 + b6 ** 2)
        a1 += np.mean(b7)
    return a1 / data.shape[0]
if b8 = = "__main__":
    b2 = np.random.rand(100, 64)
    b3 = np.random.rand(10, 64)
    b9 = fonk1(b2, b3)
    print("Sharpness Ratio:", b9)