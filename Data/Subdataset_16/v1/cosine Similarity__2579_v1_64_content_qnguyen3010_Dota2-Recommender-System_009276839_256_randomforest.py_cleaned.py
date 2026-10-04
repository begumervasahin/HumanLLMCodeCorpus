
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, f1_score
b1 = pd.read_csv('dota2Train.csv')
b2 = pd.read_csv('dota2Test.csv')
b3 = b1.iloc[:, 0].values
b4 = b1.iloc[:, 4:].values
b5 = b2.iloc[:, 0].values
b6 = b2.iloc[:, 4:].values
b7 = RandomForestClassifier(max_features='log2', n_estimators=100, criterion='entropy', random_state=0)
b7.fit(b4, b3)
b8 = b7.predict(b6)
b9 = confusion_matrix(b5, b8)
print("Confusion Matrix:")
print(b9)
b10 = accuracy_score(b5, b8)
print("\nAccuracy:", b10)
b11 = f1_score(b5, b8, average='macro')
print("F1 Score:", b11)