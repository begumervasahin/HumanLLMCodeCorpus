
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import svm, metrics
from sklearn.ensemble import IsolationForest
from sklearn.neighbors import LocalOutlierFactor
import matplotlib.pyplot as plt
b1 = pd.read_csv('kddcup.names', skiprows=1, header=None, sep=':')
b1 = dict(b1[0])
b1[41] = 'label'
b2 = list(b1.values())
b3 = pd.read_csv('kddcup.data_10_percent', low_memory=False, header=None, names=b2)
b3 = b3[b3['service'] == "http"]
b3 = b3[b3["logged_in"] == 1]
b3.label.value_counts().plot(b4 = 'bar')
b5 = ["duration", "src_bytes", "dst_bytes", "label"]
b3 = b3[b5]
b3.loc[b3['label'] == "normal.", "attack"] = 1
b3.loc[b3['label'] != "normal.", "attack"] = -1
b6 = b3['attack']
b7 = b6[b6 == -1]
print("b7.shape", b7.shape)
print("outlier fraction", b7.shape[0] / b6.shape[0])
b3.drop(["label", "attack"], b8 = 1, inplace=True)
train_data, test_data, train_target, b9 = train_test_split(b3, b6, train_size=0.8)
b10 = b7.shape[0] / b6.shape[0]
print("b10", b10)
print("One Class SVM")
b11 = svm.OneClassSVM(b10=b10, kernel='rbf', gamma=0.00005)
b11.fit(train_data)
b12 = b11.predict(train_data)
b13 = train_target
print("===================")
print("For Training Data: ")
print("===================")
print("accuracy: ", metrics.accuracy_score(b13, b12))
print("precision: ", metrics.precision_score(b13, b12))
print("recall: ", metrics.recall_score(b13, b12))
print("f1: ", metrics.f1_score(b13, b12))
b12 = b11.predict(test_data)
b13 = b9
print("===============")
print("For Test Data: ")
print("===============")
print("accuracy: ", metrics.accuracy_score(b13, b12))
print("precision: ", metrics.precision_score(b13, b12))
print("recall: ", metrics.recall_score(b13, b12))
print("f1: ", metrics.f1_score(b13, b12))
print("Isolation Forest")
b14 = IsolationForest(contamination=b10, random_state=42)
b14.fit(train_data)
b15 = b14.predict(train_data)
b13 = train_target
print("===================")
print("For Training Data: ")
print("===================")
print("accuracy: ", metrics.accuracy_score(b13, b15))
print("precision: ", metrics.precision_score(b13, b15))
print("recall: ", metrics.recall_score(b13, b15))
print("f1: ", metrics.f1_score(b13, b15))
b15 = b14.predict(test_data)
b13 = b9
print("===============")
print("For Test Data: ")
print("===============")
print("accuracy: ", metrics.accuracy_score(b13, b15))
print("precision: ", metrics.precision_score(b13, b15))
print("recall: ", metrics.recall_score(b13, b15))
print("f1: ", metrics.f1_score(b13, b15))
print("Local Outlier Factor")
b16 = LocalOutlierFactor(n_neighbors=35, contamination=b10)
b17 = b16.fit_predict(train_data)
b13 = train_target
print("===================")
print("For Training Data: ")
print("===================")
print("accuracy: ", metrics.accuracy_score(b13, b17))
print("precision: ", metrics.precision_score(b13, b17))
print("recall: ", metrics.recall_score(b13, b17))
print("f1: ", metrics.f1_score(b13, b17))
b17 = b16.fit_predict(test_data)
b13 = b9
print("===============")
print("For Test Data: ")
print("===============")
print("accuracy: ", metrics.accuracy_score(b13, b17))
print("precision: ", metrics.precision_score(b13, b17))
print("recall: ", metrics.recall_score(b13, b17))
print("f1: ", metrics.f1_score(b13, b17))
plt.figure()
b18 = np.array([''])
plt.scatter(b3['dst_bytes'], b3['src_bytes'], b19 = 10, color=b18)
plt.show()