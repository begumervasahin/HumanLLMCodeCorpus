import pandas as pd
import numpy as np
b1 = "irisTraining.txt"
b2 = "irisTesting.txt"
b3 = pd.read_csv(b1, sep=" ", header=None)
b4 = pd.read_csv(b2, sep=" ", header=None)
b5 = b4.shape[1]
b6 = list(range(b5 - 1))
b6.append("label")
b3.b7 = b6
b4.b7 = b6
b8 = b3[b3['label'] == 1].shape[0]
b9 = b3[b3['label'] == -1].shape[0]
b10 = b4['label']
del b4['label']
a1 = 0
a2 = 0
a3 = 0
a4 = 0
def fonk1(x, m, s):
    return (1/(2 * np.pi * s**2)**0.5) * np.exp(-1 * (x-m)**2 / (2 * s**2))
b11 = b4.shape[0]
for i in range(b11):
    b12 = b4.iloc[i]
    a5 = 1
    a6 = 1
    for attribute, value in b12.iteritems():
        b13 = np.array(b3[b3['label'] == 1][attribute])
        b14 = np.average(b13)
        b15 = np.std(b13)
        b16 = np.array(b3[b3['label'] == -1][attribute])
        b17 = np.average(b16)
        b18 = np.std(b16)
        a5 *= fonk1(value, b14, b15)
        a6 *= fonk1(value, b17, b18)
    a5 = a5 * b8
    a6 = a6 * b9
    b19 = 1 if a5 > a6 else -1
    b20 = b10.values[i]
    if b19 = = 1:
        if b20 = = 1:
            a1 += 1
        else:
            a3 += 1
    elif b19 = = -1:
        if b20 = = -1:
            a2 += 1
        else:
            a4 += 1
print('--- ---')
print('Counts:')
print('True Positive Count:', a1)
print('True Negative Count:', a2)
print('False Positive Count:', a3)
print('False Negative Count:', a4)
b21 = (a1 + a2) / total_test_rows
print('Accuracy:', b21)
b22 = a1 / (a1 + a4)
print('Sensitivity / Recall:', b22)
b23 = a2 / (a3 + a2)
print('Specificity:', b23)
b24 = a1 / (a1 + a3)
print('Precision:', b24)