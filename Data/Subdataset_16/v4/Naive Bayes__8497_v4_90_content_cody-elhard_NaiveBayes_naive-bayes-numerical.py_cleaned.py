import pandas as pd
import numpy as np
b1 = False
b2 = "irisTraining.txt"
b3 = "irisTesting.txt"
b4 = pd.read_csv(b2, sep=" ", header=None)
b5 = pd.read_csv(b3, sep=" ", header=None)
b6 = list(range(b5.shape[1] - 1)) + ["label"]
b4.b7 = b6
b5.b7 = b6
b8 = b4[b4['label'] == 1].shape[0]
b9 = b4[b4['label'] == -1].shape[0]
b10 = b5['label']
del b5['label']
a1 = 0
a2 = 0
a3 = 0
a4 = 0
def fonk1(x, mean, std_dev):
    return (1 / (2 * np.pi * std_dev**2)**0.5) * np.exp(-1 * (x - mean)**2 / (2 * std_dev**2))
for i in range(b5.shape[0]):
    b11 = b5.iloc[i]
    a5 = 1
    a6 = 1
    for attribute, value in b11.iteritems():
        b12 = np.array(b4[b4['label'] == 1][attribute])
        b13 = np.array(b4[b4['label'] == -1][attribute])
        b14 = np.mean(b12)
        b15 = np.std(b12)
        b16 = np.mean(b13)
        b17 = np.std(b13)
        a5 *= fonk1(value, b14, b15)
        a6 *= fonk1(value, b16, b17)
    a5 *= b8
    a6 *= b9
    b18 = 1 if a5 > a6 else -1
    b19 = b10.values[i]
    if b18 = = 1:
        if b19 = = 1:
            a1 += 1
        else:
            a3 += 1
    elif b18 = = -1:
        if b19 = = -1:
            a2 += 1
        else:
            a4 += 1
b20 = b5.shape[0]
b21 = (a1 + a2) / b20
b22 = a1 / (a1 + a4)
b23 = a2 / (a2 + a3)
b24 = a1 / (a1 + a3)
print('--- Performance Metrics ---')
print(f'True Positive Count: {a1}')
print(f'True Negative Count: {a2}')
print(f'False Positive Count: {a3}')
print(f'False Negative Count: {a4}')
print(f'Accuracy: {b21:.2f}')
print(f'Sensitivity / Recall: {b22:.2f}')
print(f'Specificity: {b23:.2f}')
print(f'Precision: {b24:.2f}')