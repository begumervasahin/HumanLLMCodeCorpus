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
        print(f"VP-tree constructed. Time elapsed: {time() - b3:.2f} seconds.")
        b5 = int(3 * self.perplexity)
        b6 = np.full(b5, np.inf)
        for i in range(self.n_samples):
            b7 = np.zeros(b5, dtype=int)
            b4.find_neighbors(i, b7, b6, self.data)
            b2[i, b7] = self._affin_bin_search_sigma(b6)
        b2 = (b2 + b2.T) / (2.0 * self.n_samples)
        self.b8 = b2
    def fonk3(self):
        center_y, b9 = np.median(self.coord, b14=0)
        b10 = np.max(self.coord) - np.min(self.coord)
        b11 = Quadnode(self.coord, b9, center_y, b10 * 2.0)
        b12 = self.coord[:, np.newaxis, :] - self.coord[np.newaxis, :, :]
        b13 = np.sum(
            (self.b8[:, :, np.newaxis] / (1.0 + np.sum(b12 ** 2, b14 = 2))[:, :, np.newaxis])
            * b12, b14 = 1
        )
        b15 = np.empty_like(b13)
        a2 = 0.0
        for i in range(self.n_samples):
            b16 = b11.summarize(self.coord[i, :], self.b1)
            b15[i, :] = b16[0]
            a2 += b16[1]
        b15 /= a2
        self.b17 = 4.0 * (b13 + b15)
