1. Repository: vuolleko/pyTSNE
   File: bh_tsne.py
   URL: https:
   Code Content:
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
        print("VP done. Time elapsed {:.2f} s".format(time() - b3))
        b5 = 3 * self.perplexity
        b6 = np.empty(b5)
        for ii in range(self.n_samples):
            b7 = np.arange(b5)
            b6[:] = np.inf
            b4.find_neighbors(ii, b7, b6, self.data)
            b2[ii, b7] = self._affin_bin_search_sigma(b6)
        b2 = (b2 + b2.T) / (2. * self.n_samples)
        self.b8 = b2
    def fonk3(self):
        yy, b9 = np.median(self.coord, b14=0)
        b10 = np.max(self.coord) - np.min(self.coord)
        b11 = Quadnode(self.coord, b9, yy, b10 * 2.)
        b12 = self.coord - self.coord[:, np.newaxis]
        b13 = np.sum( (self.b8 / (1. + np.sum(b12**2., b14=2)) )[:, :, np.newaxis]
                         * b12, b14 = 1)
        b15 = np.empty_like(b13)
        a2 = 0.
        for ii in range(self.n_samples):
            b16 = b11.summarize(self.coord[ii, :], self.b1)
            b15[ii, :] = b16[0]
            a2 += b16[1]
        b15 /= a2
        self.b17 = 4. * (b13 + b15)
   README Content:
* Heavy usage of Numpy makes the basic version relatively efficient.
* Conversely, the Barnes-Hut accelerated version relies more on pure Python and is therefore much slower at least for moderate sample sizes.
A school project.
