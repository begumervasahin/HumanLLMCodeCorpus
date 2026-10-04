import numpy as np
from time import time
from vptree import VPnode
from quadtree import Quadnode
from tsne import TSNE
class BH_TSNE(TSNE):
    def __init__(self, bh_threshold=0.5, *args, **kwargs):
        self.bh_threshold = bh_threshold
        super().__init__(*args, **kwargs)
        self.cost_min_since_max = 0
    def _set_affin_hd(self):
        affinities = np.zeros((self.n_samples, self.n_samples))
        start_time = time()
        print("Constructing a Vantage-point tree...")
        vp_tree_root = VPnode(np.arange(self.n_samples), self.data)
        elapsed_time = time() - start_time
        print(f"VP-tree constructed in {elapsed_time:.2f} seconds.")
        n_neighbors = int(3 * self.perplexity)
        distances = np.full(n_neighbors, np.inf)
        for i in range(self.n_samples):
            neighbors = np.zeros(n_neighbors, dtype=int)
            vp_tree_root.find_neighbors(i, neighbors, distances, self.data)
            affinities[i, neighbors] = self._affin_bin_search_sigma(distances)
        affinities = (affinities + affinities.T) / (2.0 * self.n_samples)
        self.affin_hd = affinities
    def _set_gradient(self):
        center_y, center_x = np.median(self.coord, axis=0)
        width = 2.0 * (np.max(self.coord) - np.min(self.coord))
        quadtree_root = Quadnode(self.coord, center_x, center_y, width)
        diffs = self.coord[:, np.newaxis, :] - self.coord[np.newaxis, :, :]
        F_attr = np.sum(
            (self.affin_hd[:, :, np.newaxis] / (1.0 + np.sum(diffs ** 2, axis=2))[:, :, np.newaxis]) * diffs,
            axis=1
        )
        F_rep = np.empty_like(F_attr)
        total_student_sum = 0.0
        for i in range(self.n_samples):
            summary = quadtree_root.summarize(self.coord[i, :], self.bh_threshold)
            F_rep[i, :] = summary[0]
            total_student_sum += summary[1]
        F_rep /= total_student_sum
        self.gradient = 4.0 * (F_attr + F_rep)
