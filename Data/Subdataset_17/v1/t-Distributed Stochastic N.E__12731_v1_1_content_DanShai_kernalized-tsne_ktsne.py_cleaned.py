import numpy as np
from kernels import Kernels
class Ktsne:
    def __init__(self, X, f_opts={}):
        self._dim = f_opts.get("n_dims", 2)
        self._perp = f_opts.get("perplexity", 30)
        self._eta = f_opts.get("eta", 200)
        self.f_opts = f_opts
        self._momentum = 0.4
        self.X = X.copy()
        self.P = None
        self.Q = None
        self._iter = 0
        n, d = self.X.shape
        y_sz = (n, self._dim)
        mw, Mw = -np.sqrt(6. / sum(y_sz)), np.sqrt(6. / sum(y_sz))
        self.Y = np.random.randn(n, self._dim) * Mw
        self.dY = None
        self.Y_t = np.array([np.zeros_like(self.Y), np.zeros_like(self.Y)])
        np.seterr(divide='ignore', invalid='ignore')
    def reduce_X(self):
        kernel_options = {
            "kernel": self.f_opts.get("ker", "pca"),
            "gamma": self.f_opts.get("gamma", 0.5),
            "degree": self.f_opts.get("p_degree", 1),
            "p_dims": self.f_opts.get("p_dims", 4)
        }
        kn = Kernels(self.X, k_opts=kernel_options)
        self.X = kn.process_data()
    @staticmethod
    def L1(X):
        D = np.sum(np.abs(X[:, None] - X[None, :]), axis=-1)
        return D
    @staticmethod
    def L2(X):
        D = np.sum((X[:, None] - X[None, :])**2, axis=-1)
        return D
    def bin_search(self, d_row, target, tol=1e-2, niter=1000, low=1e-10, up=1e3):
        for i in range(niter):
            estimated = (low + up) / 2.0
            p_row = np.exp(-d_row / estimated)
            sumP = np.sum(p_row)
            p_row /= sumP
            val = self.entropy(p_row)
            dif = np.abs(val - target)
            if dif <= tol:
                break
            if val > target:
                up = estimated
            else:
                low = estimated
        return p_row, estimated
    @staticmethod
    def entropy(p_row):
        H = -np.sum(p_row * np.log2(p_row))
        return H
    def compute_P(self):
        n, d = self.X.shape
        P = np.zeros((n, n))
        sigmas = np.ones((n, 1))
        D = self.L2(self.X)
        target_entropy = np.log2(self._perp)
        for i in range(n):
            d_row = D[i, np.hstack((np.arange(0, i), np.arange(i + 1, n)))]
            p_row, estimated = self.bin_search(d_row, target_entropy)
            P[i, np.hstack((np.arange(0, i), np.arange(i + 1, n)))] = p_row
            sigmas[i] = estimated
        msig = np.mean(np.sqrt(1 / sigmas))
        print("Mean value of sigma:", msig)
        P = (P + P.T) / (2 * n)
        P = P / np.sum(P)
        P = np.maximum(P, 1e-12)
        return P
    def compute_Q(self):
        D = self.L2(self.Y)
        q = 1 / (1 + D)
        np.fill_diagonal(q, 0)
        self.Q = q / np.sum(q)
        self.Q = np.maximum(self.Q, 1e-12)
        return q
    def gradient(self, q):
        PQ = self.P - self.Q
        M = PQ * q
        MD = 4 * (np.diag(np.sum(M, axis=1)) - M)
        self.dY = np.dot(MD, self.Y)
    def get_solution(self, steps=500):
        self.reduce_X()
        self.P = self.compute_P()
        self.P = self.P * 10.0
        for i in range(steps):
            cost = self.step()
            if i % 500 == 0:
                print("Iteration", i, ": cost is", cost)
        print("Final cost:", cost)
        self.Y = self.Y - np.mean(self.Y, axis=0)
        return self.Y
    def step(self):
        q = self.compute_Q()
        self.gradient(q)
        if self._iter == 100:
            self.P = self.P / 10.0
        if self._iter == 25:
            self._momentum = 0.8
        self.Y -= self._eta * self.dY
        self.Y += self._momentum * np.diff(self.Y_t, axis=0)[0]
        self.Y_t[1] = self.Y_t[0].copy()
        self.Y_t[0] = self.Y
        C = np.sum(self.P * np.log(self.P / self.Q))
        self._iter += 1
        return C
if __name__ == "__main__":
    data = np.random.rand(100, 10)
    f_opts = {
        "n_dims": 2,
        "perplexity": 30,
        "eta": 200,
        "ker": "rbf",
        "gamma": 0.5,
        "p_dims": 50,
        "p_degree": 3
    }
    tsne = Ktsne(data, f_opts)
    reduced_data = tsne.get_solution(steps=1000)
    print("Reduced data shape:", reduced_data.shape)