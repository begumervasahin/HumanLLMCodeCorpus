import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
import keras
from keras.models import Sequential
from keras.layers import Dense
b1 = pd.read_csv('kddcup.data_10_percent_corrected')
b1['normal.'] = b1['normal.'].replace(['back.', 'buffer_overflow.', 'ftp_write.', 'guess_passwd.', 'imap.', 'ipsweep.', 'land.', 'loadmodule.', 'multihop.', 'neptune.', 'nmap.', 'perl.', 'phf.', 'pod.', 'portsweep.', 'rootkit.', 'satan.', 'smurf.', 'spy.', 'teardrop.', 'warezclient.', 'warezmaster.'], 'attack')
b2 = [LabelEncoder() for _ in range(3)]
b3 = [OneHotEncoder(categories='auto') for _ in range(3)]
b4 = [1, 2, 3]
for i in range(3):
    b1.iloc[:, b4[i]] = b2[i].fit_transform(b1.iloc[:, b4[i]])
    b5 = b3[i].fit_transform(b1.iloc[:, b4[i]].values.reshape(-1, 1)).toarray()
    b1.drop(b6 = [b1.b6[b4[i]]], inplace=True)
    for j in range(b5.shape[1]):
        b1[f'encoded_{i}_{j}'] = b5[:, j]
b7 = LabelEncoder()
b8 = b7.fit_transform(b1.iloc[:, -1])
b1.drop(b6 = [b1.b6[-1]], inplace=True)
b11, b12, y_train, b9 = train_test_split(b1.values, b8, test_size=0.3, random_state=0)
b10 = StandardScaler()
b11 = b10.fit_transform(b11)
b12 = b10.transform(b12)
b13 = Sequential()
b13.add(Dense(b14 = 60, kernel_initializer='uniform', activation='relu', input_dim=118))
b13.add(Dense(b14 = 60, kernel_initializer='uniform', activation='relu'))
b13.add(Dense(b14 = 60, kernel_initializer='uniform', activation='relu'))
b13.add(Dense(b14 = 1, kernel_initializer='uniform', activation='sigmoid'))
b13.compile(b15 = 'adam', loss='binary_crossentropy', metrics=['b19'])
b13.fit(b11, y_train, b16 = 10, epochs=20)
b17 = (b13.predict(b12) > 0.5)
b18 = confusion_matrix(b9, b17)
b19 = (b18[0, 0] + b18[1, 1]) / b18.sum()
b20 = b18[1, 1] / (b18[0, 1] + b18[1, 1])
b21 = b18[1, 1] / (b18[1, 0] + b18[1, 1])
b22 = 2 * ((b21 * b20) / (b21 + b20))
b23 = -b21 * np.log(b21)
print("Confusion Matrix:\n", b18)
print("Accuracy:", b19)
print("Recall:", b20)
print("Precision:", b21)
print("F-measure:", b22)
print("Entropy:", b23)