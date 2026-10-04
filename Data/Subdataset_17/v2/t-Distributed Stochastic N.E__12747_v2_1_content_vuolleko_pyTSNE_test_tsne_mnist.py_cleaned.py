import time
import data
import tsne
import bh_tsne
import matplotlib.pyplot as plt
def load_mnist_data(image_file, label_file, n_samples=1000):
    images, labels = data.read_MNIST(image_file, label_file)
    images = images[:n_samples] / 255.0
    labels = labels[:n_samples]
    return images, labels
def run_tsne(images, labels, use_bh_tsne=False, max_iter=1000, animate=False):
    if use_bh_tsne:
        vis = bh_tsne.BH_TSNE(max_iter=max_iter, bh_threshold=0.5)
    else:
        vis = tsne.TSNE(max_iter=max_iter)
    vis.fit(images, animate=animate, labels=labels, anim_file="tsne_movie.mp4" if animate else None)
    return vis
def plot_embedding(vis, labels):
    fig, ax = plt.subplots()
    vis.plot_embedding2D(labels, ax)
    plt.show()
def main():
    start_time = time.time()
    print("Loading data...")
    filename_train_images = "MNIST/train-images.idx3-ubyte"
    filename_train_labels = "MNIST/train-labels.idx1-ubyte"
    images_train, labels_train = load_mnist_data(filename_train_images, filename_train_labels)
    images_train = tsne.get_pca_proj(images_train, n_components=30)
    print(f"Data loaded and preprocessed. Time elapsed: {time.time() - start_time:.2f} seconds")
    animate = False
    use_bh_tsne = False
    if animate:
        import matplotlib
        matplotlib.use("Agg")
    vis = run_tsne(images_train, labels_train, use_bh_tsne=use_bh_tsne, max_iter=1000, animate=animate)
    print(f"t-SNE completed. Total time: {time.time() - start_time:.2f} seconds")
    if not animate:
        plot_embedding(vis, labels_train)
if __name__ == "__main__":
    main()