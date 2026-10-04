import time
import data
import tsne
import bh_tsne
import matplotlib.pyplot as plt
def load_and_preprocess_data(image_file, label_file, n_samples=1000):
    print("Loading data...")
    images, labels = data.read_MNIST(image_file, label_file)
    images = images[:n_samples] / 255.0
    labels = labels[:n_samples]
    images = tsne.get_pca_proj(images, n_components=30)
    print(f"Data loaded and preprocessed. Samples: {n_samples}")
    return images, labels
def run_tsne(images, labels, use_bh_tsne=False, max_iter=1000, animate=False):
    tsne_model = bh_tsne.BH_TSNE(max_iter=max_iter, bh_threshold=0.5) if use_bh_tsne else tsne.TSNE(max_iter=max_iter)
    tsne_model.fit(images, animate=animate, labels=labels, anim_file="tsne_movie.mp4" if animate else None)
    return tsne_model
def display_embedding(tsne_model, labels):
    fig, ax = plt.subplots()
    tsne_model.plot_embedding2D(labels, ax)
    plt.show()
def main():
    start_time = time.time()
    images_file = "MNIST/train-images.idx3-ubyte"
    labels_file = "MNIST/train-labels.idx1-ubyte"
    images, labels = load_and_preprocess_data(images_file, labels_file)
    animate = False
    use_bh_tsne = False
    if animate:
        import matplotlib
        matplotlib.use("Agg")
    tsne_model = run_tsne(images, labels, use_bh_tsne=use_bh_tsne, max_iter=1000, animate=animate)
    print(f"t-SNE completed. Total time: {time.time() - start_time:.2f} seconds")
    if not animate:
        display_embedding(tsne_model, labels)
if __name__ == "__main__":
    main()