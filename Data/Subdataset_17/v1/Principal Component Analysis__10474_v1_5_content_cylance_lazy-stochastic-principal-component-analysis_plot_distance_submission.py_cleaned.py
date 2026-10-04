import numpy as np
import matplotlib.pyplot as plt
from matplotlib.offsetbox import AnchoredText
from matplotlib.patheffects import withStroke
def add_inner_title(title, loc, ax=None, size=None, **kwargs):
    if ax is None:
        ax = plt.gca()
    if size is None:
        size = dict(size=plt.rcParams['legend.fontsize'])
    at = AnchoredText(title, loc=loc, prop=size, pad=0.7, borderpad=0.01, frameon=False, **kwargs)
    ax.add_artist(at)
    at.txt._text.set_path_effects([withStroke(foreground="w", linewidth=3)])
    return at
row2name = {0: "subspace_distance", 1: "Steifel_distance"}
col2k = {0: 100, 1: 2000}
lab = {(0, 0): "(a)", (0, 1): "(b)", (1, 0): "(c)", (1, 1): "(d)"}
projection_algorithms = ['alg1', 'alg2', 'alg3', 'alg4', 'alg5']
fig, axs = plt.subplots(nrows=2, ncols=2)
ims = [[None, None], [None, None]]
for i in range(2):
    for j in range(2):
        name, k = row2name[i], col2k[j]
        mat = np.loadtxt(f"{name}/{name}__k_{k}.txt")
        im = axs[i][j].matshow(np.log10(mat))
        ims[i][j] = im
        plt.sca(axs[i][j])
        if i == 0:
            plt.xticks(np.arange(mat.shape[0]), projection_algorithms, rotation="vertical")
        else:
            plt.xticks([])
        if j == 0:
            plt.yticks(np.arange(mat.shape[0]), projection_algorithms)
        else:
            plt.yticks([])
        add_inner_title(lab[(i, j)], loc=2, ax=axs[i][j])
        fig.colorbar(ims[i][j], ax=axs[i][j])
plt.subplots_adjust(wspace=0, hspace=0.1)
plt.savefig("subspace_distance.pdf", bbox_inches="tight")
plt.show()