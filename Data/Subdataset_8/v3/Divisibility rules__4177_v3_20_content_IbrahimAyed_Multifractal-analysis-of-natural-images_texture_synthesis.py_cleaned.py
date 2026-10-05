import numpy as np
import matplotlib.pyplot as plt
def f1(x, y):
    '''Defines a circular region.'''
    return ((x ** 2 + y ** 2) < 0.25)
def generate_intensity_map(f):
    '''Generates the intensity map based on the given function.'''
    n = 256
    r_min = 1.0 / n
    X_max = 1.0
    Y_max = 1.0
    u_max = (1.0 / (r_min ** 2) - 1)
    lambda_ = (2.0 / np.pi) * u_max * (X_max + 1) * (Y_max + 1)
    N = np.random.poisson(lambda_)
    ui = u_max * np.random.uniform(size=N)
    ri = 1.0 / np.sqrt(u_max - ui)
    xi = -0.5 + np.random.uniform(size=N) * (X_max + 1)
    yi = -0.5 + np.random.uniform(size=N) * (Y_max + 1)
    sigma = np.sqrt(0.08)
    mu = -0.5 * 0.008
    log_wi = np.random.randn(N) * sigma + mu
    x = np.linspace(0, X_max, n)
    y = np.linspace(0, Y_max, n)
    X, Y = np.meshgrid(x, y)
    log_Q = np.zeros((n, n))
    for i in range(N):
        tmp = f((X - xi[i]) / ri[i], (Y - yi[i]) / ri[i])
        slct = (tmp != 0)
        log_Q[slct] = log_Q[slct] + tmp[slct] * log_wi[i]
    C = r_min ** (np.exp(mu + 0.5 * sigma ** 2) - 1)
    Q = np.exp(log_Q)
    return Q / C
def fourier_domain_integration(Qr, alpha):
    '''Performs Fourier domain integration on the given intensity map.'''
    n = Qr.shape[0]
    x = np.concatenate((np.arange(0, 1 + n / 2), np.arange(-n / 2 + 1, 0)))
    U, V = np.meshgrid(x, x)
    S = U ** 2 + V ** 2
    S[0, 0] = 1.0
    return np.real(np.fft.ifft2(np.fft.fft2(Qr) / (S ** alpha)))
if __name__ == "__main__":
    intensity_map = generate_intensity_map(f1)
    integrated_map = fourier_domain_integration(intensity_map, 0.05)
    plt.figure()
    plt.imshow(integrated_map, cmap='gray')
    plt.show()