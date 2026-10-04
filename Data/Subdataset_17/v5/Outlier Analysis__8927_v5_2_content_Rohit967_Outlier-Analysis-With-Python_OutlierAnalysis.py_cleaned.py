import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import metrics, svm
from sklearn.ensemble import IsolationForest
from sklearn.neighbors import LocalOutlierFactor
def load_feature_names(file_path):
    data_names = pd.read_csv(file_path, skiprows=1, header=None, sep=':')
    data_names = dict(data_names[0])
    data_names[41] = 'label'
    return list(data_names.values())
def load_and_filter_data(file_path, feature_names):
    data = pd.read_csv(file_path, low_memory=False, header=None, names=feature_names)
    data = data[(data['service'] == "http") & (data["logged_in"] == 1)]
    return data
def plot_label_distribution(data):
    data['label'].value_counts().plot(kind='bar')
def create_target_labels(data):
    data['attack'] = np.where(data['label'] == "normal.", 1, -1)
    target = data['attack']
    return target
def print_outliers_info(target):
    outliers = target[target == -1]
    print("outliers.shape:", outliers.shape)
    print("outlier fraction:", outliers.shape[0] / target.shape[0])
def drop_unused_columns(data, columns):
    data.drop(columns, axis=1, inplace=True)
def split_data(data, target, train_size=0.8):
    return train_test_split(data, target, train_size=train_size)
def train_and_evaluate_one_class_svm(train_data, test_data, train_target, test_target, nu):
    print("One-Class SVM")
    model = svm.OneClassSVM(nu=nu, kernel='rbf', gamma=0.00005)
    model.fit(train_data)
    evaluate_model(model, train_data, train_target, "Training Data")
    evaluate_model(model, test_data, test_target, "Test Data")
def train_and_evaluate_isolation_forest(train_data, test_data, train_target, test_target, nu):
    print("Isolation Forest")
    model = IsolationForest(contamination=nu, random_state=42)
    model.fit(train_data)
    evaluate_model(model, train_data, train_target, "Training Data", predict_method='predict')
    evaluate_model(model, test_data, test_target, "Test Data", predict_method='predict')
def train_and_evaluate_local_outlier_factor(train_data, test_data, train_target, test_target, nu):
    print("Local Outlier Factor")
    model = LocalOutlierFactor(n_neighbors=35, contamination=nu)
    evaluate_model(model, train_data, train_target, "Training Data", predict_method='fit_predict')
    evaluate_model(model, test_data, test_target, "Test Data", predict_method='fit_predict')
def evaluate_model(model, data, target, data_label, predict_method='predict'):
    if predict_method == 'predict':
        preds = model.predict(data)
    else:
        preds = model.fit_predict(data)
    print("===================")
    print(f"For {data_label}:")
    print("===================")
    print("accuracy:", metrics.accuracy_score(target, preds))
    print("precision:", metrics.precision_score(target, preds))
    print("recall:", metrics.recall_score(target, preds))
    print("f1:", metrics.f1_score(target, preds))
def main():
    feature_names = load_feature_names('kddcup.names')
    data = load_and_filter_data('kddcup.data_10_percent', feature_names)
    plot_label_distribution(data)
    relevant_features = ["duration", "src_bytes", "dst_bytes", "label"]
    data = data[relevant_features]
    target = create_target_labels(data)
    print_outliers_info(target)
    drop_unused_columns(data, ["label", "attack"])
    train_data, test_data, train_target, test_target = split_data(data, target)
    print("Training data shape:", train_data.shape)
    nu = target[target == -1].shape[0] / target.shape[0]
    print("nu:", nu)
    train_and_evaluate_one_class_svm(train_data, test_data, train_target, test_target, nu)
    train_and_evaluate_isolation_forest(train_data, test_data, train_target, test_target, nu)
    train_and_evaluate_local_outlier_factor(train_data, test_data, train_target, test_target, nu)
if __name__ == "__main__":
    main()