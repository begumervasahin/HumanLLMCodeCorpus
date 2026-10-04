import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn import preprocessing
import matplotlib.pyplot as plt
def load_and_preprocess_data(file_path):
    data_with_nan = pd.read_csv(file_path)
    data_cleaned = data_with_nan.dropna()
    data = data_cleaned.iloc[:, 1:]
    scaled_data = preprocessing.scale(data.T)
    return scaled_data
def perform_tsne(scaled_data, n_components=2, n_iter=2500, random_state=0):
    tsne = TSNE(n_components=n_components, n_iter=n_iter, random_state=random_state)
    tsne_data = tsne.fit_transform(scaled_data)
    return tsne_data
def plot_tsne(tsne_data):
    plt.scatter(tsne_data[:, 0], tsne_data[:, 1])
    plt.xlabel('t-SNE Component 1')
    plt.ylabel('t-SNE Component 2')
    plt.title('2D t-SNE Visualization')
    plt.show()
def main():
    file_path = 'endometrial.csv'
    scaled_data = load_and_preprocess_data(file_path)
    tsne_data = perform_tsne(scaled_data)
    plot_tsne(tsne_data)
if __name__ == "__main__":
    main()