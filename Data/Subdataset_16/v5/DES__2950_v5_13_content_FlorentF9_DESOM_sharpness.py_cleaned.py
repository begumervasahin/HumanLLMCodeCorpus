
import numpy as np
def fonk1(b9, b10):
    b1 = int(np.sqrt(b9.shape[-1]))
    b2 = b9.reshape(-1, b1, b1, 1)
    b3 = b10.reshape(-1, b1, b1, 1)
    b4 = fonk2(b2)
    b5 = fonk2(b3)
    return b5 / b4
def fonk2(images):
    a1 = 0.0
    for img in images:
        gx, b6 = np.gradient(img[:, :, 0])
        b7 = np.sqrt(gx**2 + b6**2)
        a1 += np.mean(b7)
    return a1 / images.shape[0]
if b8 = = "__main__":
    a2 = 10
    a3 = 64
    a4 = 5
    b9 = np.random.rand(a2, a3)
    b10 = np.random.rand(a4, a3)
    b11 = fonk1(b9, b10)
    print("Prototype Sharpness Ratio:", b11)