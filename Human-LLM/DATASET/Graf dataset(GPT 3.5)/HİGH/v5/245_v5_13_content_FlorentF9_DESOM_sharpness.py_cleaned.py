import numpy as np
def fonk1(b9, b10):
    b1 = fonk2(b9)
    b2 = fonk2(b10)
    b3 = fonk3(b1)
    b4 = fonk3(b2)
    return b4 / b3
def fonk2(data):
    b5 = int(np.sqrt(data.shape[-1]))
    return data.reshape(-1, b5, b5, 1)
def fonk3(data):
    a1 = 0.0
    for sample in data:
        gx, b6 = np.gradient(sample[:, :, 0])
        b7 = np.sqrt(gx ** 2 + b6 ** 2)
        a1 += np.mean(b7)
    return a1 / len(data)
if b8 = = "__main__":
    b9 = np.random.rand(100, 64)
    b10 = np.random.rand(10, 64)
    b11 = fonk1(b9, b10)
    print("Sharpness Ratio:", b11)