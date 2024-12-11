import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
import keras
from keras.models import Sequential
from keras.layers import Dense
b1 = pd.read_csv('kddcup.data_10_percent_corrected')
b2 = ['back.', 'buffer_overflow.', 'ftp_write.', 'guess_passwd.', 'imap.', 'ipsweep.', 'land.', 'loadmodule.', 'multihop.', 'neptune.', 'nmap.', 'perl.', 'phf.', 'pod.', 'portsweep.', 'rootkit.', 'satan.', 'smurf.', 'spy.', 'teardrop.', 'warezclient.', 'warezmaster.']
b1['normal.'] = b1['normal.'].replace(b2, 'attack')
b3 = [LabelEncoder() for _ in range(3)]
b4 = [OneHotEncoder(categories='auto') for _ in range(3)]
b5 = [1, 2, 3]
for i in range(3):
    b1.iloc[:, b5[i]] = b3[i].fit_transform(b1.iloc[:, b5[i]])
    b6 = b4[i].fit_transform(b1.iloc[:, b5[i]].values.reshape(-1, 1)).toarray()
    b1.drop(b7 = [b1.b7[b5[i]]], inplace=True)
    for j in range(b6.shape[1]):
        b1[f'encoded_{i}_{j}'] = b6[:, j]
b8 = LabelEncoder()
b9 = b8.fit_transform(b1.iloc[:, -1])
b1.drop(b7 = [b1.b7[-1]], inplace=True)
b12, b13, y_train, b10 = train_test_split(b1.values, b9, test_size=0.3, random_state=0)
b11 = StandardScaler()
b12 = b11.fit_transform(b12)
b13 = b11.transform(b13)
b14 = Sequential()
b14.add(Dense(b15 = 60, kernel_initializer='uniform', activation='relu', input_dim=118))
b14.add(Dense(b15 = 60, kernel_initializer='uniform', activation='relu'))
b14.add(Dense(b15 = 60, kernel_initializer='uniform', activation='relu'))
b14.add(Dense(b15 = 1, kernel_initializer='uniform', activation='sigmoid'))
b14.compile(b16 = 'adam', loss='binary_crossentropy', metrics=['b20'])
b14.fit(b12, y_train, b17 = 10, epochs=20)
b18 = (b14.predict(b13) > 0.5)
b19 = confusion_matrix(b10, b18)
b20 = (b19[0, 0] + b19[1, 1]) / b19.sum()
b21 = b19[1, 1] / (b19[0, 1] + b19[1, 1])
b22 = b19[1, 1] / (b19[1, 0] + b19[1, 1])
b23 = 2 * ((b22 * b21) / (b22 + b21))
b24 = -b22 * np.log(b22)
print("Confusion Matrix:\n", b19)
print("Accuracy:", b20)
print("Recall:", b21)
print("Precision:", b22)
print("F-measure:", b23)
print("Entropy:", b24)