from __future__ import division
import numpy as np
from kernels import Kernels
class Ktsne:
    def __init__(self, X, options={}):
        self.dimension = options.get("n_dims", 2)
        self.perplexity = options.get("perplexity", 30)
        self.eta = options.get("eta", 200)
        self.options = options
        self.momentum = 0.4
        self.X = X.copy()
        self.P = None
        self.Q = None
        self.iteration = 0
        self.Y = None
        self.dY = None
        self.Y_t = np.zeros((2,) + self.X.shape)
        np.seterr(divide='ignore', invalid='ignore')
    def reduce_X(self):
        kernel_options = {
            "kernel": self.options.get("ker", "pca"),
            "gamma": self.options.get("gamma", 0.5),
            "degree": self.options.get("p_degree", 1),
            "p_dims": self.options.get("p_dims", 4)
        }
        kn = Kernels(self.X.copy(), k_opts=kernel_options)
        self.X = kn.process_data()
    def L1_distance(self, X):
        return np.sum(np.abs(X[:, None] - X[None, :], axis=-1))
    def L2_distance(self, X):
        return np.sum((X[:, None] - X[None, :]) ** 2, axis=-1)
    def binary_search(self, distance_row, target, tolerance=1e-2, max_iterations=1000, lower_bound=1e-10, upper_bound=1e3):
        for _ in range(max_iterations):
            estimated_sigma = (lower_bound + upper_bound) / 2.
            probability_row = np.exp(- (distance_row) / estimated_sigma)
            probability_row /= np.sum(probability_row)
            entropy_value = self.entropy(probability_row)
            difference = np.abs(entropy_value - target)
            if difference <= tolerance:
                break
            if entropy_value > target:
                upper_bound = estimated_sigma
            else:
                lower_bound = estimated_sigma
        return probability_row, estimated_sigma
    def entropy(self, probability_row):
        return -np.sum(probability_row * np.log2(probability_row))
    def compute_P(self):
        n, d = self.X.shape
        P = np.zeros((n, n))
        sigmas = np.ones((n, 1))
        distance_matrix = self.L2_distance(self.X)
        target_entropy = np.log2(self.perplexity)
        for i in range(n):
            distance_row = distance_matrix[i, np.hstack((np.arange(0, i), np.arange(i+1, n)))]
            probability_row, estimated_sigma = self.binary_search(distance_row, target_entropy)
            P[i, np.hstack((np.arange(0, i), np.arange(i+1, n)))] = probability_row
            sigmas[i] = estimated_sigma
        mean_sigma = np.mean(np.sqrt(1 / sigmas))
        print("Mean value of sigma: ", mean_sigma)
        P = (P + P.T) / (2 * n)
        P /= np.sum(P)
        P = np.maximum(P, 1e-12)
        return P
    def compute_Q(self):
        distance_matrix = self.L2_distance(self.Y)
        Q = 1 / (1 + distance_matrix)
        np.fill_diagonal(Q, 0)
        self.Q = Q / np.sum(Q)
        self.Q = np.maximum(self.Q, 1e-12)
        return Q
    def gradient(self, Q):
        PQ = self.P - self.Q
        M = PQ * Q
        MD = 4 * (np.diag(np.sum(M, 1)) - M)
        self.dY = np.dot(MD, self.Y)
    def get_solution(self, steps=500):
        self.reduce_X()
        self.P = self.compute_P()
        self.P *= 10.
        for i in range(steps):
            cost = self.step()
            if i % 500 == 0:
                print("Iteration ", i, ": cost is ", cost)
        print("Cost:", cost)
        self.Y -= np.mean(self.Y, 0)
        return self.Y
    def step(self):
        Q = self.compute_Q()
        self.gradient(Q)
        if self.iteration == 100:
            self.P /= 10.
        if self.iteration == 25:
            self.momentum = .8
        self.Y -= self.eta * self.dY
        self.Y += self.momentum * np.diff(self.Y_t, axis=0)[0]
        self.Y_t[1] = self.Y_t[0].copy()
        self.Y_t[0] = self.Y
        cost = np.sum(self.P * np.log(self.P / self.Q))
        self.iteration += 1
        return cost