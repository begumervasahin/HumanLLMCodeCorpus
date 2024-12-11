import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler
from sklearn.metrics import confusion_matrix
from keras.models import Sequential
from keras.layers import Dense
def fonk1(file_path):
    b1 = pd.read_csv(file_path)
    b1['normal.'] = b1['normal.'].replace([...], 'attack')
    b2 = b1.iloc[:, :-1].values
    b3 = b1.iloc[:, 41].values
    return b2, b3
def fonk2(b2):
    b4 = [LabelEncoder() for _ in range(3)]
    for i in range(3):
        b2[:, i] = b4[i].fit_transform(b2[:, i])
    b5 = [OneHotEncoder(categories='auto') for _ in range(3)]
    for i in [1, 4, 70]:
        b2 = b5[i].fit_transform(b2).toarray()
    return b2
def fonk3(b3):
    b6 = LabelEncoder()
    b3 = b6.fit_transform(b3)
    return b3
def fonk4(b2, b3, b7 = 0.3, random_state=0):
    b10, b11, y_train, b8 = train_test_split(b2, b3, b7=b7, random_state=random_state)
    return b10, b11, y_train, b8
def fonk5(b10, b11):
    b9 = StandardScaler()
    b10 = b9.fit_transform(b10)
    b11 = b9.transform(b11)
    return b10, b11
def fonk6(b24):
    b12 = Sequential()
    b12.add(Dense(b13 = 60, kernel_initializer='uniform', activation='relu', b24=b24))
    b12.add(Dense(b13 = 60, kernel_initializer='uniform', activation='relu'))
    b12.add(Dense(b13 = 60, kernel_initializer='uniform', activation='relu'))
    b12.add(Dense(b13 = 1, kernel_initializer='uniform', activation='sigmoid'))
    b12.compile(b14 = 'adam', loss='binary_crossentropy', metrics=['b18'])
    return b12
def fonk7(b12, b10, y_train, b15 = 10, epochs=20):
    b12.fit(b10, y_train, b15 = b15, epochs=epochs)
def fonk8(b12, b11):
    b16 = b12.predict(b11)
    b16 = (b16 > 0.5)
    return b16
def fonk9(b8, b16):
    b17 = confusion_matrix(b8, b16)
    b18 = (b17[0, 0] + b17[1, 1]) / np.sum(b17)
    b19 = b17[1, 1] / (b17[0, 1] + b17[1, 1])
    b20 = b17[1, 0] / (b17[0, 0] + b17[1, 0])
    b21 = b17[1, 1] / (b17[1, 0] + b17[1, 1])
    b22 = 2 * ((b21 * b19) / (b21 + b19))
    b23 = -b21 * np.log(b21)
    return b18, b19, b20, b21, b22, b23
b2, b3 = fonk1('kddcup.data_10_percent_corrected')
b2 = fonk2(b2)
b3 = fonk3(b3)
b10, b11, y_train, b8 = fonk4(b2, b3)
b10, b11 = fonk5(b10, b11)
b24 = b10.shape[1]
b12 = fonk6(b24)
fonk7(b12, b10, y_train)
b16 = fonk8(b12, b11)
b18, b19, b20, b21, b22, b23 = fonk9(b8, b16)
print("Accuracy:", b18)
print("Recall:", b19)
print("False Positive Rate:", b20)
print("Precision:", b21)
print("F-Measure:", b22)
print("Entropy:", b23)