import numpy as np
from time import time
from vptree import VPnode
from quadtree import Quadnode
from tsne import TSNE
class class1(TSNE):
    def fonk1(self, b1 = 0.5, *args, **kwargs):
        self.b1 = b1
        super().fonk1(*args, **kwargs)
        self.a1 = 0
    def fonk2(self):
        b2 = np.zeros((self.n_samples, self.n_samples))
        b3 = time()
        print("Constructing a Vantage-point tree...")
        b4 = VPnode(np.arange(self.n_samples), self.data)
        b5 = time() - b3
        print(f"VP-tree constructed in {b5:.2f} seconds.")
        b6 = int(3 * self.perplexity)
        b7 = np.full(b6, np.inf)
        for i in range(self.n_samples):
            b8 = np.zeros(b6, dtype=int)
            b4.find_neighbors(i, b8, b7, self.data)
            b2[i, b8] = self._affin_bin_search_sigma(b7)
        b2 = (b2 + b2.T) / (2.0 * self.n_samples)
        self.b9 = b2
    def fonk3(self):
        center_y, b10 = np.median(self.coord, b15=0)
        b11 = 2.0 * (np.max(self.coord) - np.min(self.coord))
        b12 = Quadnode(self.coord, b10, center_y, b11)
        b13 = self.coord[:, np.newaxis, :] - self.coord[np.newaxis, :, :]
        b14 = np.sum(
            (self.b9[:, :, np.newaxis] / (1.0 + np.sum(b13 ** 2, b15 = 2))[:, :, np.newaxis]) * b13,
            b15 = 1
        )
        b16 = np.empty_like(b14)
        a2 = 0.0
        for i in range(self.n_samples):
            b17 = b12.summarize(self.coord[i, :], self.b1)
            b16[i, :] = b17[0]
            a2 += b17[1]
        b16 /= a2
        self.b18 = 4.0 * (b14 + b16)
