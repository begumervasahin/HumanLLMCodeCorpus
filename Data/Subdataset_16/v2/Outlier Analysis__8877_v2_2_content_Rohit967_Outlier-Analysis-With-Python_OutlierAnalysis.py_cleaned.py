import numpy as np
import pandas as pd
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.ensemble import IsolationForest
from sklearn.neighbors import LocalOutlierFactor
import matplotlib.pyplot as plt
b1 = pd.read_csv('kddcup.names', skiprows=1, header=None, sep=':')
b2 = dict(b1[0])
b2[41] = 'label'
b3 = list(b2.values())
b4 = pd.read_csv('kddcup.data_10_percent', low_memory=False, header=None, names=b3)
b4 = b4[(b4['service'] == "http") & (b4["logged_in"] == 1)]
b4.label.value_counts().plot(b5 = 'bar')
plt.title('Label Distribution')
plt.show()
b6 = ["duration", "src_bytes", "dst_bytes", "label"]
b4 = b4[b6]
b4['attack'] = np.where(b4['label'] == "normal.", 1, -1)
b7 = b4['attack']
b8 = b7[b7 == -1]
print("b8.shape:", b8.shape)
print("outlier fraction:", b8.shape[0] / b7.shape[0])
b4.drop(["label", "attack"], b9 = 1, inplace=True)
train_data, test_data, train_target, b10 = train_test_split(b4, b7, train_size=0.8)
print("Training b4 shape:", train_data.shape)
b11 = b8.shape[0] / b7.shape[0]
print("b11:", b11)
print("One Class SVM")
b12 = svm.OneClassSVM(b11=b11, kernel='rbf', gamma=0.00005)
b12.fit(train_data)
def fonk1(model, train_data, train_target, test_data, b10):
    b13 = model.predict(train_data)
    b14 = model.predict(test_data)
    print("===================")
    print("For Training Data: ")
    print("===================")
    print("accuracy:", metrics.accuracy_score(train_target, b13))
    print("precision:", metrics.precision_score(train_target, b13))
    print("recall:", metrics.recall_score(train_target, b13))
    print("f1:", metrics.f1_score(train_target, b13))
    print("===============")
    print("For Test Data: ")
    print("===============")
    print("accuracy:", metrics.accuracy_score(b10, b14))
    print("precision:", metrics.precision_score(b10, b14))
    print("recall:", metrics.recall_score(b10, b14))
    print("f1:", metrics.f1_score(b10, b14))
fonk1(b12, train_data, train_target, test_data, b10)
print("Isolation Forest")
b15 = IsolationForest(contamination=b11, random_state=42)
b15.fit(train_data)
fonk1(b15, train_data, train_target, test_data, b10)
print("Local Outlier Factor")
b16 = LocalOutlierFactor(n_neighbors=35, contamination=b11)
def fonk2(b16, train_data, train_target, test_data, b10):
    b17 = b16.fit_predict(train_data)
    b18 = b16.fit_predict(test_data)
    print("===================")
    print("For Training Data: ")
    print("===================")
    print("accuracy:", metrics.accuracy_score(train_target, b17))
    print("precision:", metrics.precision_score(train_target, b17))
    print("recall:", metrics.recall_score(train_target, b17))
    print("f1:", metrics.f1_score(train_target, b17))
    print("===============")
    print("For Test Data: ")
    print("===============")
    print("accuracy:", metrics.accuracy_score(b10, b18))
    print("precision:", metrics.precision_score(b10, b18))
    print("recall:", metrics.recall_score(b10, b18))
    print("f1:", metrics.f1_score(b10, b18))
fonk2(b16, train_data, train_target, test_data, b10)