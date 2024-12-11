import pandas as pd
from sklearn.externals import joblib
b1 = joblib.load('Random_Forest.pkl')
b2 = joblib.load('Neural_Network.pkl')
b3 = pd.read_csv("Test_Data_Table.csv")
b4 = b3.label
b3 = b3.drop(b3.columns[0], axis=1)
b3 = b3.drop(labels=['label'], axis=1)
b5 = pd.read_csv("Data_Table_Preprocessed.csv")
b5 = b5.drop(b5.columns[0], axis=1)
b6 = pd.DataFrame()
for column in b5.columns:
    b6[column] = b3[column]
a1 = 0
a2 = 0
a3 = 0
for i in range(len(b3)):
    b7 = pd.DataFrame(columns=b6.columns)
    b7.loc[0] = b6.loc[i]
    b8 = b4.loc[i]
    b9 = b2.predict(b7)
    b10 = b1.predict(b7)
    if b9 = = b10 and b9 == b8:
        a1 += 1
    elif b9 != b10:
        a2 += 1
    elif b9 = = b10 and b9 != b8:
        a3 += 1
    print("Correct predictions:", a1)
    print("No predictions:", a2)
    print("Incorrect predictions:", a3)