import numpy as np
from time import time
from vptree import VPnode
from quadtree import Quadnode
from tsne import TSNE
class BH_TSNE(TSNE):
    def __init__(self, bh_threshold=0.5, *args, **kwargs):
        self.bh_threshold = bh_threshold
        super(BH_TSNE, self).__init__(*args, **kwargs)
        self.cost_min_since_max = 0
    def _set_affin_hd(self):
        affin = np.zeros((self.n_samples, self.n_samples))
        time0 = time()
        print("Constructing a Vantage-point tree...")
        root = VPnode(np.arange(self.n_samples), self.data)
        print("VP tree constructed. Time elapsed: {:.2f} s".format(time() - time0))
        n_neighbors = int(3 * self.perplexity)
        distances = np.empty(n_neighbors)
        for ii in range(self.n_samples):
            neighbors = np.zeros(n_neighbors, dtype=int)
            distances.fill(np.inf)
            root.find_neighbors(ii, neighbors, distances, self.data)
            affin[ii, neighbors] = self._affin_bin_search_sigma(distances)
        affin = (affin + affin.T) / (2. * self.n_samples)
        self.affin_hd = affin
    def _set_gradient(self):
        yy, xx = np.median(self.coord, axis=0)
        width = np.max(self.coord) - np.min(self.coord)
        qdroot = Quadnode(self.coord, xx, yy, width * 2.)
        diffs = self.coord[:, np.newaxis, :] - self.coord[np.newaxis, :, :]
        F_attr = np.sum((self.affin_hd[:, :, np.newaxis] / (1. + np.sum(diffs**2, axis=2))[:, :, np.newaxis]) * diffs, axis=1)
        F_rep = np.empty_like(F_attr)
        student_sum = 0.
        for ii in range(self.n_samples):
            summary = qdroot.summarize(self.coord[ii, :], self.bh_threshold)
            F_rep[ii, :] = summary[0]
            student_sum += summary[1]
        F_rep /= student_sum
        self.gradient = 4. * (F_attr + F_rep)
