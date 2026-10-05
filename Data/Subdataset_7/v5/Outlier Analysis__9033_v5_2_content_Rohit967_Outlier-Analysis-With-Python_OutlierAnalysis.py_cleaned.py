import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import svm, metrics
from sklearn.ensemble import IsolationForest
from sklearn.neighbors import LocalOutlierFactor
import matplotlib.pyplot as plt
def fonk1():
    b1 = pd.read_csv('kddcup.names', skiprows=1, header=None, sep=':')
    b1 = dict(b1[0])
    b1[41] = 'label'
    b2 = list(b1.values())
    b3 = pd.read_csv('kddcup.data_10_percent', low_memory=False, header=None, names=b2)
    return b3
def fonk2(b3):
    b3 = b3[(b3['service'] == "http") & (b3["logged_in"] == 1)]
    b3 = b3[["duration", "src_bytes", "dst_bytes", "label"]]
    b3['attack'] = np.where(b3['label'] == "normal.", 1, -1)
    b3.drop(["label", "attack"], b4 = 1, inplace=True)
    return b3
def fonk3(model, train_data, test_data, train_target, b10):
    model.fit(train_data)
    b5 = model.predict(train_data)
    b6 = model.predict(test_data)
    print("Training Performance:")
    fonk4(train_target, b5)
    print("\nTesting Performance:")
    fonk4(b10, b6)
def fonk4(b9, predictions):
    print("Accuracy:", metrics.accuracy_score(b9, predictions))
    print("Precision:", metrics.precision_score(b9, predictions))
    print("Recall:", metrics.recall_score(b9, predictions))
    print("F1 Score:", metrics.f1_score(b9, predictions))
def fonk5(b3):
    b3.label.value_counts().plot(b7 = 'bar')
    plt.show()
def fonk6(b3):
    plt.scatter(b3['dst_bytes'], b3['src_bytes'], b8 = 10)
    plt.show()
def fonk7():
    b3 = fonk1()
    b3 = fonk2(b3)
    fonk5(b3)
    b9 = b3['attack']
    b3.drop("attack", b4 = 1, inplace=True)
    train_data, test_data, train_target, b10 = train_test_split(b3, b9, train_size=0.8)
    b11 = (train_target == -1).sum() / train_target.shape[0]
    print("\nOne Class SVM")
    b12 = svm.OneClassSVM(b11=b11, kernel='rbf', gamma=0.00005)
    fonk3(b12, train_data, test_data, train_target, b10)
    print("\nIsolation Forest")
    b13 = IsolationForest(contamination=b11, random_state=42)
    fonk3(b13, train_data, test_data, train_target, b10)
    print("\nLocal Outlier Factor")
    b14 = LocalOutlierFactor(n_neighbors=35, contamination=b11)
    fonk3(b14, train_data, test_data, train_target, b10)
    fonk6(b3)
if b15 = = "__main__":
    fonk7()