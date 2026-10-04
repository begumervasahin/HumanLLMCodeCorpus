
import numpy as np
import pandas as pd
from collections import defaultdict
from sklearn import datasets
from sklearn.model_selection import train_test_split
from operator import itemgetter
def cosine_similarity(u, v):
    return np.inner(u, v) / (np.linalg.norm(u) * np.linalg.norm(v))
def nearest_neighbors(train, test, y_train, n_neighbors=5):
    predictions = []
    for test_sample in test:
        distances = {i: cosine_similarity(train_sample, test_sample)
                     for i, train_sample in enumerate(train)}
        sorted_neighbors = sorted(distances.items(), key=itemgetter(1), reverse=True)[:n_neighbors]
        neighbor_targets = [y_train[neighbor[0]] for neighbor in sorted_neighbors]
        target_count = defaultdict(int)
        for target in neighbor_targets:
            target_count[target] += 1
        predicted_target = max(target_count.items(), key=itemgetter(1))[0]
        predictions.append(predicted_target)
    return predictions
def evaluate_accuracy(predictions, true_labels):
    return np.mean(np.array(predictions) == true_labels) * 100
def load_iris_dataset():
    iris_data = datasets.load_iris()
    iris_df = pd.DataFrame(iris_data.data, columns=iris_data.feature_names)
    iris_df['target'] = iris_data.target
    return iris_df
def load_wine_dataset(file_path):
    wine_data = pd.read_csv(file_path)
    return wine_data
def main():
    iris_df = load_iris_dataset()
    iris_accuracies = []
    for _ in range(20):
        shuffled_df = iris_df.sample(frac=1).reset_index(drop=True)
        X_iris = shuffled_df.drop('target', axis=1).values
        y_iris = shuffled_df['target'].values
        X_train, X_test, y_train, y_test = train_test_split(X_iris, y_iris, test_size=0.2, random_state=None)
        y_pred = nearest_neighbors(X_train, X_test, y_train, n_neighbors=5)
        iris_accuracies.append(evaluate_accuracy(y_pred, y_test))
    print(f"Average accuracy for Iris dataset: {np.mean(iris_accuracies):.2f}%")
    wine_data = load_wine_dataset("redwinequality.csv")
    wine_accuracies = []
    wine_fuzzy_accuracies = []
    for _ in range(20):
        shuffled_df = wine_data.sample(frac=1).reset_index(drop=True)
        X_wine = shuffled_df.drop('quality', axis=1).values
        y_wine = shuffled_df['quality'].values
        X_train, X_test, y_train, y_test = train_test_split(X_wine, y_wine, test_size=0.1, random_state=None)
        y_pred = nearest_neighbors(X_train, X_test, y_train, n_neighbors=5)
        wine_accuracies.append(evaluate_accuracy(y_pred, y_test))
        fuzzy_accuracy = np.mean(np.abs(np.array(y_pred) - y_test) < 2) * 100
        wine_fuzzy_accuracies.append(fuzzy_accuracy)
    print(f"Average strict accuracy for Red Wine dataset: {np.mean(wine_accuracies):.2f}%")
    print(f"Average fuzzy accuracy for Red Wine dataset: {np.mean(wine_fuzzy_accuracies):.2f}%")
if __name__ == '__main__':
    main()