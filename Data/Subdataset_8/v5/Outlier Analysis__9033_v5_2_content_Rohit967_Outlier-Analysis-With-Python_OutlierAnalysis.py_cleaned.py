import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import svm, metrics
from sklearn.ensemble import IsolationForest
from sklearn.neighbors import LocalOutlierFactor
import matplotlib.pyplot as plt
def load_data():
    data_names = pd.read_csv('kddcup.names', skiprows=1, header=None, sep=':')
    data_names = dict(data_names[0])
    data_names[41] = 'label'
    column_names = list(data_names.values())
    data = pd.read_csv('kddcup.data_10_percent', low_memory=False, header=None, names=column_names)
    return data
def preprocess_data(data):
    data = data[(data['service'] == "http") & (data["logged_in"] == 1)]
    data = data[["duration", "src_bytes", "dst_bytes", "label"]]
    data['attack'] = np.where(data['label'] == "normal.", 1, -1)
    data.drop(["label", "attack"], axis=1, inplace=True)
    return data
def evaluate_model(model, train_data, test_data, train_target, test_target):
    model.fit(train_data)
    train_preds = model.predict(train_data)
    test_preds = model.predict(test_data)
    print("Training Performance:")
    print_metrics(train_target, train_preds)
    print("\nTesting Performance:")
    print_metrics(test_target, test_preds)
def print_metrics(target, predictions):
    print("Accuracy:", metrics.accuracy_score(target, predictions))
    print("Precision:", metrics.precision_score(target, predictions))
    print("Recall:", metrics.recall_score(target, predictions))
    print("F1 Score:", metrics.f1_score(target, predictions))
def visualize_label_distribution(data):
    data.label.value_counts().plot(kind='bar')
    plt.show()
def scatter_plot(data):
    plt.scatter(data['dst_bytes'], data['src_bytes'], s=10)
    plt.show()
def main():
    data = load_data()
    data = preprocess_data(data)
    visualize_label_distribution(data)
    target = data['attack']
    data.drop("attack", axis=1, inplace=True)
    train_data, test_data, train_target, test_target = train_test_split(data, target, train_size=0.8)
    nu = (train_target == -1).sum() / train_target.shape[0]
    print("\nOne Class SVM")
    svm_model = svm.OneClassSVM(nu=nu, kernel='rbf', gamma=0.00005)
    evaluate_model(svm_model, train_data, test_data, train_target, test_target)
    print("\nIsolation Forest")
    forest_model = IsolationForest(contamination=nu, random_state=42)
    evaluate_model(forest_model, train_data, test_data, train_target, test_target)
    print("\nLocal Outlier Factor")
    lof_model = LocalOutlierFactor(n_neighbors=35, contamination=nu)
    evaluate_model(lof_model, train_data, test_data, train_target, test_target)
    scatter_plot(data)
if __name__ == "__main__":
    main()