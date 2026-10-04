import numpy as np
import pandas as pd
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.ensemble import IsolationForest
from sklearn.neighbors import LocalOutlierFactor
import matplotlib.pyplot as plt
def load_feature_names(file_path):
    data_names = pd.read_csv(file_path, skiprows=1, header=None, sep=':')
    data_names_dict = dict(data_names[0])
    data_names_dict[41] = 'label'
    return list(data_names_dict.values())
def load_and_filter_data(file_path, column_names):
    data = pd.read_csv(file_path, low_memory=False, header=None, names=column_names)
    data = data[(data['service'] == "http") & (data["logged_in"] == 1)]
    return data
def plot_label_distribution(data):
    data.label.value_counts().plot(kind='bar')
    plt.title('Label Distribution')
    plt.show()
def prepare_data(data, relevant_features):
    data = data[relevant_features]
    data['attack'] = np.where(data['label'] == "normal.", 1, -1)
    target = data['attack']
    data.drop(["label", "attack"], axis=1, inplace=True)
    return data, target
def print_outliers_info(target):
    outliers = target[target == -1]
    print("outliers.shape:", outliers.shape)
    print("outlier fraction:", outliers.shape[0] / target.shape[0])
def evaluate_model(model, train_data, train_target, test_data, test_target):
    preds_train = model.predict(train_data)
    preds_test = model.predict(test_data)
    print("===================")
    print("For Training Data: ")
    print("===================")
    print("accuracy:", metrics.accuracy_score(train_target, preds_train))
    print("precision:", metrics.precision_score(train_target, preds_train))
    print("recall:", metrics.recall_score(train_target, preds_train))
    print("f1:", metrics.f1_score(train_target, preds_train))
    print("===============")
    print("For Test Data: ")
    print("===============")
    print("accuracy:", metrics.accuracy_score(test_target, preds_test))
    print("precision:", metrics.precision_score(test_target, preds_test))
    print("recall:", metrics.recall_score(test_target, preds_test))
    print("f1:", metrics.f1_score(test_target, preds_test))
def evaluate_lof(lof, train_data, train_target, test_data, test_target):
    preds_train_lof = lof.fit_predict(train_data)
    preds_test_lof = lof.fit_predict(test_data)
    print("===================")
    print("For Training Data: ")
    print("===================")
    print("accuracy:", metrics.accuracy_score(train_target, preds_train_lof))
    print("precision:", metrics.precision_score(train_target, preds_train_lof))
    print("recall:", metrics.recall_score(train_target, preds_train_lof))
    print("f1:", metrics.f1_score(train_target, preds_train_lof))
    print("===============")
    print("For Test Data: ")
    print("===============")
    print("accuracy:", metrics.accuracy_score(test_target, preds_test_lof))
    print("precision:", metrics.precision_score(test_target, preds_test_lof))
    print("recall:", metrics.recall_score(test_target, preds_test_lof))
    print("f1:", metrics.f1_score(test_target, preds_test_lof))
def main():
    names_file_path = 'kddcup.names'
    data_file_path = 'kddcup.data_10_percent'
    column_names = load_feature_names(names_file_path)
    data = load_and_filter_data(data_file_path, column_names)
    plot_label_distribution(data)
    relevant_features = ["duration", "src_bytes", "dst_bytes", "label"]
    data, target = prepare_data(data, relevant_features)
    print_outliers_info(target)
    train_data, test_data, train_target, test_target = train_test_split(data, target, train_size=0.8)
    print("Training data shape:", train_data.shape)
    nu = target[target == -1].shape[0] / target.shape[0]
    print("nu:", nu)
    print("One Class SVM")
    model_svm = svm.OneClassSVM(nu=nu, kernel='rbf', gamma=0.00005)
    model_svm.fit(train_data)
    evaluate_model(model_svm, train_data, train_target, test_data, test_target)
    print("Isolation Forest")
    model_if = IsolationForest(contamination=nu, random_state=42)
    model_if.fit(train_data)
    evaluate_model(model_if, train_data, train_target, test_data, test_target)
    print("Local Outlier Factor")
    lof = LocalOutlierFactor(n_neighbors=35, contamination=nu)
    evaluate_lof(lof, train_data, train_target, test_data, test_target)
if __name__ == "__main__":
    main()