import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import svm, metrics
from sklearn.ensemble import IsolationForest
from sklearn.neighbors import LocalOutlierFactor
import matplotlib.pyplot as plt
data_names = pd.read_csv('kddcup.names', skiprows=1, header=None, sep=':')
data_names = dict(data_names[0])
data_names[41] = 'label'
dictlist = [value for key, value in data_names.items()]
data = pd.read_csv('kddcup.data_10_percent', low_memory=False, header=None, names=dictlist)
data = data[data['service'] == "http"]
data = data[data["logged_in"] == 1]
data.label.value_counts().plot(kind='bar')
relevant_features = ["duration", "src_bytes", "dst_bytes", "label"]
data = data[relevant_features]
data.loc[data['label'] == "normal.", "attack"] = 1
data.loc[data['label'] != "normal.", "attack"] = -1
target = data['attack']
data.drop(["label", "attack"], axis=1, inplace=True)
train_data, test_data, train_target, test_target = train_test_split(data, target, train_size=0.8)
outliers = target[target == -1]
nu = outliers.shape[0] / target.shape[0]
print("One Class SVM")
model = svm.OneClassSVM(nu=nu, kernel='rbf', gamma=0.00005)
model.fit(train_data)
preds = model.predict(train_data)
print("===================")
print("For Training Data: ")
print("===================")
print("accuracy: ", metrics.accuracy_score(train_target, preds))
print("precision: ", metrics.precision_score(train_target, preds))
print("recall: ", metrics.recall_score(train_target, preds))
print("f1: ", metrics.f1_score(train_target, preds))
preds = model.predict(test_data)
print("===============")
print("For Test Data: ")
print("===============")
print("accuracy: ", metrics.accuracy_score(test_target, preds))
print("precision: ", metrics.precision_score(test_target, preds))
print("recall: ", metrics.recall_score(test_target, preds))
print("f1: ", metrics.f1_score(test_target, preds))
print("Isolation Forest")
model1 = IsolationForest(contamination=nu, random_state=42)
model1.fit(train_data)
preds1 = model1.predict(train_data)
print("===================")
print("For Training Data: ")
print("===================")
print("accuracy: ", metrics.accuracy_score(train_target, preds1))
print("precision: ", metrics.precision_score(train_target, preds1))
print("recall: ", metrics.recall_score(train_target, preds1))
print("f1: ", metrics.f1_score(train_target, preds1))
preds1 = model1.predict(test_data)
print("===============")
print("For Test Data: ")
print("===============")
print("accuracy: ", metrics.accuracy_score(test_target, preds1))
print("precision: ", metrics.precision_score(test_target, preds1))
print("recall: ", metrics.recall_score(test_target, preds1))
print("f1: ", metrics.f1_score(test_target, preds1))
print("Local Outlier Factor")
lof = LocalOutlierFactor(n_neighbors=35, contamination=nu)
lof.fit(train_data)
preds2 = lof.fit_predict(train_data)
print("===================")
print("For Training Data: ")
print("===================")
print("accuracy: ", metrics.accuracy_score(train_target, preds2))
print("precision: ", metrics.precision_score(train_target, preds2))
print("recall: ", metrics.recall_score(train_target, preds2))
print("f1: ", metrics.f1_score(train_target, preds2))
preds2 = lof.fit_predict(test_data)
print("===============")
print("For Test Data: ")
print("===============")
print("accuracy: ", metrics.accuracy_score(test_target, preds2))
print("precision: ", metrics.precision_score(test_target, preds2))
print("recall: ", metrics.recall_score(test_target, preds2))
print("f1: ", metrics.f1_score(test_target, preds2))
plt.figure()
colors = np.array(['b' if label == 1 else 'r' for label in data['attack']])
plt.scatter(data['dst_bytes'], data['src_bytes'], s=10, color=colors)
plt.show()