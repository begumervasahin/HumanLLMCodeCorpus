import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate
def fonk1(l, L, b22, b1 = 1.0, Ymax=1.0):
    b2 = l
    b3 = 1.0 * L
    b4 = (1.0 / (b2 ** 2) - 1)
    b5 = (1.0 / (b3 ** 2) - 1)
    b6 = (2.0 / np.pi) * (b4 - b5) * (b1 + 1) * (Ymax + 1)
    b7 = np.random.poisson(b6)
    b8 = (b4 - b5) * np.random.uniform(size=b7) + b5
    b9 = 1.0 / np.sqrt(b4 - b8 + b5)
    b10 = -0.5 + np.random.uniform(size=b7) * (b1 + 1)
    b11 = -0.5 + np.random.uniform(size=b7) * (Ymax + 1)
    b12 = np.sqrt(0.08)
    b13 = -0.5 * 0.08
    b14 = np.random.randn(b7) * b12 + b13
    b15 = np.linspace(0, b1, b22)
    b16 = np.linspace(0, Ymax, b22)
    X, b17 = np.meshgrid(b15, b16)
    b18 = np.zeros((b22, b22))
    for i in range(b7):
        b19 = ((((X - b10[i]) / b9[i]) ** 2 + ((b17 - b11[i]) / b9[i]) ** 2) < 0.25)
        b18[b19] += b14[i]
    b20 = np.exp(b18)
    b21 = (b2 / b3) ** (np.exp(b13 + 0.5 * b12 ** 2) - 1)
    return b20 / b21
def fonk2(Qr, a2):
    b22 = Qr.shape[0]
    b15 = np.concatenate((np.arange(0, 1 + b22 / 2), np.arange(-b22 / 2 + 1, 0)))
    U, b23 = np.meshgrid(b15, b15)
    b24 = U ** 2 + b23 ** 2
    b24[0, 0] = 1.0
    return np.real(np.fft.ifft2(np.fft.fft2(Qr) / (b24 ** a2)))
def fonk3(Qr, a2):
    b22 = Qr.shape[0]
    b15 = np.concatenate((np.arange(0, 1 + b22 / 2), np.arange(-b22 / 2 + 1, 0)))
    U, b23 = np.meshgrid(b15, b15)
    b24 = U ** 2 + b23 ** 2
    b24[0, 0] = 1.0
    return np.real(np.fft.ifft2(np.fft.fft2(Qr) * (b24 ** a2)))
def fonk4(b33, Iold):
    b25 = b33.shape[0]
    b22 = Iold.shape[0]
    if (b33.shape[1] != b25) or (Iold.shape[1] != b22) or ((b25 / b22) != 2 ** (int(np.log2(b25 / b22)))):
        print("Error: Size of images mismatch")
        return
    for i in range(b22):
        for j in range(b22):
            b26 = Iold[i, j]
            b33[2 * i:2 * (i + 1), 2 * j:2 * (j + 1)] = (b26 * b33[2 * i:2 * (i + 1), 2 * j:2 * (j + 1)]) / np.sum(
                b33[2 * i:2 * (i + 1), 2 * j:2 * (j + 1)])
    return b33
def fonk5(Im, a2, a1):
    b22 = Im.shape[0]
    b1 = 1.0
    b27 = 1.0 / b22
    b28 = interpolatex2(Im, b22, b1, b1)
    b29 = fonk3(b28, a2)
    b30 = fonk1(0.5 * b27, b27, 2 * b22, b1, b1)
    b31 = b29 * b30 + a1 * 1 * (b30 - b30.mean())
    b32 = Im.mean() + fonk2(b31, a2)
    b32 = np.maximum(b32, np.zeros_like(b32))
    b33 = fonk4(b32, Im)
    return b33
def fonk6():
    b1 = 1.0
    b22 = 32
    b20 = fonk1(1.0 / b22, b22, b1, b1)
    a1 = 8
    a2 = 0.7
    a3 = 23
    b34 = a3 + a1 * fonk2(b20 - b20.mean(), a2)
    plt.figure()
    plt.imshow(b34, b35 = 'magma')
    plt.plot()
    b36 = fonk5(b34, a2, a1)
    plt.figure()
    plt.imshow(b36, b35 = 'magma')
    plt.plot()
    b37 = fonk5(b36, a2, a1)
    plt.figure()
    plt.imshow(b37, b35 = 'magma')
    plt.plot()
    b38 = fonk5(b37, a2, a1)
    plt.figure()
    plt.imshow(b38, b35 = 'magma')
    plt.plot()
    b39 = fonk5(b38, a2, a1)
    plt.figure()
    plt.imshow(b39, b35 = 'magma')
    plt.plot()
    b40 = fonk5(b39, a2, a1)
    plt.figure()
    plt.imshow(b40, b35 = 'magma')
    plt.plot()
    a4 = 8
    b41 = b34[a4:a4 + 16, a4:a4 + 16]
    plt.figure()
    plt.imshow(b41, b35 = 'magma')
    plt.plot()
    b42 = b37[a4 * 4:(a4 + 16) * 4, a4 * 4:(a4 + 16) * 4]
    plt.figure()
    plt.imshow(b42, b35 = 'magma')
    plt.plot()
    b42 = b38[a4 * 8:(a4 + 16) * 8, a4 * 8:(a4 + 16) * 8]
    plt.figure()
    plt.imshow(b42, b35 = 'magma')
    plt.plot()
    b42 = b39[a4 * 16:(a4 + 16) * 16, a4 * 16:(a4 + 16) * 16]
    plt.figure()
    plt.imshow(b42, b35 = 'magma')
    plt.plot()
    plt.show()
if b43 = = "__main__":
    fonk6()