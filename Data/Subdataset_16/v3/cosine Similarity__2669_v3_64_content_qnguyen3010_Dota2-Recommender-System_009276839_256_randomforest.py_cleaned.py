
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, f1_score
def fonk1(b15, b16):
    b1 = pd.read_csv(b15)
    b2 = pd.read_csv(b16)
    b3 = b1.iloc[:, 0].values
    b4 = b1.iloc[:, 4:].values
    b5 = b2.iloc[:, 0].values
    b6 = b2.iloc[:, 4:].values
    return b4, b3, b6, b5
def fonk2(b4, b3):
    b7 = RandomForestClassifier(
        b8 = 'log2',
        b9 = 100,
        b10 = 'entropy',
        a1 = 0
    )
    b7.fit(b4, b3)
    return b7
def fonk3(b7, b6, b5):
    b11 = b7.predict(b6)
    b12 = confusion_matrix(b5, b11)
    print("Confusion Matrix:")
    print(b12)
    b13 = accuracy_score(b5, b11)
    print("\nAccuracy:", b13)
    b14 = f1_score(b5, b11, average='macro')
    print("F1 Score:", b14)
def fonk4():
    b15 = 'dota2Train.csv'
    b16 = 'dota2Test.csv'
    b4, b3, b6, b5 = fonk1(b15, b16)
    b7 = fonk2(b4, b3)
    fonk3(b7, b6, b5)
if b17 = = "__main__":
    fonk4()