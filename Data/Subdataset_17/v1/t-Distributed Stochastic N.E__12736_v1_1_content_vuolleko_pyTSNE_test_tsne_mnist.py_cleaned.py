import time
import data
import tsne
import bh_tsne
import matplotlib.pyplot as plt
def main():
    start_time = time.time()
    print("Loading data...")
    filename_train_images = "MNIST/train-images.idx3-ubyte"
    filename_train_labels = "MNIST/train-labels.idx1-ubyte"
    images_train, labels_train = data.read_MNIST(filename_train_images, filename_train_labels)
    n_samples = 1000
    images_train = images_train[:n_samples] / 255.0
    labels_train = labels_train[:n_samples]
    images_train = tsne.get_pca_proj(images_train, n_components=30)
    print(f"Done. Time elapsed: {time.time() - start_time:.2f} seconds")
    animate = False
    if animate:
        import matplotlib
        matplotlib.use("Agg")
    vis = tsne.TSNE(max_iter=1000)
    vis.fit(images_train, animate=animate, labels=labels_train, anim_file="tsne_movie.mp4")
    print(f"Total time: {time.time() - start_time:.2f} seconds")
    if not animate:
        fig, ax = plt.subplots()
        vis.plot_embedding2D(labels_train, ax)
        plt.show()
if __name__ == "__main__":
    main()