from time import time
import matplotlib.pyplot as plt
import data
import tsne
def fonk1():
    b1 = time()
    print("Loading data...")
    b2 = "MNIST/train-images.idx3-ubyte"
    b3 = "MNIST/train-labels.idx1-ubyte"
    b5, b4 = data.read_MNIST(b2, b3)
    a1 = 1000
    b5 = b5[:a1] / 255.
    b4 = b4[:a1]
    b5 = tsne.get_pca_proj(b5, 30)
    print("Data loading completed. Time elapsed: {:.2f} s".format(time() - b1))
    b6 = False
    if b6:
        import matplotlib
        matplotlib.use("Agg")
    b7 = tsne.TSNE(max_iter=1000)
    b7.fit(b5, b8 = b6, labels=b4, anim_file="tsne_movie.mp4")
    print("Total execution time: {:.2f} s".format(time() - b1))
    if not b6:
        fig, b9 = plt.subplots()
        b7.plot_embedding2D(b4, b9)
        plt.show()
if b10 = = "__main__":
    fonk1()