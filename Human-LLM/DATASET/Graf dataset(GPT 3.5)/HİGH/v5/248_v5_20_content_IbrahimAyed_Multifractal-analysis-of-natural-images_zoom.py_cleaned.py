import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate
def fonk1(l, L, b26, b1 = 1.0, Ymax=1.0):
    b2 = l
    b3 = L
    b4 = 1.0 / (b2 ** 2) - 1
    b5 = 1.0 / (b3 ** 2) - 1
    b6 = (2.0 / np.pi) * (b4 - b5) * (b1 + 1) * (Ymax + 1)
    b7 = np.random.poisson(b6)
    b8 = np.random.uniform(b5, b4, size=b7)
    b9 = 1.0 / np.sqrt(b4 - b8 + b5)
    b10 = np.random.uniform(-0.5, b1 + 0.5, size=b7)
    b11 = np.random.uniform(-0.5, Ymax + 0.5, size=b7)
    b12 = np.sqrt(0.08)
    b13 = -0.5 * 0.08
    b14 = np.random.randn(b7) * b12 + b13
    b15 = np.linspace(0, b1, b26)
    b16 = np.linspace(0, Ymax, b26)
    X, b17 = np.meshgrid(b15, b16)
    b18 = np.zeros((b26, b26))
    for i in range(b7):
        b19 = (((X - b10[i]) / b9[i]) ** 2 + ((b17 - b11[i]) / b9[i]) ** 2) < 0.25
        b18[b19] += b14[i]
    b20 = np.exp(b18)
    b21 = (b2 / b3) ** (np.exp(b13 + 0.5 * b12 ** 2) - 1)
    return b20 / b21
def fonk2(Im, b26, b1, Ymax):
    b15 = np.linspace(0, b1, b26)
    b16 = np.linspace(0, Ymax, b26)
    X, b17 = np.meshgrid(b15, b16)
    b22 = np.linspace(0, b1, b26 * 2)
    b23 = np.linspace(0, Ymax, b26 * 2)
    X_new, b24 = np.meshgrid(b22, b23)
    b25 = interpolate.interp2d(b15, b16, Im)
    return b25(b22, b23)
def fonk3(Qr, a2):
    b26 = Qr.shape[0]
    b15 = np.concatenate((np.arange(0, 1 + b26 / 2), np.arange(-b26 / 2 + 1, 0)))
    U, b27 = np.meshgrid(b15, b15)
    b28 = U ** 2 + b27 ** 2
    b28[0, 0] = 1.0
    return np.real(np.fft.ifft2(np.fft.fft2(Qr) / (b28 ** a2)))
def fonk4(Qr, a2):
    b26 = Qr.shape[0]
    b15 = np.concatenate((np.arange(0, 1 + b26 / 2), np.arange(-b26 / 2 + 1, 0)))
    U, b27 = np.meshgrid(b15, b15)
    b28 = U ** 2 + b27 ** 2
    b28[0, 0] = 1.0
    return np.real(np.fft.ifft2(np.fft.fft2(Qr) * (b28 ** a2)))
def fonk5(b37, Iold):
    b29 = b37.shape[0]
    b26 = Iold.shape[0]
    if (b37.shape[1] != b29) or (Iold.shape[1] != b26) or ((b29 / b26) != 2 ** (int(np.log2(b29 / b26)))):
        print("Error: Size of images mismatch")
        return
    for i in range(b26):
        for j in range(b26):
            b30 = Iold[i, j]
            b37[2 * i:2 * (i + 1), 2 * j:2 * (j + 1)] *= b30 / np.sum(
                b37[2 * i:2 * (i + 1), 2 * j:2 * (j + 1)])
    return b37
def fonk6(Im, a2, a1):
    b26 = Im.shape[0]
    b1 = 1.0
    b31 = 1.0 / b26
    b32 = fonk2(Im, b26, b1, b1)
    b33 = fonk4(b32, a2)
    b34 = fonk1(0.5 * b31, b31, 2 * b26, b1, b1)
    b35 = b33 * b34 + a1 * 1 * (b34 - b34.mean())
    b36 = Im.mean() + fonk3(b35, a2)
    b36 = np.maximum(b36, np.zeros_like(b36))
    b37 = fonk5(b36, Im)
    return b37
def fonk7():
    b1 = 1.0
    b26 = 32
    b20 = fonk1(1.0 / b26, b26, b1, b1)
    a1 = 8
    a2 = 0.7
    a3 = 23
    b38 = a3 + a1 * fonk3(b20 - b20.mean(), a2)
    plt.figure()
    plt.imshow(b38, b39 = 'magma')
    plt.plot()
    b40 = fonk6(b38, a2, a1)
    plt.figure()
    plt.imshow(b40, b39 = 'magma')
    plt.plot()
    b41 = fonk6(b40, a2, a1)
    plt.figure()
    plt.imshow(b41, b39 = 'magma')
    plt.plot()
    b42 = fonk6(b41, a2, a1)
    plt.figure()
    plt.imshow(b42, b39 = 'magma')
    plt.plot()
    b43 = fonk6(b42, a2, a1)
    plt.figure()
    plt.imshow(b43, b39 = 'magma')
    plt.plot()
    b44 = fonk6(b43, a2, a1)
    plt.figure()
    plt.imshow(b44, b39 = 'magma')
    plt.plot()
    a4 = 8
    b45 = b38[a4:a4 + 16, a4:a4 + 16]
    plt.figure()
    plt.imshow(b45, b39 = 'magma')
    plt.plot()
    b46 = b41[a4 * 4:(a4 + 16) * 4, a4 * 4:(a4 + 16) * 4]
    plt.figure()
    plt.imshow(b46, b39 = 'magma')
    plt.plot()
    b46 = b42[a4 * 8:(a4 + 16) * 8, a4 * 8:(a4 + 16) * 8]
    plt.figure()
    plt.imshow(b46, b39 = 'magma')
    plt.plot()
    b46 = b43[a4 * 16:(a4 + 16) * 16, a4 * 16:(a4 + 16) * 16]
    plt.figure()
    plt.imshow(b46, b39 = 'magma')
    plt.plot()
    plt.show()
if b47 = = "__main__":
    fonk7()