import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import svm, metrics
from sklearn.ensemble import IsolationForest
from sklearn.neighbors import LocalOutlierFactor
import matplotlib.pyplot as plt
def fonk1(file_names):
    b1 = pd.read_csv(file_names, skiprows=1, header=None, sep=':')
    b1 = dict(b1[0])
    b1[41] = 'label'
    b2 = pd.read_csv('kddcup.data_10_percent', low_memory=False, header=None, names=b1.values())
    return b2
def fonk2(b2):
    b3 = b2[(b2['service'] == "http") & (b2["logged_in"] == 1)]
    b3['label'].value_counts().plot(b4 = 'bar')
    b5 = ["duration", "src_bytes", "dst_bytes", "label"]
    b3 = b3[b5]
    b3['attack'] = np.where(b3['label'] == "normal.", 1, -1)
    return b3
def fonk3(data_type, b8, preds):
    print("===================")
    print(f"For {data_type} Data: ")
    print("===================")
    print("accuracy: ", metrics.accuracy_score(b8, preds))
    print("precision: ", metrics.precision_score(b8, preds))
    print("recall: ", metrics.recall_score(b8, preds))
    print("f1: ", metrics.f1_score(b8, preds))
def fonk4(model, train_data, test_data, train_target, b10):
    model.fit(train_data)
    b6 = model.predict(train_data)
    b7 = model.predict(test_data)
    fonk3("Training", train_target, b6)
    fonk3("Test", b10, b7)
    return b6, b7
def fonk5():
    b2 = fonk1('kddcup.names')
    b3 = fonk2(b2)
    b8 = b3['attack']
    b3.drop(["label", "attack"], b9 = 1, inplace=True)
    train_data, test_data, train_target, b10 = train_test_split(b3, b8, train_size=0.8)
    b11 = b8[b8 == -1].shape[0] / b8.shape[0]
    print("One Class SVM")
    b12 = svm.OneClassSVM(b11=b11, kernel='rbf', gamma=0.00005)
    b6, b7 = fonk4(b12, train_data, test_data, train_target, b10)
    print("\nIsolation Forest")
    b13 = IsolationForest(contamination=b11, random_state=42)
    train_preds1, b14 = fonk4(b13, train_data, test_data, train_target, b10)
    print("\nLocal Outlier Factor")
    b15 = LocalOutlierFactor(n_neighbors=35, contamination=b11)
    train_preds2, b16 = fonk4(b15, train_data, test_data, train_target, b10)
    plt.figure()
    b17 = np.array(['b' if label == 1 else 'r' for label in b3['attack']])
    plt.scatter(b3['dst_bytes'], b3['src_bytes'], b18 = 10, color=b17)
    plt.show()
if b19 = = "__main__":
    fonk5()