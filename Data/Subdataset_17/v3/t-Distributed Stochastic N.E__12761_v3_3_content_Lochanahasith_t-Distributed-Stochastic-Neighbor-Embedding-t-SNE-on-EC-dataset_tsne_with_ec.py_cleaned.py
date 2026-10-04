import pandas as pd
import numpy as np
from sklearn.manifold import TSNE
from sklearn.preprocessing import scale
import matplotlib.pyplot as plt
def load_and_preprocess_data(file_path):
    data = pd.read_csv(file_path)
    data_cleaned = data.dropna()
    features = data_cleaned.iloc[:, 1:]
    scaled_features = scale(features.T)
    return scaled_features
def perform_tsne(scaled_data, n_components=2, n_iter=2500, random_state=0):
    tsne = TSNE(n_components=n_components, n_iter=n_iter, random_state=random_state)
    tsne_result = tsne.fit_transform(scaled_data)
    return tsne_result
def plot_tsne(tsne_data):
    plt.figure(figsize=(10, 8))
    plt.scatter(tsne_data[:, 0], tsne_data[:, 1], alpha=0.6, edgecolor='k')
    plt.xlabel('t-SNE Component 1')
    plt.ylabel('t-SNE Component 2')
    plt.title('2D t-SNE Visualization')
    plt.grid(True)
    plt.show()
def main():
    file_path = 'endometrial.csv'
    scaled_data = load_and_preprocess_data(file_path)
    tsne_result = perform_tsne(scaled_data)
    plot_tsne(tsne_result)
if __name__ == "__main__":
    main()