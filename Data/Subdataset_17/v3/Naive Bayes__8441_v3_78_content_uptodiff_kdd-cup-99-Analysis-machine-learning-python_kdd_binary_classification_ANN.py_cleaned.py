
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from keras.models import Sequential
from keras.layers import Dense
from math import log
dataset = pd.read_csv('kddcup.data_10_percent_corrected')
attack_types = [
    'back.', 'buffer_overflow.', 'ftp_write.', 'guess_passwd.', 'imap.', 'ipsweep.', 'land.',
    'loadmodule.', 'multihop.', 'neptune.', 'nmap.', 'perl.', 'phf.', 'pod.', 'portsweep.',
    'rootkit.', 'satan.', 'smurf.', 'spy.', 'teardrop.', 'warezclient.', 'warezmaster.'
]
dataset['normal.'] = dataset['normal.'].replace(attack_types, 'attack')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values
label_encoders = [LabelEncoder() for _ in range(3)]
categorical_columns = [1, 2, 3]
for i, col in enumerate(categorical_columns):
    X[:, col] = label_encoders[i].fit_transform(X[:, col])
onehotencoder = OneHotEncoder()
X = onehotencoder.fit_transform(X).toarray()
labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
classifier = Sequential([
    Dense(units=60, kernel_initializer='uniform', activation='relu', input_dim=X_train.shape[1]),
    Dense(units=60, kernel_initializer='uniform', activation='relu'),
    Dense(units=60, kernel_initializer='uniform', activation='relu'),
    Dense(units=1, kernel_initializer='uniform', activation='sigmoid')
])
classifier.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
classifier.fit(X_train, y_train, batch_size=10, epochs=20)
y_pred = (classifier.predict(X_test) > 0.5)
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(cm)
def calculate_metrics(cm):
    accuracy = (cm[0, 0] + cm[1, 1]) / np.sum(cm)
    recall = cm[1, 1] / (cm[1, 1] + cm[0, 1])
    false_positive_rate = cm[1, 0] / (cm[1, 0] + cm[0, 0])
    precision = cm[1, 1] / (cm[1, 1] + cm[1, 0])
    f_measure = 2 * ((precision * recall) / (precision + recall))
    entropy = -precision * log(precision) if precision > 0 else 0
    return accuracy, recall, false_positive_rate, precision, f_measure, entropy
accuracy, recall, false_positive_rate, precision, f_measure, entropy = calculate_metrics(cm)
print(f"Accuracy: {accuracy:.4f}")
print(f"Recall: {recall:.4f}")
print(f"False Positive Rate: {false_positive_rate:.4f}")
print(f"Precision: {precision:.4f}")
print(f"F-measure: {f_measure:.4f}")
print(f"Entropy: {entropy:.4f}")