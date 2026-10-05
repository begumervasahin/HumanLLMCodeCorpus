import numpy as np
import pandas as pd
from collections import defaultdict
from sklearn import datasets
def cosine_similarity(u, v):
    cosine = np.inner(u, v) / (np.linalg.norm(u) * np.linalg.norm(v))
    return cosine
def nearest_neighbors(train, test, Y_train, n_neighbors=5):
    predictions = []
    for test_instance in test:
        distances = {}
        for idx, train_instance in enumerate(train):
            distance_metric = cosine_similarity(train_instance, test_instance)
            distances[idx] = distance_metric
        sorted_distances = sorted(distances.items(), key=lambda x: x[1], reverse=True)
        neighbors_indices = [i[0] for i in sorted_distances[:n_neighbors]]
        neighbors_targets = [Y_train[idx] for idx in neighbors_indices]
        target_counts = defaultdict(int)
        for target in neighbors_targets:
            target_counts[target] += 1
        most_common_target = max(target_counts, key=target_counts.get)
        predictions.append(most_common_target)
    return predictions
def main():
    iris_data = datasets.load_iris()
    iris_df = pd.DataFrame(iris_data.data, columns=iris_data.feature_names)
    iris_df['target'] = iris_data.target
    iris_accuracy_list = []
    for _ in range(20):
        shuffled_iris_df = iris_df.sample(frac=1).reset_index(drop=True)
        Y_iris = np.array(shuffled_iris_df['target'])
        X_iris = np.array(shuffled_iris_df.drop('target', axis=1))
        train_iris = X_iris[:120]
        Y_train_iris = Y_iris[:120]
        test_iris = X_iris[120:]
        Y_iris_true = Y_iris[120:]
        Y_iris_predict = nearest_neighbors(train_iris, test_iris, Y_train_iris, n_neighbors=5)
        accuracy_iris = np.mean(Y_iris_predict == Y_iris_true) * 100
        iris_accuracy_list.append(accuracy_iris)
    print("Average accuracy for Iris dataset:", np.mean(iris_accuracy_list))
    wine_data = pd.read_csv("redwinequality.csv")
    wine_accuracy_list = []
    fuzzy_accuracy_list = []
    for _ in range(20):
        shuffled_wine_data = wine_data.sample(frac=1).reset_index(drop=True)
        Y_wine = np.array(shuffled_wine_data['quality'])
        X_wine = np.array(shuffled_wine_data.drop('quality', axis=1))
        train_wine = X_wine[:1500]
        Y_train_wine = Y_wine[:1500]
        test_wine = X_wine[1500:1600]
        Y_wine_true = Y_wine[1500:1600]
        Y_wine_predict = nearest_neighbors(train_wine, test_wine, Y_train_wine, n_neighbors=5)
        accuracy_wine = np.mean(Y_wine_predict == Y_wine_true) * 100
        wine_accuracy_list.append(accuracy_wine)
        fuzzy_accuracy = np.mean(np.abs(Y_wine_predict - Y_wine_true) < 2) * 100
        fuzzy_accuracy_list.append(fuzzy_accuracy)
    print("Average strict accuracy for Wine dataset:", np.mean(wine_accuracy_list))
    print("Average fuzzy accuracy for Wine dataset:", np.mean(fuzzy_accuracy_list))
if __name__ == "__main__":
    main()