import time
import data
import tsne
import bh_tsne
import matplotlib.pyplot as plt
def fonk1(image_file, label_file, b1 = 1000):
    b3, b2 = data.read_MNIST(image_file, label_file)
    b3 = b3[:b1] / 255.0
    b2 = b2[:b1]
    return b3, b2
def fonk2(b3, b2, b4 = False, max_iter=1000, b6=False):
    if b4:
        b5 = bh_tsne.BH_TSNE(max_iter=max_iter, bh_threshold=0.5)
    else:
        b5 = tsne.TSNE(max_iter=max_iter)
    b5.fit(b3, b6 = b6, b2=b2, anim_file="tsne_movie.mp4" if b6 else None)
    return b5
def fonk3(b5, b2):
    fig, b7 = plt.subplots()
    b5.plot_embedding2D(b2, b7)
    plt.show()
def fonk4():
    b8 = time.time()
    print("Loading data...")
    b9 = "MNIST/train-b3.idx3-ubyte"
    b10 = "MNIST/train-b2.idx1-ubyte"
    b12, b11 = fonk1(b9, b10)
    b12 = tsne.get_pca_proj(b12, n_components=30)
    print(f"Data loaded and preprocessed. Time elapsed: {time.time() - b8:.2f} seconds")
    b6 = False
    b4 = False
    if b6:
        import matplotlib
        matplotlib.use("Agg")
    b5 = fonk2(b12, b11, b4=b4, max_iter=1000, b6=b6)
    print(f"t-SNE completed. Total time: {time.time() - b8:.2f} seconds")
    if not b6:
        fonk3(b5, b11)
if b13 = = "__main__":
    fonk4()