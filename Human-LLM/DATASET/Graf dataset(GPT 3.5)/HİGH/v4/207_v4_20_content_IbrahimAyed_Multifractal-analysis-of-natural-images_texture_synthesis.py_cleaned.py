import numpy as np
import matplotlib.pyplot as plt
def fonk1(b15, b16):
    '''Defines a1 circular region with radius 0.5.'''
    return ((b15 ** 2 + b16 ** 2) < 0.25)
def fonk2(b15, b16):
    '''Defines a1 square region with side length 1.'''
    return (np.abs(b15) < 0.5) * (np.abs(b16) < 0.5)
def fonk3(b15, b16):
    '''Defines a1 cosine function with elliptical contours.'''
    a1 = 1.0
    a2 = 10.0
    b1 = np.sqrt((b15 / a1) ** 2 + (b16 / a2) ** 2)
    b2 = np.zeros_like(b1)
    b3 = b1 < 0.5
    b2[b3] = np.cos(np.pi * b1[b3])
    return b2
def fonk4(b15, b16):
    '''Defines a1 cosine squared function with elliptical contours.'''
    a1 = 1.0
    a2 = 1.0
    b1 = np.sqrt((b15 / a1) ** 2 + (b16 / a2) ** 2)
    b2 = np.zeros_like(b1)
    b3 = b1 < 0.5
    b2[b3] = np.cos(np.pi * b1[b3]) ** 2
    return b2
def fonk5(b15, b16):
    '''Defines a1 cosine squared function with exponential scaling along b1.'''
    a1 = 1.0
    a2 = 1.0
    b1 = np.sqrt((b15 / a1) ** 2 + (b16 / a2) ** 2)
    b2 = np.zeros_like(b1)
    b3 = b1 < 0.5
    b2[b3] = np.cos(np.pi * np.exp(b1[b3])) ** 2
    return b2
def fonk6(b15, b16):
    '''Defines a1 cosine squared function with exponential double scaling along b1.'''
    a1 = 10.0
    a2 = 1.0
    b1 = np.sqrt((b15 / a1) ** 2 + (b16 / a2) ** 2)
    b2 = np.zeros_like(b1)
    b3 = b1 < 0.5
    b2[b3] = np.cos(np.pi * np.exp(np.exp(b1[b3]))) ** 2
    return b2
def fonk7(b15, b16):
    '''Defines an exponential decay function with elliptical contours.'''
    a1 = 1.0
    a2 = 1.0
    b1 = np.sqrt((b15 / a1) ** 2 + (b16 / a2) ** 2)
    b2 = np.zeros_like(b1)
    b3 = b1 < 0.5
    b2[b3] = np.exp(-1 / (1 - (2 * b1[b3]) ** 4))
    return b2
def fonk8(f):
    '''Generates an intensity map using the given function.'''
    a3 = 256
    b4 = 1.0 / a3
    a4 = 1.0
    a5 = 1.0
    b5 = (1.0 / (b4 ** 2) - 1)
    b6 = (2.0 / np.pi) * b5 * (a4 + 1) * (a5 + 1)
    b7 = np.random.poisson(b6)
    b8 = b5 * np.random.uniform(size=b7)
    b9 = 1.0 / np.sqrt(b5 - b8)
    b10 = -0.5 + np.random.uniform(size=b7) * (a4 + 1)
    b11 = -0.5 + np.random.uniform(size=b7) * (a5 + 1)
    b12 = np.sqrt(0.08)
    b13 = -0.5 * 0.008
    b14 = np.random.randn(b7) * b12 + b13
    b15 = np.linspace(0, a4, a3)
    b16 = np.linspace(0, a5, a3)
    X, b17 = np.meshgrid(b15, b16)
    b18 = np.zeros((a3, a3))
    for i in range(b7):
        b19 = f((X - b10[i]) / b9[i], (b17 - b11[i]) / b9[i])
        b20 = (b19 != 0)
        b18[b20] += b19[b20] * b14[i]
    b21 = b4 ** (np.exp(b13 + 0.5 * b12 ** 2) - 1)
    b22 = np.exp(b18)
    return b22 / b21
def fonk9(Qr, alpha):
    '''Performs Fourier domain integration on the given intensity map.'''
    a3 = Qr.shape[0]
    b15 = np.concatenate((np.arange(0, 1 + a3 / 2), np.arange(-a3 / 2 + 1, 0)))
    U, b23 = np.meshgrid(b15, b15)
    b24 = U ** 2 + b23 ** 2
    b24[0, 0] = 1.0
    return np.real(np.fft.ifft2(np.fft.fft2(Qr) / (b24 ** alpha)))
if b25 = = "__main__":
    b26 = fonk8(f1)
    b27 = fonk9(b26, 0.05)
    plt.figure()
    plt.imshow(b27, b28 = 'gray')
    plt.show()