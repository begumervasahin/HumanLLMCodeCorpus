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
b2 = [value for key, value in b1.items()]
b3 = pd.read_csv('kddcup.data_10_percent', low_memory=False, header=None, names=b2)
b3 = b3[b3['service'] == "http"]
b3 = b3[b3["logged_in"] == 1]
b3.label.value_counts().plot(b4 = 'bar')
b5 = ["duration", "src_bytes", "dst_bytes", "label"]
b3 = b3[b5]
b3.loc[b3['label'] == "normal.", "attack"] = 1
b3.loc[b3['label'] != "normal.", "attack"] = -1
b6 = b3['attack']
b3.drop(["label", "attack"], b7 = 1, inplace=True)
train_data, test_data, train_target, b8 = train_test_split(b3, b6, train_size=0.8)
b9 = b6[b6 == -1]
b10 = b9.shape[0] / b6.shape[0]
print("One Class SVM")
b11 = svm.OneClassSVM(b10=b10, kernel='rbf', gamma=0.00005)
b11.fit(train_data)
b12 = b11.predict(train_data)
print("===================")
print("For Training Data: ")
print("===================")
print("accuracy: ", metrics.accuracy_score(train_target, b12))
print("precision: ", metrics.precision_score(train_target, b12))
print("recall: ", metrics.recall_score(train_target, b12))
print("f1: ", metrics.f1_score(train_target, b12))
b12 = b11.predict(test_data)
print("===============")
print("For Test Data: ")
print("===============")
print("accuracy: ", metrics.accuracy_score(b8, b12))
print("precision: ", metrics.precision_score(b8, b12))
print("recall: ", metrics.recall_score(b8, b12))
print("f1: ", metrics.f1_score(b8, b12))
print("Isolation Forest")
b13 = IsolationForest(contamination=b10, random_state=42)
b13.fit(train_data)
b14 = b13.predict(train_data)
print("===================")
print("For Training Data: ")
print("===================")
print("accuracy: ", metrics.accuracy_score(train_target, b14))
print("precision: ", metrics.precision_score(train_target, b14))
print("recall: ", metrics.recall_score(train_target, b14))
print("f1: ", metrics.f1_score(train_target, b14))
b14 = b13.predict(test_data)
print("===============")
print("For Test Data: ")
print("===============")
print("accuracy: ", metrics.accuracy_score(b8, b14))
print("precision: ", metrics.precision_score(b8, b14))
print("recall: ", metrics.recall_score(b8, b14))
print("f1: ", metrics.f1_score(b8, b14))
print("Local Outlier Factor")
b15 = LocalOutlierFactor(n_neighbors=35, contamination=b10)
b15.fit(train_data)
b16 = b15.fit_predict(train_data)
print("===================")
print("For Training Data: ")
print("===================")
print("accuracy: ", metrics.accuracy_score(train_target, b16))
print("precision: ", metrics.precision_score(train_target, b16))
print("recall: ", metrics.recall_score(train_target, b16))
print("f1: ", metrics.f1_score(train_target, b16))
b16 = b15.fit_predict(test_data)
print("===============")
print("For Test Data: ")
print("===============")
print("accuracy: ", metrics.accuracy_score(b8, b16))
print("precision: ", metrics.precision_score(b8, b16))
print("recall: ", metrics.recall_score(b8, b16))
print("f1: ", metrics.f1_score(b8, b16))
plt.figure()
b17 = np.array(['b' if label == 1 else 'r' for label in b3['attack']])
plt.scatter(b3['dst_bytes'], b3['src_bytes'], b18 = 10, color=b17)
plt.show()