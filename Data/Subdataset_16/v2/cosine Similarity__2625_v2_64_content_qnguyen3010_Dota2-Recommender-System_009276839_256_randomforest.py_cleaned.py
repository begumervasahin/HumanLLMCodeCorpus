
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, f1_score
def fonk1(b12, b13):
    b1 = pd.read_csv(b12)
    b2 = pd.read_csv(b13)
    b3 = b1.iloc[:, 0].values
    b4 = b1.iloc[:, 4:].values
    b5 = b2.iloc[:, 0].values
    b6 = b2.iloc[:, 4:].values
    return b4, b3, b6, b5
def fonk2(b4, b3):
    b7 = RandomForestClassifier(max_features='log2', n_estimators=100, criterion='entropy', random_state=0)
    b7.fit(b4, b3)
    return b7
def fonk3(b7, b6, b5):
    b8 = b7.predict(b6)
    b9 = confusion_matrix(b5, b8)
    print("Confusion Matrix:")
    print(b9)
    b10 = accuracy_score(b5, b8)
    print("\nAccuracy:", b10)
    b11 = f1_score(b5, b8, average='macro')
    print("F1 Score:", b11)
def fonk4():
    b12 = 'dota2Train.csv'
    b13 = 'dota2Test.csv'
    b4, b3, b6, b5 = fonk1(b12, b13)
    b7 = fonk2(b4, b3)
    fonk3(b7, b6, b5)
if b14 = = "__main__":
    fonk4()