import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
def load_and_clean_data(url):
    data = pd.read_csv(url)
    data_cleaned = data.dropna(axis=1)
    data_cleaned = data_cleaned.iloc[:, 7:]
    return data_cleaned
def preprocess_data(data):
    features = data.iloc[:, :-1].values
    labels = data.iloc[:, -1].values
    scaler = StandardScaler()
    features_scaled = scaler.fit_transform(features)
    label_encoder = LabelEncoder()
    labels_encoded = label_encoder.fit_transform(labels)
    x_train, x_test, y_train, y_test = train_test_split(
        features_scaled, labels_encoded, test_size=0.1, random_state=0
    )
    return x_train, x_test, y_train, y_test
def visualize_tsne(x_test, y_test):
    tsne = TSNE(n_components=2, random_state=0)
    x_test_2d = tsne.fit_transform(x_test)
    markers = ['s', 'd', 'o', '^', 'v']
    colors = ['red', 'blue', 'lightgreen', 'purple', 'cyan']
    unique_classes = np.unique(y_test)
    plt.figure(figsize=(8, 6))
    for idx, class_label in enumerate(unique_classes):
        plt.scatter(
            x=x_test_2d[y_test == class_label, 0],
            y=x_test_2d[y_test == class_label, 1],
            c=colors[idx], marker=markers[idx], label=class_label
        )
    plt.xlabel('t-SNE Component 1')
    plt.ylabel('t-SNE Component 2')
    plt.legend(loc='upper left')
    plt.title('t-SNE Visualization of Test Data')
    plt.show()
def main():
    data_url = "https:
    cleaned_data = load_and_clean_data(data_url)
    x_train, x_test, y_train, y_test = preprocess_data(cleaned_data)
    visualize_tsne(x_test, y_test)
if __name__ == "__main__":
    main()