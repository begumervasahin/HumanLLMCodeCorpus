import numpy as np
import matplotlib.pyplot as plt
from matplotlib.offsetbox import AnchoredText
from matplotlib.patheffects import withStroke
def fonk1(title, b18, b1 = None, b2=None, **kwargs):
    if b1 is None:
        b1 = plt.gca()
    if b2 is None:
        b2 = {'b2': plt.rcParams['legend.fontsize']}
    b3 = AnchoredText(title, b18=b18, prop=b2, pad=0.7, borderpad=0.01, frameon=False, **kwargs)
    b1.add_artist(b3)
    b3.txt._text.set_path_effects([withStroke(b4 = "w", linewidth=3)])
    return b3
b5 = {0: "subspace_distance", 1: "Steifel_distance"}
b6 = {0: 100, 1: 2000}
b7 = {(0, 0): "(a)", (0, 1): "(b)", (1, 0): "(c)", (1, 1): "(d)"}
b8 = ['alg1', 'alg2', 'alg3', 'alg4', 'alg5']
fig, b9 = plt.subplots(nrows=2, ncols=2)
b10 = [[None, None], [None, None]]
for b15 in range(2):
    for b17 in range(2):
        b11 = b5[b15]
        b12 = b6[b17]
        b13 = np.loadtxt(f"{b11}/{b11}__k_{b12}.txt")
        b14 = b9[b15][b17].matshow(np.log10(b13))
        b10[b15][b17] = b14
        plt.sca(b9[b15][b17])
        if b15 = = 0:
            plt.xticks(np.arange(b13.shape[0]), b8, b16 = "vertical")
        else:
            plt.xticks([])
        if b17 = = 0:
            plt.yticks(np.arange(b13.shape[0]), b8)
        else:
            plt.yticks([])
        fonk1(b7[(b15, b17)], b18 = 2, b1=b9[b15][b17])
        fig.colorbar(b10[b15][b17], b1 = b9[b15][b17])
plt.subplots_adjust(b19 = 0, hspace=0.1)
plt.savefig("subspace_distance.pdf", b20 = "tight")
plt.show()