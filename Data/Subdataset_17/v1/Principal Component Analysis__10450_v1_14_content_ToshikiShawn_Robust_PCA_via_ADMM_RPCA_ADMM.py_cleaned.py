import numpy as np
from numpy.linalg import svd
from PIL import Image
import matplotlib.pyplot as plt
class TRPCA:
    def converged(self, L, E, X, L_new, E_new):
        eps = 1e-8
        condition1 = np.max(np.abs(L_new - L)) < eps
        condition2 = np.max(np.abs(E_new - E)) < eps
        condition3 = np.max(np.abs(L_new + E_new - X)) < eps
        return condition1 and condition2 and condition3
    def SoftShrink(self, X, tau):
        return np.sign(X) * np.maximum(np.abs(X) - tau, 0)
    def SVDShrink(self, X, tau):
        u, s, v = svd(X, full_matrices=False)
        s_bar = self.SoftShrink(s, tau)
        return np.dot(u, np.dot(np.diag(s_bar), v))
    def ADMM(self, X):
        m, n = X.shape
        rho = 1.5
        mu = 1e-3
        mu_max = 1e10
        max_iters = 1000
        lamb = 1 / np.sqrt(max(m, n))
        L = np.zeros((m, n), float)
        E = np.zeros((m, n), float)
        Y = np.zeros((m, n), float)
        iters = 0
        while True:
            iters += 1
            L_new = self.SVDShrink(X - E - (1/mu) * Y, 1/mu)
            E_new = self.SoftShrink(X - L_new - (1/mu) * Y, lamb/mu)
            Y += mu * (L_new + E_new - X)
            mu = min(rho * mu, mu_max)
            if self.converged(L, E, X, L_new, E_new) or iters >= max_iters:
                return L_new, E_new
            else:
                L, E = L_new, E_new
                print(np.max(X - L - E))
image_path = 'set_your_path_here'
X = np.array(Image.open(image_path).convert('L'))
trpca = TRPCA()
L, S = trpca.ADMM(X)
plt.figure(figsize=(15, 5))
plt.subplot(131)
plt.imshow(L, cmap='gray')
plt.title('Low-rank Matrix L')
plt.subplot(132)
plt.imshow(S, cmap='gray')
plt.title('Sparse Matrix S')
plt.subplot(133)
plt.imshow(X, cmap='gray')
plt.title('Original Image X')
plt.show()