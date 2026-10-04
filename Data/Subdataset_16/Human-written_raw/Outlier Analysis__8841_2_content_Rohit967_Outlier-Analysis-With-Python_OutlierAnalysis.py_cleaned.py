import numpy as np
import pandas as pd
from sklearn import utils
b1 = pd.read_csv('kddcup.names', skiprows = 1,b5=None,sep=':')
b1 = dict(b1[0])
b1[41] = 'label'
b2 = []
for key, value in b1.items():
    b3 = value
    b2.append(b3)
b4 = pd.read_csv('kddcup.data_10_percent', low_memory=False,
                   b5 = None,names = b2)
b4 = b4[b4['service'] == "http"]
b4 = b4[b4["logged_in"] == 1]
b4.label.value_counts().plot(b6 = 'bar')
b7 = [
    "duration",
    "src_bytes",
    "dst_bytes",
    "label"
]
b4 = b4[b7]
b4.loc[b4['label'] == "normal.", "attack"] = 1
b4.loc[b4['label'] != "normal.", "attack"] = -1
b8 = b4['attack']
b9 = b8[b8 == -1]
print("b9.shape", b9.shape)
print("outlier fraction", b9.shape[0]/b8.shape[0])
b4.drop(["label", "attack"], b10 = 1, inplace=True)
from sklearn.model_selection import train_test_split
train_data, test_data, train_target, b11 = train_test_split(b4, b8, train_size = 0.8)
train_data.shape
from sklearn import svm
b12 = b9.shape[0] / b8.shape[0]
print("b12", b12)
print("
print("One Class SVM")
print("
b13 = svm.OneClassSVM(b12=b12, kernel='rbf', gamma=0.00005)
b13.fit(train_data)
from sklearn import metrics
b14 = b13.predict(train_data)
b15 = train_target
print("===================")
print("For Training Data: ")
print("===================")
print("accuracy: ", metrics.accuracy_score(b15, b14))
print("precision: ", metrics.precision_score(b15, b14))
print("recall: ", metrics.recall_score(b15, b14))
print("f1: ", metrics.f1_score(b15, b14))
b14 = b13.predict(test_data)
b15 = b11
print("===============")
print("For Test Data: ")
print("===============")
print("accuracy: ", metrics.accuracy_score(b15, b14))
print("precision: ", metrics.precision_score(b15, b14))
print("recall: ", metrics.recall_score(b15, b14))
print("f1: ", metrics.f1_score(b15, b14))
'''
import matplotlib.pyplot as plt
plt.figure()
b16 = np.array(['
plt.scatter(b4['dst_bytes'], b4['src_bytes'], b17 = 10, color=b16)
plt.show()
'''
print("
print("Isolation Forest")
print("
from sklearn.ensemble import IsolationForest
b18 = IsolationForest(contamination=b12,random_state=42)
b18.fit(train_data)
b19 = b18.predict(train_data)
b15 = train_target
print("===================")
print("For Training Data: ")
print("===================")
print("accuracy: ", metrics.accuracy_score(b15, b19))
print("precision: ", metrics.precision_score(b15, b19))
print("recall: ", metrics.recall_score(b15, b19))
print("f1: ", metrics.f1_score(b15, b19))
b19 = b18.predict(test_data)
b15 = b11
print("===============")
print("For Test Data: ")
print("===============")
print("accuracy: ", metrics.accuracy_score(b15, b19))
print("precision: ", metrics.precision_score(b15, b19))
print("recall: ", metrics.recall_score(b15, b19))
print("f1: ", metrics.f1_score(b15, b19))
print("
print("Local Outlier Factor")
print("
from sklearn.neighbors import LocalOutlierFactor
b20 = LocalOutlierFactor(n_neighbors=35, contamination=b12)
b21 = b20.fit_predict(train_data)
b15 = train_target
print("===================")
print("For Training Data: ")
print("===================")
print("accuracy: ", metrics.accuracy_score(b15, b21))
print("precision: ", metrics.precision_score(b15, b21))
print("recall: ", metrics.recall_score(b15, b21))
print("f1: ", metrics.f1_score(b15, b21))
b21 = b20.fit_predict(test_data)
b15 = b11
print("===============")
print("For Test Data: ")
print("===============")
print("accuracy: ", metrics.accuracy_score(b15, b21))
print("precision: ", metrics.precision_score(b15, b21))
print("recall: ", metrics.recall_score(b15, b21))
print("f1: ", metrics.f1_score(b15, b21))
'''
b1 = ['duration','protocol_type','service','flag','src_bytes','dst_bytes','land','wrong_fragment',
 'urgent','hot','num_failed_logins','logged_in','num_compromised','root_shell',
'su_attempted', 'num_root','num_file_creations','num_shells','num_access_files',
'num_outbound_cmds','is_host_login','is_guest_login','count','srv_count','serror_rate',
'srv_serror_rate','rerror_rate','srv_rerror_rate','same_srv_rate','diff_srv_rate',
'srv_diff_host_rate','dst_host_count','dst_host_srv_count','dst_host_same_srv_rate',
'dst_host_diff_srv_rate','dst_host_same_src_port_rate','dst_host_srv_diff_host_rate',
'dst_host_serror_rate','dst_host_srv_serror_rate','dst_host_rerror_rate',
'dst_host_srv_rerror_rate','label']'''