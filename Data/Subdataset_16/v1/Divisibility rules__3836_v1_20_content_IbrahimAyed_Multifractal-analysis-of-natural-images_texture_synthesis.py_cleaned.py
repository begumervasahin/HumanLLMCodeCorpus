
import numpy as np
import matplotlib.pyplot as plt
a1 = 256
def fonk1(b17, b18):
    return (b17**2 + b18**2) < 0.25
def fonk2(b17, b18):
    return (np.abs(b17) < 0.5) * (np.abs(b18) < 0.5)
def fonk3(b17, b18):
    a, b1 = 1.0, 10.0
    b2 = np.sqrt((b17/a)**2 + (b18/b1)**2)
    b3 = np.zeros_like(b2)
    b4 = b2 < 0.5
    b3[b4] = np.cos(np.pi * b2[b4])
    return b3
def fonk4(b17, b18):
    a, b1 = 1.0, 1.0
    b2 = np.sqrt((b17/a)**2 + (b18/b1)**2)
    b3 = np.zeros_like(b2)
    b4 = b2 < 0.5
    b3[b4] = np.cos(np.pi * b2[b4])**2
    return b3
def fonk5(b17, b18):
    a, b1 = 1.0, 1.0
    b2 = np.sqrt((b17/a)**2 + (b18/b1)**2)
    b3 = np.zeros_like(b2)
    b4 = b2 < 0.5
    b3[b4] = np.cos(np.pi * np.exp(b2[b4]))**2
    return b3
def fonk6(b17, b18):
    a, b1 = 10.0, 1.0
    b2 = np.sqrt((b17/a)**2 + (b18/b1)**2)
    b3 = np.zeros_like(b2)
    b4 = b2 < 0.5
    b3[b4] = np.cos(np.pi * np.exp(np.exp(b2[b4])))**2
    return b3
def fonk7(b17, b18):
    a, b1 = 1.0, 1.0
    b2 = np.sqrt((b17/a)**2 + (b18/b1)**2)
    b3 = np.zeros_like(b2)
    b4 = b2 < 0.5
    b3[b4] = np.exp(-1/(1 - (2 * b2[b4])**4))
    return b3
def fonk8(f):
    b5 = 1.0 / a1
    Xmax, b6 = 1.0, 1.0
    b7 = (1.0 / (b5**2)) - 1
    b8 = (2.0 / np.pi) * b7 * (Xmax + 1) * (b6 + 1)
    b9 = np.random.poisson(b8)
    b10 = b7 * np.random.uniform(size=b9)
    b11 = 1.0 / np.sqrt(b7 - b10)
    b12 = -0.5 + np.random.uniform(size=b9) * (Xmax + 1)
    b13 = -0.5 + np.random.uniform(size=b9) * (b6 + 1)
    b14 = np.sqrt(0.08)
    b15 = -0.5 * 0.008
    b16 = np.random.randn(b9) * b14 + b15
    b17 = np.linspace(0, Xmax, a1)
    b18 = np.linspace(0, b6, a1)
    X, b19 = np.meshgrid(b17, b18)
    b20 = np.zeros((a1, a1))
    for i in range(b9):
        b21 = f((X - b12[i]) / b11[i], (b19 - b13[i]) / b11[i])
        b22 = (b21 != 0)
        b20[b22] = b20[b22] + b21[b22] * b16[i]
    b23 = np.exp(b20)
    b24 = b5**(np.exp(b15 + 0.5 * b14**2) - 1)
    return b23 / b24
def fonk9(Qr, alpha):
    a1 = Qr.shape[0]
    b17 = np.concatenate((np.arange(0, 1 + a1
    U, b25 = np.meshgrid(b17, b17)
    b26 = U**2 + b25**2
    b26[0, 0] = 1.0
    return np.real(np.fft.ifft2(np.fft.fft2(Qr) / (b26**alpha)))
b27 = fonk9(fonk8(f1), 0.05)
plt.figure()
plt.imshow(b27, b28 = 'gray')
plt.show()