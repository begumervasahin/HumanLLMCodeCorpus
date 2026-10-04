import numpy as np
from time import time
from vptree import VPnode
from quadtree import Quadnode
from tsne import TSNE
class class1(TSNE):
    def fonk1(self, b1 = 0.5, *args, **kwargs):
        self.b1 = b1
        super(class1, self).fonk1(*args, **kwargs)
        self.a1 = 0
    def fonk2(self):
        b2 = np.zeros((self.n_samples, self.n_samples))
        b3 = time()
        print("Constructing a Vantage-point tree...")
        b4 = VPnode(np.arange(self.n_samples), self.data)
        print("VP tree constructed. Time elapsed: {:.2f} s".format(time() - b3))
        b5 = int(3 * self.perplexity)
        b6 = np.empty(b5)
        for ii in range(self.n_samples):
            b7 = np.zeros(b5, dtype=int)
            b6.fill(np.inf)
            b4.find_neighbors(ii, b7, b6, self.data)
            b2[ii, b7] = self._affin_bin_search_sigma(b6)
        b2 = (b2 + b2.T) / (2. * self.n_samples)
        self.b8 = b2
    def fonk3(self):
        yy, b9 = np.median(self.coord, axis=0)
        b10 = np.max(self.coord) - np.min(self.coord)
        b11 = Quadnode(self.coord, b9, yy, b10 * 2.)
        b12 = self.coord[:, np.newaxis, :] - self.coord[np.newaxis, :, :]
        b13 = np.sum((self.b8[:, :, np.newaxis] / (1. + np.sum(b12**2, axis=2))[:, :, np.newaxis]) * b12, axis=1)
        b14 = np.empty_like(b13)
        a2 = 0.
        for ii in range(self.n_samples):
            b15 = b11.summarize(self.coord[ii, :], self.b1)
            b14[ii, :] = b15[0]
            a2 += b15[1]
        b14 /= a2
        self.b16 = 4. * (b13 + b14)
