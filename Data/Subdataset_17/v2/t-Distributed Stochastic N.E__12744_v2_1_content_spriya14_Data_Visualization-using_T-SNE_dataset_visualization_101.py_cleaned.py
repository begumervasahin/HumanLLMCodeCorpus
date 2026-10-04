import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
def load_and_clean_data(url):
    dataframe_all = pd.read_csv(url)
    columns_without_null = dataframe_all.columns[dataframe_all.isnull().sum() == 0]
    dataframe_cleaned = dataframe_all[columns_without_null]
    dataframe_cleaned = dataframe_cleaned.iloc[:, 7:]
    return dataframe_cleaned
def preprocess_data(dataframe):
    x = dataframe.iloc[:, :-1].values
    scaler = StandardScaler()
    x_scaled = scaler.fit_transform(x)
    y = dataframe.iloc[:, -1].values
    encoder = LabelEncoder()
    y_encoded = encoder.fit_transform(y)
    x_train, x_test, y_train, y_test = train_test_split(x_scaled, y_encoded, test_size=0.1, random_state=0)
    return x_train, x_test, y_train, y_test
def visualize_tsne(x_test, y_test):
    tsne = TSNE(n_components=2, random_state=0)
    x_test_2d = tsne.fit_transform(x_test)
    markers = ['s', 'd', 'o', '^', 'v']
    colors = ['red', 'blue', 'lightgreen', 'purple', 'cyan']
    unique_classes = np.unique(y_test)
    plt.figure()
    for idx, class_label in enumerate(unique_classes):
        plt.scatter(x=x_test_2d[y_test == class_label, 0],
                    y=x_test_2d[y_test == class_label, 1],
                    c=colors[idx], marker=markers[idx], label=class_label)
    plt.xlabel('t-SNE component 1')
    plt.ylabel('t-SNE component 2')
    plt.legend(loc='upper left')
    plt.title('t-SNE visualization of test data')
    plt.show()
def main():
    url = "https:
    dataframe_cleaned = load_and_clean_data(url)
    x_train, x_test, y_train, y_test = preprocess_data(dataframe_cleaned)
    visualize_tsne(x_test, y_test)
if __name__ == "__main__":
    main()