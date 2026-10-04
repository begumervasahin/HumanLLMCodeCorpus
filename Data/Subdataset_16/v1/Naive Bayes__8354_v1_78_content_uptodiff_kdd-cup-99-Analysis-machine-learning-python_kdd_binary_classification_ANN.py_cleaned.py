
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from keras.models import Sequential
from keras.layers import Dense
from math import log
b1 = pd.read_csv('kddcup.data_10_percent_corrected')
b2 = ['back.', 'buffer_overflow.', 'ftp_write.', 'guess_passwd.', 'imap.', 'ipsweep.', 'land.',
                'loadmodule.', 'multihop.', 'neptune.', 'nmap.', 'perl.', 'phf.', 'pod.', 'portsweep.',
                'rootkit.', 'satan.', 'smurf.', 'spy.', 'teardrop.', 'warezclient.', 'warezmaster.']
b1['normal.'] = b1['normal.'].replace(b2, 'attack')
b3 = b1.iloc[:, :-1].values
b4 = b1.iloc[:, 41].values
b5 = LabelEncoder()
b6 = LabelEncoder()
b7 = LabelEncoder()
b3[:, 1] = b5.fit_transform(b3[:, 1])
b3[:, 2] = b6.fit_transform(b3[:, 2])
b3[:, 3] = b7.fit_transform(b3[:, 3])
b8 = OneHotEncoder()
b3 = b8.fit_transform(b3).toarray()
b9 = LabelEncoder()
b4 = b9.fit_transform(b4)
b12, b13, y_train, b10 = train_test_split(b3, b4, test_size=0.3, random_state=0)
b11 = StandardScaler()
b12 = b11.fit_transform(b12)
b13 = b11.transform(b13)
b14 = Sequential()
b14.add(Dense(b15 = 60, kernel_initializer='uniform', activation='relu', input_dim=b12.shape[1]))
b14.add(Dense(b15 = 60, kernel_initializer='uniform', activation='relu'))
b14.add(Dense(b15 = 60, kernel_initializer='uniform', activation='relu'))
b14.add(Dense(b15 = 1, kernel_initializer='uniform', activation='sigmoid'))
b14.compile(b16 = 'adam', loss='binary_crossentropy', metrics=['b20'])
b14.fit(b12, y_train, b17 = 10, epochs=20)
b18 = b14.predict(b13)
b18 = (b18 > 0.5)
b19 = confusion_matrix(b10, b18)
print("Confusion Matrix:")
print(b19)
b20 = (b19[0,0] + b19[1,1]) / (b19[0,0] + b19[0,1] + b19[1,0] + b19[1,1])
b21 = b19[1,1] / (b19[1,1] + b19[0,1])
b22 = b19[1,0] / (b19[1,0] + b19[0,0])
b23 = b19[1,1] / (b19[1,1] + b19[1,0])
b24 = 2 * ((b23 * b21) / (b23 + b21))
b25 = -b23 * log(b23)
print("Accuracy:", b20)
print("Recall:", b21)
print("False Positive Rate:", b22)
print("Precision:", b23)
print("F-measure:", b24)
print("Entropy:", b25)