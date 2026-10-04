
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
b2 = [
    'back.', 'buffer_overflow.', 'ftp_write.', 'guess_passwd.', 'imap.', 'ipsweep.', 'land.',
    'loadmodule.', 'multihop.', 'neptune.', 'nmap.', 'perl.', 'phf.', 'pod.', 'portsweep.',
    'rootkit.', 'satan.', 'smurf.', 'spy.', 'teardrop.', 'warezclient.', 'warezmaster.'
]
b1['normal.'] = b1['normal.'].replace(b2, 'attack')
b3 = b1.iloc[:, :-1].values
b4 = b1.iloc[:, -1].values
b5 = [LabelEncoder() for _ in range(3)]
b6 = [1, 2, 3]
for i, col in enumerate(b6):
    b3[:, col] = b5[i].fit_transform(b3[:, col])
b7 = OneHotEncoder()
b3 = b7.fit_transform(b3).toarray()
b8 = LabelEncoder()
b4 = b8.fit_transform(b4)
b11, b12, y_train, b9 = train_test_split(b3, b4, test_size=0.3, random_state=0)
b10 = StandardScaler()
b11 = b10.fit_transform(b11)
b12 = b10.transform(b12)
b13 = Sequential([
    Dense(b14 = 60, kernel_initializer='uniform', activation='relu', input_dim=b11.shape[1]),
    Dense(b14 = 60, kernel_initializer='uniform', activation='relu'),
    Dense(b14 = 60, kernel_initializer='uniform', activation='relu'),
    Dense(b14 = 1, kernel_initializer='uniform', activation='sigmoid')
])
b13.compile(b15 = 'adam', loss='binary_crossentropy', metrics=['b19'])
b13.fit(b11, y_train, b16 = 10, epochs=20)
b17 = (b13.predict(b12) > 0.5)
b18 = confusion_matrix(b9, b17)
print("Confusion Matrix:")
print(b18)
def fonk1(b18):
    b19 = (b18[0, 0] + b18[1, 1]) / np.sum(b18)
    b20 = b18[1, 1] / (b18[1, 1] + b18[0, 1])
    b21 = b18[1, 0] / (b18[1, 0] + b18[0, 0])
    b22 = b18[1, 1] / (b18[1, 1] + b18[1, 0])
    b23 = 2 * ((b22 * b20) / (b22 + b20))
    b24 = -b22 * log(b22) if b22 > 0 else 0
    return b19, b20, b21, b22, b23, b24
b19, b20, b21, b22, b23, b24 = fonk1(b18)
print(f"Accuracy: {b19:.4f}")
print(f"Recall: {b20:.4f}")
print(f"False Positive Rate: {b21:.4f}")
print(f"Precision: {b22:.4f}")
print(f"F-measure: {b23:.4f}")
print(f"Entropy: {b24:.4f}")