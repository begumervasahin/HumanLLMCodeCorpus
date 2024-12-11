import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler
from sklearn.metrics import confusion_matrix
from keras.models import Sequential
from keras.layers import Dense
b1 = pd.read_csv('kddcup.data_10_percent_corrected')
b1['normal.'] = b1['normal.'].replace([...], 'attack')
b2 = b1.iloc[:, :-1].values
b3 = b1.iloc[:, 41].values
b4 = LabelEncoder()
b5 = LabelEncoder()
b6 = LabelEncoder()
b2[:, 1] = b4.fit_transform(b2[:, 1])
b2[:, 2] = b5.fit_transform(b2[:, 2])
b2[:, 3] = b6.fit_transform(b2[:, 3])
b7 = OneHotEncoder(categorical_features=[1])
b2 = b7.fit_transform(b2).toarray()
b8 = OneHotEncoder(categorical_features=[4])
b2 = b8.fit_transform(b2).toarray()
b9 = OneHotEncoder(categorical_features=[70])
b2 = b9.fit_transform(b2).toarray()
b10 = LabelEncoder()
b3 = b10.fit_transform(b3)
b13, b14, y_train, b11 = train_test_split(b2, b3, test_size=0.3, random_state=0)
b12 = StandardScaler()
b13 = b12.fit_transform(b13)
b14 = b12.transform(b14)
b15 = Sequential()
b15.add(Dense(b16 = 60, kernel_initializer='uniform', activation='relu', input_dim=118))
b15.add(Dense(b16 = 60, kernel_initializer='uniform', activation='relu'))
b15.add(Dense(b16 = 60, kernel_initializer='uniform', activation='relu'))
b15.add(Dense(b16 = 1, kernel_initializer='uniform', activation='sigmoid'))
b15.compile(b17 = 'adam', loss='binary_crossentropy', metrics=['b21'])
b15.fit(b13, y_train, b18 = 10, epochs=20)
b19 = b15.predict(b14)
b19 = (b19 > 0.5)
b20 = confusion_matrix(b11, b19)
b21 = (b20[0, 0] + b20[1, 1]) / np.sum(b20)
b22 = b20[1, 1] / (b20[0, 1] + b20[1, 1])
b23 = b20[1, 0] / (b20[0, 0] + b20[1, 0])
b24 = b20[1, 1] / (b20[1, 0] + b20[1, 1])
b25 = 2 * ((b24 * b22) / (b24 + b22))
b26 = -b24 * np.log(b24)
print("Accuracy:", b21)
print("Recall:", b22)
print("False Positive Rate:", b23)
print("Precision:", b24)
print("F-Measure:", b25)
print("Entropy:", b26)