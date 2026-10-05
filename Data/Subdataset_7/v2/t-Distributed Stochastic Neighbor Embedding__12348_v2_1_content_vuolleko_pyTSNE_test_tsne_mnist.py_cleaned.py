from time import time
import matplotlib.pyplot as plt
import data
import tsne
def fonk1():
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
    print("Data loading completed. Time elapsed: {:.2f} s".format(time() - b2))
    b7 = False
    if b7:
        import matplotlib
        matplotlib.use("Agg")
    b8 = tsne.TSNE(max_iter=1000)
    b8.fit(b6, b9 = b7, labels=b5, anim_file="tsne_movie.mp4")
    print("Total execution time: {:.2f} s".format(time() - b1))
    if not b7:
        fig, b10 = plt.subplots()
        b8.plot_embedding2D(b5, b10)
        plt.show()
if b11 = = "__main__":
    fonk1()