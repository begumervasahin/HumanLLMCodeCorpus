import numpy as np
from numpy.linalg import svd
from PIL import Image
import matplotlib.pyplot as plt
class TRPCA:
    def __init__(self, rho=1.5, mu=1e-3, mu_max=1e10, max_iters=1000):
        self.rho = rho
        self.mu = mu
        self.mu_max = mu_max
        self.max_iters = max_iters
    def converged(self, L, E, X, L_new, E_new, eps=1e-8):
        condition1 = np.max(L_new - L) < eps
        condition2 = np.max(E_new - E) < eps
        condition3 = np.max(L_new + E_new - X) < eps
        return condition1 and condition2 and condition3
    def soft_shrink(self, X, tau):
        return np.sign(X) * np.maximum(np.abs(X) - tau, 0)
    def svd_shrink(self, X, tau):
        u, s, v = svd(X, full_matrices=False)
        s_bar = self.soft_shrink(s, tau)
        return np.dot(np.dot(u, np.diag(s_bar)), v)
    def admm(self, X):
        m, n = X.shape
        lamb = 1 / np.sqrt(max(m, n))
        L = np.zeros((m, n), float)
        E = np.zeros((m, n), float)
        Y = np.zeros((m, n), float)
        iters = 0
        while iters < self.max_iters:
            iters += 1
            L_new = self.svd_shrink(X - E - (1 / self.mu) * Y, 1 / self.mu)
            E_new = self.soft_shrink(X - L_new - (1 / self.mu) * Y, lamb / self.mu)
            Y += self.mu * (L_new + E_new - X)
            self.mu = min(self.rho * self.mu, self.mu_max)
            if self.converged(L, E, X, L_new, E_new):
                break
            L, E = L_new, E_new
            print(f"Iteration {iters}, error: {np.max(X - L - E)}")
        return L_new, E_new
def main(image_path):
    X = np.array(Image.open(image_path).convert('L'))
    trpca = TRPCA()
    L, S = trpca.admm(X)
    plt.subplot(131)
    plt.imshow(L, cmap='gray')
    plt.title('Low-rank')
    plt.subplot(132)
    plt.imshow(S, cmap='gray')
    plt.title('Sparse')
    plt.subplot(133)
    plt.imshow(X, cmap='gray')
    plt.title('Original')
    plt.show()
if __name__ == '__main__':
    image_path = 'set your path'
    main(image_path)