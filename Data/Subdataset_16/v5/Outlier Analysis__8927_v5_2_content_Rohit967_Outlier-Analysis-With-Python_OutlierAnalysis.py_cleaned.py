import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import metrics, svm
from sklearn.ensemble import IsolationForest
from sklearn.neighbors import LocalOutlierFactor
def fonk1(file_path):
    b1 = pd.read_csv(file_path, skiprows=1, header=None, sep=':')
    b1 = dict(b1[0])
    b1[41] = 'label'
    return list(b1.values())
def fonk2(file_path, b11):
    b2 = pd.read_csv(file_path, low_memory=False, header=None, names=b11)
    b2 = b2[(b2['service'] == "http") & (b2["logged_in"] == 1)]
    return b2
def fonk3(b2):
    b2['label'].value_counts().plot(b3 = 'bar')
def fonk4(b2):
    b2['attack'] = np.where(b2['label'] == "normal.", 1, -1)
    b4 = b2['attack']
    return b4
def fonk5(b4):
    b5 = b4[b4 == -1]
    print("b5.shape:", b5.shape)
    print("outlier fraction:", b5.shape[0] / b4.shape[0])
def fonk6(b2, columns):
    b2.drop(columns, b6 = 1, inplace=True)
def fonk7(b2, b4, b7 = 0.8):
    return train_test_split(b2, b4, b7 = b7)
def fonk8(train_data, test_data, train_target, b13, b14):
    print("One-Class SVM")
    b8 = svm.OneClassSVM(b14=b14, kernel='rbf', gamma=0.00005)
    b8.fit(train_data)
    fonk11(b8, train_data, train_target, "Training Data")
    fonk11(b8, test_data, b13, "Test Data")
def fonk9(train_data, test_data, train_target, b13, b14):
    print("Isolation Forest")
    b8 = IsolationForest(contamination=b14, random_state=42)
    b8.fit(train_data)
    fonk11(b8, train_data, train_target, "Training Data", b9 = 'predict')
    fonk11(b8, test_data, b13, "Test Data", b9 = 'predict')
def fonk10(train_data, test_data, train_target, b13, b14):
    print("Local Outlier Factor")
    b8 = LocalOutlierFactor(n_neighbors=35, contamination=b14)
    fonk11(b8, train_data, train_target, "Training Data", b9 = 'fit_predict')
    fonk11(b8, test_data, b13, "Test Data", b9 = 'fit_predict')
def fonk11(b8, b2, b4, data_label, b9 = 'predict'):
    if b9 = = 'predict':
        b10 = b8.predict(b2)
    else:
        b10 = b8.fit_predict(b2)
    print("===================")
    print(f"For {data_label}:")
    print("===================")
    print("accuracy:", metrics.accuracy_score(b4, b10))
    print("precision:", metrics.precision_score(b4, b10))
    print("recall:", metrics.recall_score(b4, b10))
    print("f1:", metrics.f1_score(b4, b10))
def fonk12():
    b11 = fonk1('kddcup.names')
    b2 = fonk2('kddcup.data_10_percent', b11)
    fonk3(b2)
    b12 = ["duration", "src_bytes", "dst_bytes", "label"]
    b2 = b2[b12]
    b4 = fonk4(b2)
    fonk5(b4)
    fonk6(b2, ["label", "attack"])
    train_data, test_data, train_target, b13 = fonk7(b2, b4)
    print("Training b2 shape:", train_data.shape)
    b14 = b4[b4 == -1].shape[0] / b4.shape[0]
    print("b14:", b14)
    fonk8(train_data, test_data, train_target, b13, b14)
    fonk9(train_data, test_data, train_target, b13, b14)
    fonk10(train_data, test_data, train_target, b13, b14)
if b15 = = "__main__":
    fonk12()