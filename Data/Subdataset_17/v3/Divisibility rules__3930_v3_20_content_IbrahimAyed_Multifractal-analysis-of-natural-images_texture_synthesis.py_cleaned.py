
import numpy as np
import matplotlib.pyplot as plt
n = 256
def f1(x, y):
    return (x**2 + y**2) < 0.25
def f2(x, y):
    return (np.abs(x) < 0.5) & (np.abs(y) < 0.5)
def f3(x, y):
    a, b = 1.0, 10.0
    M = np.sqrt((x/a)**2 + (y/b)**2)
    res = np.zeros_like(M)
    select = M < 0.5
    res[select] = np.cos(np.pi * M[select])
    return res
def f4(x, y):
    a, b = 1.0, 1.0
    M = np.sqrt((x/a)**2 + (y/b)**2)
    res = np.zeros_like(M)
    select = M < 0.5
    res[select] = np.cos(np.pi * M[select])**2
    return res
def f5(x, y):
    a, b = 1.0, 1.0
    M = np.sqrt((x/a)**2 + (y/b)**2)
    res = np.zeros_like(M)
    select = M < 0.5
    res[select] = np.cos(np.pi * np.exp(M[select]))**2
    return res
def f6(x, y):
    a, b = 10.0, 1.0
    M = np.sqrt((x/a)**2 + (y/b)**2)
    res = np.zeros_like(M)
    select = M < 0.5
    res[select] = np.cos(np.pi * np.exp(np.exp(M[select])))**2
    return res
def f7(x, y):
    a, b = 1.0, 1.0
    M = np.sqrt((x/a)**2 + (y/b)**2)
    res = np.zeros_like(M)
    select = M < 0.5
    res[select] = np.exp(-1/(1 - (2 * M[select])**4))
    return res
def Q(f):
    rmin = 1.0 / n
    Xmax, Ymax = 1.0, 1.0
    umax = (1.0 / (rmin**2)) - 1
    lbda = (2.0 / np.pi) * umax * (Xmax + 1) * (Ymax + 1)
    N = np.random.poisson(lbda)
    ui = umax * np.random.uniform(size=N)
    ri = 1.0 / np.sqrt(umax - ui)
    xi = -0.5 + np.random.uniform(size=N) * (Xmax + 1)
    yi = -0.5 + np.random.uniform(size=N) * (Ymax + 1)
    sigma = np.sqrt(0.08)
    mu = -0.5 * 0.008
    logWi = np.random.randn(N) * sigma + mu
    x = np.linspace(0, Xmax, n)
    y = np.linspace(0, Ymax, n)
    X, Y = np.meshgrid(x, y)
    logQ = np.zeros((n, n))
    for i in range(N):
        tmp = f((X - xi[i]) / ri[i], (Y - yi[i]) / ri[i])
        slct = (tmp != 0)
        logQ[slct] += tmp[slct] * logWi[i]
    Q = np.exp(logQ)
    C = rmin**(np.exp(mu + 0.5 * sigma**2) - 1)
    return Q / C
def integrate(Qr, alpha):
    n = Qr.shape[0]
    x = np.concatenate((np.arange(0, 1 + n
    U, V = np.meshgrid(x, x)
    S = U**2 + V**2
    S[0, 0] = 1.0
    return np.real(np.fft.ifft2(np.fft.fft2(Qr) / (S**alpha)))
Qres1 = integrate(Q(f1), 0.05)
plt.figure()
plt.imshow(Qres1, cmap='gray')
plt.title('Generated Field')
plt.colorbar()
plt.show()