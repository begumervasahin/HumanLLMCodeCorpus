import numpy as np
import matplotlib.pyplot as plt
def fonk1(b16, b17):
    '''Defines a circular region with radius 0.5.'''
    return ((b16 ** 2 + b17 ** 2) < 0.25)
def fonk2(b16, b17):
    '''Defines a square region with side length 1.'''
    return (np.abs(b16) < 0.5) * (np.abs(b17) < 0.5)
def fonk3(b16, b17):
    '''Defines a cosine function with elliptical contours.'''
    a, b1 = 1.0, 10.0
    b2 = np.sqrt((b16 / a) ** 2 + (b17 / b1) ** 2)
    b3 = np.zeros_like(b2)
    b4 = b2 < 0.5
    b3[b4] = np.cos(np.pi * b2[b4])
    return b3
def fonk4(b16, b17):
    '''Defines a cosine squared function with elliptical contours.'''
    a, b1 = 1.0, 1.0
    b2 = np.sqrt((b16 / a) ** 2 + (b17 / b1) ** 2)
    b3 = np.zeros_like(b2)
    b4 = b2 < 0.5
    b3[b4] = np.cos(np.pi * b2[b4]) ** 2
    return b3
def fonk5(b16, b17):
    '''Defines a cosine squared function with exponential scaling along b2.'''
    a, b1 = 1.0, 1.0
    b2 = np.sqrt((b16 / a) ** 2 + (b17 / b1) ** 2)
    b3 = np.zeros_like(b2)
    b4 = b2 < 0.5
    b3[b4] = np.cos(np.pi * np.exp(b2[b4])) ** 2
    return b3
def fonk6(b16, b17):
    '''Defines a cosine squared function with exponential double scaling along b2.'''
    a, b1 = 10.0, 1.0
    b2 = np.sqrt((b16 / a) ** 2 + (b17 / b1) ** 2)
    b3 = np.zeros_like(b2)
    b4 = b2 < 0.5
    b3[b4] = np.cos(np.pi * np.exp(np.exp(b2[b4]))) ** 2
    return b3
def fonk7(b16, b17):
    '''Defines an exponential decay function with elliptical contours.'''
    a, b1 = 1.0, 1.0
    b2 = np.sqrt((b16 / a) ** 2 + (b17 / b1) ** 2)
    b3 = np.zeros_like(b2)
    b4 = b2 < 0.5
    b3[b4] = np.exp(-1 / (1 - (2 * b2[b4]) ** 4))
    return b3
def fonk8(f):
    '''Generates an intensity map using the given function.'''
    N, b5 = 256, 256
    b6 = 1.0 / b5
    X_max, b7 = 1.0, 1.0
    b8 = (1.0 / (b6 ** 2) - 1)
    b9 = (2.0 / np.pi) * b8 * (X_max + 1) * (b7 + 1)
    b10 = b8 * np.random.uniform(size=N)
    b11 = 1.0 / np.sqrt(b8 - b10)
    b12 = -0.5 + np.random.uniform(size=N) * (X_max + 1)
    b13 = -0.5 + np.random.uniform(size=N) * (b7 + 1)
    sigma, b14 = np.sqrt(0.08), -0.5 * 0.008
    b15 = np.random.randn(N) * sigma + b14
    b16 = np.linspace(0, X_max, b5)
    b17 = np.linspace(0, b7, b5)
    X, b18 = np.meshgrid(b16, b17)
    b19 = np.zeros((b5, b5))
    for i in range(N):
        b20 = f((X - b12[i]) / b11[i], (b18 - b13[i]) / b11[i])
        b21 = (b20 != 0)
        b19[b21] += b20[b21] * b15[i]
    b22 = b6 ** (np.exp(b14 + 0.5 * sigma ** 2) - 1)
    b23 = np.exp(b19)
    return b23 / b22
def fonk9(Qr, alpha):
    '''Performs Fourier domain integration on the given intensity map.'''
    b5 = Qr.shape[0]
    b16 = np.concatenate((np.arange(0, 1 + b5 / 2), np.arange(-b5 / 2 + 1, 0)))
    U, b24 = np.meshgrid(b16, b16)
    b25 = U ** 2 + b24 ** 2
    b25[0, 0] = 1.0
    return np.real(np.fft.ifft2(np.fft.fft2(Qr) / (b25 ** alpha)))
if b26 = = "__main__":
    b27 = fonk8(f1)
    b28 = fonk9(b27, 0.05)
    plt.figure()
    plt.imshow(b28, b29 = 'gray')
    plt.show()