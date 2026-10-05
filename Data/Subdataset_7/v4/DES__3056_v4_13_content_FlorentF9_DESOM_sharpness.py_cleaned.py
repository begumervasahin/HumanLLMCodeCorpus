import numpy as np
def fonk1(b10, b11):
    b1 = int(np.sqrt(b10.shape[-1]))
    b2 = b10.reshape(-1, b1, b1, 1)
    b3 = int(np.sqrt(b11.shape[-1]))
    b4 = b11.reshape(-1, b3, b3, 1)
    b5 = fonk2(b2)
    b6 = fonk2(b4)
    return b6 / b5
def fonk2(data):
    a1 = 0.0
    for sample in data:
        gx, b7 = np.gradient(sample[:, :, 0])
        b8 = np.sqrt(gx ** 2 + b7 ** 2)
        a1 += np.mean(b8)
    return a1 / data.shape[0]
if b9 = = "__main__":
    b10 = np.random.rand(100, 64)
    b11 = np.random.rand(10, 64)
    b12 = fonk1(b10, b11)
    print("Sharpness Ratio:", b12)