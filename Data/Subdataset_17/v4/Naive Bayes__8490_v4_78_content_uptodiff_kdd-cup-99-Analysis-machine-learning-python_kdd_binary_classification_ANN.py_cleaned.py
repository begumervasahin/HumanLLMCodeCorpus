
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from keras.models import Sequential
from keras.layers import Dense
from math import log
dataset = pd.read_csv('kddcup.data_10_percent_corrected')
attack_types = [
    'back.', 'buffer_overflow.', 'ftp_write.', 'guess_passwd.', 'imap.', 'ipsweep.',
    'land.', 'loadmodule.', 'multihop.', 'neptune.', 'nmap.', 'perl.', 'phf.',
    'pod.', 'portsweep.', 'rootkit.', 'satan.', 'smurf.', 'spy.', 'teardrop.',
    'warezclient.', 'warezmaster.'
]
dataset['normal.'] = dataset['normal.'].replace(attack_types, 'attack')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 41].values
label_encoders = [LabelEncoder() for _ in range(3)]
X[:, 1] = label_encoders[0].fit_transform(X[:, 1])
X[:, 2] = label_encoders[1].fit_transform(X[:, 2])
X[:, 3] = label_encoders[2].fit_transform(X[:, 3])
onehot_encoders = [OneHotEncoder(categorical_features=[i]) for i in [1, 4, 70]]
for encoder in onehot_encoders:
    X = encoder.fit_transform(X).toarray()
label_encoder_y = LabelEncoder()
y = label_encoder_y.fit_transform(y)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
classifier = Sequential()
classifier.add(Dense(units=60, kernel_initializer='uniform', activation='relu', input_dim=118))
classifier.add(Dense(units=60, kernel_initializer='uniform', activation='relu'))
classifier.add(Dense(units=60, kernel_initializer='uniform', activation='relu'))
classifier.add(Dense(units=1, kernel_initializer='uniform', activation='sigmoid'))
classifier.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
classifier.fit(X_train, y_train, batch_size=10, epochs=20)
y_pred = classifier.predict(X_test)
y_pred = (y_pred > 0.5)
cm = confusion_matrix(y_test, y_pred)
accuracy = (cm[0, 0] + cm[1, 1]) / np.sum(cm)
recall = cm[1, 1] / (cm[0, 1] + cm[1, 1])
false_positive_rate = cm[1, 0] / (cm[0, 0] + cm[1, 0])
precision = cm[1, 1] / (cm[1, 0] + cm[1, 1])
f_measure = 2 * ((precision * recall) / (precision + recall))
entropy = -precision * log(precision)
print(f"The Accuracy is: {accuracy:.2f}")
print(f"Recall is: {recall:.2f}")
print(f"False Positive Rate: {false_positive_rate:.2f}")
print(f"Precision is: {precision:.2f}")
print(f"F-measure is: {f_measure:.2f}")
print(f"Entropy is: {entropy:.2f}")