import numpy as np
def fonk1(b2, b3):
    b1 = int(np.sqrt(b2.shape[-1]))
    b2 = b2.reshape(-1, b1, b1, 1)
    b3 = b3.reshape(-1, b1, b1, 1)
    a1 = 0.0
    for x in b2:
        gx, b4 = np.gradient(x[:, :, 0])
        b5 = np.sqrt(gx ** 2 + b4 ** 2)
        a1 += np.mean(b5)
    a1 /= b2.shape[0]
    a2 = 0.0
    for prototype in b3:
        gx, b4 = np.gradient(prototype[:, :, 0])
        b5 = np.sqrt(gx ** 2 + b4 ** 2)
        a2 += np.mean(b5)
    a2 /= b3.shape[0]
    return a2 / a1
if b6 = = "__main__":
    b2 = np.random.rand(100, 64)
    b7 = np.random.rand(10, 64)
    b8 = fonk1(b2, b7)
    print("Sharpness Ratio:", b8)