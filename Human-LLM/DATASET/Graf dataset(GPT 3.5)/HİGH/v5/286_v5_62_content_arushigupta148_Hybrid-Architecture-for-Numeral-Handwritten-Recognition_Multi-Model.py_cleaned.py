import pandas as pd
from sklearn.externals import joblib
b1 = joblib.load('Random_Forest.pkl')
b2 = joblib.load('Neural_Network.pkl')
b3 = pd.read_csv("Test_Data_Table.csv")
b4 = b3.pop('label')
b5 = pd.read_csv("Data_Table_Preprocessed.csv")
b5.drop(b5.columns[0], b6 = 1, inplace=True)
b7 = b3[b5.columns]
a1 = 0
a2 = 0
a3 = 0
for i, sample in b7.iterrows():
    b8 = sample.values.reshape(1, -1)
    b9 = b4[i]
    b10 = b2.predict(b8)
    b11 = b1.predict(b8)
    if b10 = = b11 == b9:
        a1 += 1
    elif b10 != b11:
        a2 += 1
    elif b10 = = b11 != b9:
        a3 += 1
    print("Correct predictions:", a1)
    print("No predictions:", a2)
    print("Incorrect predictions:", a3)