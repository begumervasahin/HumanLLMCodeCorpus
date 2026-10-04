
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
b5 = [LabelEncoder() for _ in range(3)]
for i, col in enumerate([1, 2, 3]):
    b3[:, col] = b5[i].fit_transform(b3[:, col])
b6 = OneHotEncoder()
b3 = b6.fit_transform(b3).toarray()
b7 = LabelEncoder()
b4 = b7.fit_transform(b4)
b10, b11, y_train, b8 = train_test_split(b3, b4, test_size=0.3, random_state=0)
b9 = StandardScaler()
b10 = b9.fit_transform(b10)
b11 = b9.transform(b11)
b12 = Sequential()
b12.add(Dense(b13 = 60, kernel_initializer='uniform', activation='relu', input_dim=b10.shape[1]))
b12.add(Dense(b13 = 60, kernel_initializer='uniform', activation='relu'))
b12.add(Dense(b13 = 60, kernel_initializer='uniform', activation='relu'))
b12.add(Dense(b13 = 1, kernel_initializer='uniform', activation='sigmoid'))
b12.compile(b14 = 'adam', loss='binary_crossentropy', metrics=['b18'])
b12.fit(b10, y_train, b15 = 10, epochs=20)
b16 = (b12.predict(b11) > 0.5)
b17 = confusion_matrix(b8, b16)
print("Confusion Matrix:")
print(b17)
b18 = (b17[0, 0] + b17[1, 1]) / np.sum(b17)
b19 = b17[1, 1] / (b17[1, 1] + b17[0, 1])
b20 = b17[1, 0] / (b17[1, 0] + b17[0, 0])
b21 = b17[1, 1] / (b17[1, 1] + b17[1, 0])
b22 = 2 * ((b21 * b19) / (b21 + b19))
b23 = -b21 * log(b21)
print("Accuracy:", b18)
print("Recall:", b19)
print("False Positive Rate:", b20)
print("Precision:", b21)
print("F-measure:", b22)
print("Entropy:", b23)