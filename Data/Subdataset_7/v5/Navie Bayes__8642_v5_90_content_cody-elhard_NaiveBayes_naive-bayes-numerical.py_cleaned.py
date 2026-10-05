import pandas as pd
import numpy as np
def fonk1(b22, b23):
    b1 = pd.read_csv(b22, sep=" ", header=None)
    b2 = pd.read_csv(b23, sep=" ", header=None)
    b3 = b2.shape[1]
    b4 = list(range(b3 - 1))
    b4.append("label")
    b1.b5 = b4
    b2.b5 = b4
    return b1, b2
def fonk2(b1):
    b6 = b1[b1['label'] == 1].shape[0]
    b7 = b1[b1['label'] == -1].shape[0]
    return b6, b7
def fonk3(x, mean, std_dev):
    return (1 / (2 * np.pi * std_dev**2)**0.5) * np.exp(-1 * (x - mean)**2 / (2 * std_dev**2))
def fonk4(b15, b1, b6, b7):
    a1 = 1
    a2 = 1
    for attribute, value in b15.iteritems():
        b8 = np.array(b1[b1['label'] == 1][attribute])
        b9 = np.average(b8)
        b10 = np.std(b8)
        b11 = np.array(b1[b1['label'] == -1][attribute])
        b12 = np.average(b11)
        b13 = np.std(b11)
        a1 *= fonk3(value, b9, b10)
        a2 *= fonk3(value, b12, b13)
    a1 = a1 * b6
    a2 = a2 * b7
    b14 = 1 if a1 > a2 else -1
    return b14
def fonk5(b2, b24, b1, b6, b7):
    a3 = 0
    a4 = 0
    a5 = 0
    a6 = 0
    for i in range(b2.shape[0]):
        b15 = b2.iloc[i]
        b14 = fonk4(b15, b1, b6, b7)
        b16 = b24.values[i]
        if b14 = = 1:
            if b16 = = 1:
                a3 += 1
            else:
                a5 += 1
        elif b14 = = -1:
            if b16 = = -1:
                a4 += 1
            else:
                a6 += 1
    return a3, a4, a5, a6
def fonk6(a3, a4, a5, a6, total_test_rows):
    print('--- ---')
    print('Counts:')
    print('True Positive Count:', a3)
    print('True Negative Count:', a4)
    print('False Positive Count:', a5)
    print('False Negative Count:', a6)
    b17 = (a3 + a4) / total_test_rows
    print('Accuracy:', b17)
    b18 = a3 / (a3 + a6)
    print('Sensitivity / Recall:', b18)
    b19 = a4 / (a5 + a4)
    print('Specificity:', b19)
    b20 = a3 / (a3 + a5)
    print('Precision:', b20)
if b21 = = "__main__":
    b22 = "irisTraining.txt"
    b23 = "irisTesting.txt"
    b1, b2 = fonk1(b22, b23)
    b6, b7 = fonk2(b1)
    b24 = b2['label']
    del b2['label']
    a3, a4, a5, a6 = fonk5(b2, b24, b1, b6, b7)
    fonk6(a3, a4, a5, a6, b2.shape[0])