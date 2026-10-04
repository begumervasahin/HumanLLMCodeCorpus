import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
def load_and_preview_data(url):
    data = pd.read_csv(url)
    print("Initial Data Preview:")
    print(data.head())
    return data
def clean_data(data):
    columns_without_null = data.columns[data.isnull().sum() == 0]
    data_cleaned = data[columns_without_null]
    data_cleaned = data_cleaned.iloc[:, 7:]
    print("\nRemaining Columns After Cleaning:")
    print(data_cleaned.columns)
    return data_cleaned
def preprocess_data(data):
    X = data.iloc[:, :-1].values
    y = data.iloc[:, -1].values
    scaler = StandardScaler()
    X_standardized = scaler.fit_transform(X)
    label_encoder = LabelEncoder()
    y_encoded = label_encoder.fit_transform(y)
    print("\nClass Labels:")
    print(np.unique(y))
    X_train, X_test, y_train, y_test = train_test_split(X_standardized, y_encoded, test_size=0.1, random_state=0)
    return X_train, X_test, y_train, y_test, label_encoder
def visualize_tsne(X_test, y_test, label_encoder):
    tsne = TSNE(n_components=2, random_state=0)
    X_test_2d = tsne.fit_transform(X_test)
    markers = ['s', 'd', 'o', '^', 'v']
    colors = ['red', 'blue', 'lightgreen', 'purple', 'cyan']
    color_map = dict(zip(np.unique(y_test), colors))
    plt.figure(figsize=(10, 8))
    for idx, class_label in enumerate(np.unique(y_test)):
        plt.scatter(X_test_2d[y_test == class_label, 0], X_test_2d[y_test == class_label, 1],
                    c=color_map[class_label], marker=markers[idx],
                    label=label_encoder.inverse_transform([class_label])[0])
    plt.xlabel('t-SNE Component 1')
    plt.ylabel('t-SNE Component 2')
    plt.legend(loc='upper left')
    plt.title('t-SNE Visualization of Test Data')
    plt.show()
def main():
    data_url = "https:
    data = load_and_preview_data(data_url)
    data_cleaned = clean_data(data)
    X_train, X_test, y_train, y_test, label_encoder = preprocess_data(data_cleaned)
    visualize_tsne(X_test, y_test, label_encoder)
if __name__ == "__main__":
    main()