import numpy as np
import pandas as pd
from sklearn import datasets
from collections import defaultdict
import operator
def Cos(u, v):
    cosine = np.inner(u, v) / (np.linalg.norm(u) * np.linalg.norm(v))
    return cosine
def nearest_neighbors(train, test, Y_train, n_neighbors=5):
    predict = []
    for m in range(test.shape[0]):
        v = test[m]
        distance = {}
        for i in range(train.shape[0]):
            u = train[i]
            distance_metric = Cos(u, v)
            distance[i] = distance_metric
        distance_sort = sorted(distance.items(), key=operator.itemgetter(1), reverse=True)
        neighbors_id = [distance_sort[i][0] for i in range(n_neighbors) if n_neighbors < len(distance_sort)]
        neighbors_target = [Y_train[item] for item in neighbors_id]
        target_dict = defaultdict(int)
        for i in neighbors_target:
            target_dict[i] += 1
        target_dict_sort = sorted(target_dict.items(), key=operator.itemgetter(1), reverse=True)
        predict_target = target_dict_sort[0][0]
        predict.append(predict_target)
    return predict
def evaluate_accuracy(data, target_name, n_train_samples, n_test_samples, n_trials, fuzzy=False):
    accuracy_list = []
    for i in range(n_trials):
        df = data.sample(frac=1).reset_index(drop=True)
        Y = np.array(df[target_name])
        X = np.array(df.drop(target_name, axis=1))
        train_data = X[:n_train_samples]
        Y_train = Y[:n_train_samples]
        test_data = X[n_train_samples:n_train_samples + n_test_samples]
        Y_true = Y[n_train_samples:n_train_samples + n_test_samples]
        Y_predict = nearest_neighbors(train_data, test_data, Y_train, n_neighbors=5)
        if fuzzy:
            accuracy = np.mean(abs(np.array(Y_predict) - np.array(Y_true)) < 2) * 100
        else:
            accuracy = np.mean(np.array(Y_predict) == np.array(Y_true)) * 100
        accuracy_list.append(accuracy)
    return np.mean(accuracy_list)
if __name__ == '__main__':
    iris_data = datasets.load_iris()
    iris_df = pd.DataFrame(iris_data.data)
    iris_df['target'] = iris_data.target
    iris_accuracy = evaluate_accuracy(iris_df, 'target', 120, 30, 20)
    print("Average accuracy for iris dataset is:", iris_accuracy)
    wine_data = pd.read_csv("redwinequality.csv")
    wine_accuracy_strict = evaluate_accuracy(wine_data, 'quality', 1500, 100, 20)
    wine_accuracy_fuzzy = evaluate_accuracy(wine_data, 'quality', 1500, 100, 20, fuzzy=True)
    print("Average strict accuracy for red wine dataset is:", wine_accuracy_strict)
    print("Average fuzzy accuracy for red wine dataset is:", wine_accuracy_fuzzy)