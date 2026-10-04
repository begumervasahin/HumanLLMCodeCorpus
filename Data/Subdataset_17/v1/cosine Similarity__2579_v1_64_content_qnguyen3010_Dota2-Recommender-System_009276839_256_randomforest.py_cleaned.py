
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, f1_score
dataset = pd.read_csv('dota2Train.csv')
testset = pd.read_csv('dota2Test.csv')
y_train = dataset.iloc[:, 0].values
X_train = dataset.iloc[:, 4:].values
y_test = testset.iloc[:, 0].values
X_test = testset.iloc[:, 4:].values
classifier = RandomForestClassifier(max_features='log2', n_estimators=100, criterion='entropy', random_state=0)
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(cm)
accuracy = accuracy_score(y_test, y_pred)
print("\nAccuracy:", accuracy)
f1 = f1_score(y_test, y_pred, average='macro')
print("F1 Score:", f1)