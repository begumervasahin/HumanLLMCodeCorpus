import time
import data
import tsne
import bh_tsne
import matplotlib.pyplot as plt
def fonk1():
    b1 = time.time()
    print("Loading data...")
    b2 = "MNIST/train-images.idx3-ubyte"
    b3 = "MNIST/train-labels.idx1-ubyte"
    b5, b4 = data.read_MNIST(b2, b3)
    a1 = 1000
    b5 = b5[:a1] / 255.0
    b4 = b4[:a1]
    b5 = tsne.get_pca_proj(b5, n_components=30)
    print(f"Done. Time elapsed: {time.time() - b1:.2f} seconds")
    b6 = False
    if b6:
        import matplotlib
        matplotlib.use("Agg")
    b7 = tsne.TSNE(max_iter=1000)
    b7.fit(b5, b6 = b6, labels=b4, anim_file="tsne_movie.mp4")
    print(f"Total time: {time.time() - b1:.2f} seconds")
    if not b6:
        fig, b8 = plt.subplots()
        b7.plot_embedding2D(b4, b8)
        plt.show()
if b9 = = "__main__":
    fonk1()