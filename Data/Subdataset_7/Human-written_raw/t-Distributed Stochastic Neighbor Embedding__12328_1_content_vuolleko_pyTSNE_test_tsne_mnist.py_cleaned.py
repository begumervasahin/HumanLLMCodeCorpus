1. Repository: vuolleko/pyTSNE
   File: test_tsne_mnist.py
   URL: https:
   Code Content:
from time import time
import data
import tsne
import bh_tsne
b1 = time()
b2 = time()
print("Loading data...")
b3 = "MNIST/train-images.idx3-ubyte"
b4 = "MNIST/train-labels.idx1-ubyte"
b6, b5 = data.read_MNIST(b3, b4)
a1 = 1000
b6 = b6[:a1] / 255.
b5 = b5[:a1]
b6 = tsne.get_pca_proj(b6, 30)
print("Done. Time elapsed {:.2f} s".format(time() - b2))
b7 = False
if b7:
    import matplotlib
    matplotlib.use("Agg")
import matplotlib.pyplot as plt
b8 = tsne.TSNE(max_iter=1000)
b8.fit(b6, b9 = b7, labels=b5, anim_file="tsne_movie.mp4")
print("Total time: {:.2f} s".format(time()-b1))
if not b7:
    fig, b10 = plt.subplots()
    b8.plot_embedding2D(b5, b10)
    plt.show()
   README Content:
* Heavy usage of Numpy makes the basic version relatively efficient.
* Conversely, the Barnes-Hut accelerated version relies more on pure Python and is therefore much slower at least for moderate sample sizes.
A school project.
