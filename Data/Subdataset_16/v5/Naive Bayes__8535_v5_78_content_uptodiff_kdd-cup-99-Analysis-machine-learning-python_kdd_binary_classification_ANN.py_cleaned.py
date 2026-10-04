
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.b27 import confusion_matrix
from keras.models import Sequential
from keras.layers import Dense
from math import log
def fonk1(b18):
    b1 = pd.read_csv(b18)
    b2 = [
        'back.', 'buffer_overflow.', 'ftp_write.', 'guess_passwd.', 'imap.', 'ipsweep.',
        'land.', 'loadmodule.', 'multihop.', 'neptune.', 'nmap.', 'perl.', 'phf.',
        'pod.', 'portsweep.', 'rootkit.', 'satan.', 'smurf.', 'spy.', 'teardrop.',
        'warezclient.', 'warezmaster.'
    ]
    b1['normal.'] = b1['normal.'].replace(b2, 'attack')
    b3 = b1.iloc[:, :-1].values
    b4 = b1.iloc[:, -1].values
    b5 = [LabelEncoder() for _ in range(3)]
    for i in range(1, 4):
        b3[:, i] = b5[i - 1].fit_transform(b3[:, i])
    b6 = [OneHotEncoder(categorical_features=[i]) for i in [1, 4, 70]]
    for encoder in b6:
        b3 = encoder.fit_transform(b3).toarray()
    b7 = LabelEncoder()
    b4 = b7.fit_transform(b4)
    return b3, b4
def fonk2(b23):
    b8 = Sequential()
    b8.add(Dense(b9 = 60, kernel_initializer='uniform', activation='relu', b23=b23))
    b8.add(Dense(b9 = 60, kernel_initializer='uniform', activation='relu'))
    b8.add(Dense(b9 = 60, kernel_initializer='uniform', activation='relu'))
    b8.add(Dense(b9 = 1, kernel_initializer='uniform', activation='sigmoid'))
    b8.compile(b10 = 'adam', loss='binary_crossentropy', b27=['b12'])
    return b8
def fonk3(b19, b26):
    b11 = confusion_matrix(b19, b26)
    b12 = (b11[0, 0] + b11[1, 1]) / np.sum(b11)
    b13 = b11[1, 1] / (b11[0, 1] + b11[1, 1])
    b14 = b11[1, 0] / (b11[0, 0] + b11[1, 0])
    b15 = b11[1, 1] / (b11[1, 0] + b11[1, 1])
    b16 = 2 * ((b15 * b13) / (b15 + b13))
    b17 = -b15 * log(b15)
    return {
        "b12": b12,
        "b13": b13,
        "b14": b14,
        "b15": b15,
        "b16": b16,
        "b17": b17
    }
def fonk4():
    b18 = 'kddcup.data_10_percent_corrected'
    b3, b4 = fonk1(b18)
    b21, b22, y_train, b19 = train_test_split(b3, b4, test_size=0.3, random_state=0)
    b20 = StandardScaler()
    b21 = b20.fit_transform(b21)
    b22 = b20.transform(b22)
    b23 = b21.shape[1]
    b24 = fonk2(b23)
    b24.fit(b21, y_train, b25 = 10, epochs=20)
    b26 = b24.predict(b22)
    b26 = (b26 > 0.5)
    b27 = fonk3(b19, b26)
    print(f"The Accuracy is: {b27['b12']:.2f}")
    print(f"Recall is: {b27['b13']:.2f}")
    print(f"False Positive Rate: {b27['b14']:.2f}")
    print(f"Precision is: {b27['b15']:.2f}")
    print(f"F-measure is: {b27['b16']:.2f}")
    print(f"Entropy is: {b27['b17']:.2f}")
if b28 = = "__main__":
    fonk4()