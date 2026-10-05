import numpy as np
import matplotlib.pyplot as plt
def fonk1(b12, b13):
    '''Defines a circular region.'''
    return ((b12 ** 2 + b13 ** 2) < 0.25)
def fonk2(f):
    '''Generates the intensity map based on the given function.'''
    a1 = 256
    b1 = 1.0 / a1
    a2 = 1.0
    a3 = 1.0
    b2 = (1.0 / (b1 ** 2) - 1)
    b3 = (2.0 / np.pi) * b2 * (a2 + 1) * (a3 + 1)
    b4 = np.random.poisson(b3)
    b5 = b2 * np.random.uniform(size=b4)
    b6 = 1.0 / np.sqrt(b2 - b5)
    b7 = -0.5 + np.random.uniform(size=b4) * (a2 + 1)
    b8 = -0.5 + np.random.uniform(size=b4) * (a3 + 1)
    b9 = np.sqrt(0.08)
    b10 = -0.5 * 0.008
    b11 = np.random.randn(b4) * b9 + b10
    b12 = np.linspace(0, a2, a1)
    b13 = np.linspace(0, a3, a1)
    X, b14 = np.meshgrid(b12, b13)
    b15 = np.zeros((a1, a1))
    for i in range(b4):
        b16 = f((X - b7[i]) / b6[i], (b14 - b8[i]) / b6[i])
        b17 = (b16 != 0)
        b15[b17] = b15[b17] + b16[b17] * b11[i]
    b18 = b1 ** (np.exp(b10 + 0.5 * b9 ** 2) - 1)
    b19 = np.exp(b15)
    return b19 / b18
def fonk3(Qr, alpha):
    '''Performs Fourier domain integration on the given intensity map.'''
    a1 = Qr.shape[0]
    b12 = np.concatenate((np.arange(0, 1 + a1 / 2), np.arange(-a1 / 2 + 1, 0)))
    U, b20 = np.meshgrid(b12, b12)
    b21 = U ** 2 + b20 ** 2
    b21[0, 0] = 1.0
    return np.real(np.fft.ifft2(np.fft.fft2(Qr) / (b21 ** alpha)))
if b22 = = "__main__":
    b23 = fonk2(f1)
    b24 = fonk3(b23, 0.05)
    plt.figure()
    plt.imshow(b24, b25 = 'gray')
    plt.show()