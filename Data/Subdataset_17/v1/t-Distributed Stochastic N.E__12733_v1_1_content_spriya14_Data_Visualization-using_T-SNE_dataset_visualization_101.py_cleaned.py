import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
def load_and_clean_data(url):
    dataframe_all = pd.read_csv(url)
    count_null = dataframe_all.isnull().sum()
    columns_without_null = count_null[count_null == 0].index
    dataframe_cleaned = dataframe_all[columns_without_null]
    dataframe_cleaned = dataframe_cleaned.iloc[:, 7:]
    return dataframe_cleaned
def preprocess_data(dataframe):
    x = dataframe.iloc[:, :-1].values
    standard_scaler = StandardScaler()
    x_std = standard_scaler.fit_transform(x)
    y = dataframe.iloc[:, -1].values
    label_encoder = LabelEncoder()
    y_encoded = label_encoder.fit_transform(y)
    x_train, x_test, y_train, y_test = train_test_split(x_std, y_encoded, test_size=0.1, random_state=0)
    return x_train, x_test, y_train, y_test
def visualize_tsne(x_test, y_test):
    tsne = TSNE(n_components=2, random_state=0)
    x_test_2d = tsne.fit_transform(x_test)
    markers = ('s', 'd', 'o', '^', 'v')
    color_map = {0: 'red', 1: 'blue', 2: 'lightgreen', 3: 'purple', 4: 'cyan'}
    plt.figure()
    for idx, cl in enumerate(np.unique(y_test)):
        plt.scatter(x=x_test_2d[y_test == cl, 0], y=x_test_2d[y_test == cl, 1],
                    c=color_map[idx], marker=markers[idx], label=cl)
    plt.xlabel('X in t-SNE')
    plt.ylabel('Y in t-SNE')
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