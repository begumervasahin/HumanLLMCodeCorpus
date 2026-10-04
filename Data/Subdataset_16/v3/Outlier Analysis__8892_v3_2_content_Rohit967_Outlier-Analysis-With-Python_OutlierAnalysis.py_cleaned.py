import numpy as np
import pandas as pd
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.ensemble import IsolationForest
from sklearn.neighbors import LocalOutlierFactor
import matplotlib.pyplot as plt
def fonk1(file_path):
    b1 = pd.read_csv(file_path, skiprows=1, header=None, sep=':')
    b2 = dict(b1[0])
    b2[41] = 'label'
    return list(b2.values())
def fonk2(file_path, b14):
    b3 = pd.read_csv(file_path, low_memory=False, header=None, names=b14)
    b3 = b3[(b3['service'] == "http") & (b3["logged_in"] == 1)]
    return b3
def fonk3(b3):
    b3.label.value_counts().plot(b4 = 'bar')
    plt.title('Label Distribution')
    plt.show()
def fonk4(b3, b15):
    b3 = b3[b15]
    b3['attack'] = np.where(b3['label'] == "normal.", 1, -1)
    b5 = b3['attack']
    b3.drop(["label", "attack"], b6 = 1, inplace=True)
    return b3, b5
def fonk5(b5):
    b7 = b5[b5 == -1]
    print("b7.shape:", b7.shape)
    print("outlier fraction:", b7.shape[0] / b5.shape[0])
def fonk6(model, train_data, train_target, test_data, b16):
    b8 = model.predict(train_data)
    b9 = model.predict(test_data)
    print("===================")
    print("For Training Data: ")
    print("===================")
    print("accuracy:", metrics.accuracy_score(train_target, b8))
    print("precision:", metrics.precision_score(train_target, b8))
    print("recall:", metrics.recall_score(train_target, b8))
    print("f1:", metrics.f1_score(train_target, b8))
    print("===============")
    print("For Test Data: ")
    print("===============")
    print("accuracy:", metrics.accuracy_score(b16, b9))
    print("precision:", metrics.precision_score(b16, b9))
    print("recall:", metrics.recall_score(b16, b9))
    print("f1:", metrics.f1_score(b16, b9))
def fonk7(b20, train_data, train_target, test_data, b16):
    b10 = b20.fit_predict(train_data)
    b11 = b20.fit_predict(test_data)
    print("===================")
    print("For Training Data: ")
    print("===================")
    print("accuracy:", metrics.accuracy_score(train_target, b10))
    print("precision:", metrics.precision_score(train_target, b10))
    print("recall:", metrics.recall_score(train_target, b10))
    print("f1:", metrics.f1_score(train_target, b10))
    print("===============")
    print("For Test Data: ")
    print("===============")
    print("accuracy:", metrics.accuracy_score(b16, b11))
    print("precision:", metrics.precision_score(b16, b11))
    print("recall:", metrics.recall_score(b16, b11))
    print("f1:", metrics.f1_score(b16, b11))
def fonk8():
    b12 = 'kddcup.names'
    b13 = 'kddcup.data_10_percent'
    b14 = fonk1(b12)
    b3 = fonk2(b13, b14)
    fonk3(b3)
    b15 = ["duration", "src_bytes", "dst_bytes", "label"]
    b3, b5 = fonk4(b3, b15)
    fonk5(b5)
    train_data, test_data, train_target, b16 = train_test_split(b3, b5, train_size=0.8)
    print("Training b3 shape:", train_data.shape)
    b17 = b5[b5 == -1].shape[0] / b5.shape[0]
    print("b17:", b17)
    print("One Class SVM")
    b18 = svm.OneClassSVM(b17=b17, kernel='rbf', gamma=0.00005)
    b18.fit(train_data)
    fonk6(b18, train_data, train_target, test_data, b16)
    print("Isolation Forest")
    b19 = IsolationForest(contamination=b17, random_state=42)
    b19.fit(train_data)
    fonk6(b19, train_data, train_target, test_data, b16)
    print("Local Outlier Factor")
    b20 = LocalOutlierFactor(n_neighbors=35, contamination=b17)
    fonk7(b20, train_data, train_target, test_data, b16)
if b21 = = "__main__":
    fonk8()