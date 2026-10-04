import matplotlib.pyplot as plt
import numpy as np
from matplotlib.offsetbox import AnchoredText
from matplotlib.patheffects import withStroke
def fonk1(title, b17, b1 = None, b2=None, **kwargs):
    if b1 is None:
        b1 = plt.gca()
    if b2 is None:
        b2 = dict(b2=plt.rcParams['legend.fontsize'])
    b3 = AnchoredText(title, b17=b17, prop=b2, pad=0.7, borderpad=0.01, frameon=False, **kwargs)
    b1.add_artist(b3)
    b3.txt._text.set_path_effects([withStroke(b4 = "w", linewidth=3)])
    return b3
fig, b5 = plt.subplots(nrows=2, ncols=2)
b6 = {0: "subspace_distance", 1: "Steifel_distance"}
b7 = {0: 100, 1: 2000}
b8 = {(0, 0): "(a)", (0, 1): "(b)", (1, 0): "(c)", (1, 1): "(d)"}
b9 = projection_algorithms
b10 = [[None, None], [None, None]]
for b14 in range(2):
    for b16 in range(2):
        name, b11 = b6[b14], b7[b16]
        b12 = np.loadtxt(f"{name}/{name}__k_{b11}.txt")
        b13 = b5[b14][b16].matshow(np.log10(b12))
        b10[b14][b16] = b13
        plt.sca(b5[b14][b16])
        if b14 = = 0:
            plt.xticks(np.arange(b12.shape[0]), b9, b15 = "vertical")
        else:
            plt.xticks([])
        if b16 = = 0:
            plt.yticks(np.arange(b12.shape[0]), b9)
        else:
            plt.yticks([])
        fonk1(b8[(b14, b16)], b17 = 2, b1=b5[b14][b16])
        fig.colorbar(b10[b14][b16], b1 = b5[b14][b16])
plt.subplots_adjust(b18 = 0, hspace=0.1)
plt.savefig("subspace_distance.pdf", b19 = "tight")