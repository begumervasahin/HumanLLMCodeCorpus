import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler
from sklearn.metrics import confusion_matrix
from keras.models import Sequential
from keras.layers import Dense
dataset = pd.read_csv('kddcup.data_10_percent_corrected')
dataset['normal.'] = dataset['normal.'].replace([...], 'attack')
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 41].values
labelencoder_x_1 = LabelEncoder()
labelencoder_x_2 = LabelEncoder()
labelencoder_x_3 = LabelEncoder()
x[:, 1] = labelencoder_x_1.fit_transform(x[:, 1])
x[:, 2] = labelencoder_x_2.fit_transform(x[:, 2])
x[:, 3] = labelencoder_x_3.fit_transform(x[:, 3])
onehotencoder_1 = OneHotEncoder(categorical_features=[1])
x = onehotencoder_1.fit_transform(x).toarray()
onehotencoder_2 = OneHotEncoder(categorical_features=[4])
x = onehotencoder_2.fit_transform(x).toarray()
onehotencoder_3 = OneHotEncoder(categorical_features=[70])
x = onehotencoder_3.fit_transform(x).toarray()
labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)
sc_x = StandardScaler()
x_train = sc_x.fit_transform(x_train)
x_test = sc_x.transform(x_test)
classifier = Sequential()
classifier.add(Dense(units=60, kernel_initializer='uniform', activation='relu', input_dim=118))
classifier.add(Dense(units=60, kernel_initializer='uniform', activation='relu'))
classifier.add(Dense(units=60, kernel_initializer='uniform', activation='relu'))
classifier.add(Dense(units=1, kernel_initializer='uniform', activation='sigmoid'))
classifier.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
classifier.fit(x_train, y_train, batch_size=10, epochs=20)
y_pred = classifier.predict(x_test)
y_pred = (y_pred > 0.5)
cm = confusion_matrix(y_test, y_pred)
accuracy = (cm[0, 0] + cm[1, 1]) / np.sum(cm)
recall = cm[1, 1] / (cm[0, 1] + cm[1, 1])
false_positive_rate = cm[1, 0] / (cm[0, 0] + cm[1, 0])
precision = cm[1, 1] / (cm[1, 0] + cm[1, 1])
f_measure = 2 * ((precision * recall) / (precision + recall))
entropy = -precision * np.log(precision)
print("Accuracy:", accuracy)
print("Recall:", recall)
print("False Positive Rate:", false_positive_rate)
print("Precision:", precision)
print("F-Measure:", f_measure)
print("Entropy:", entropy)