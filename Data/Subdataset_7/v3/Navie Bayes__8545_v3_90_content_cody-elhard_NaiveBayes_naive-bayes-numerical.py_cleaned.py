import pandas as pd
import numpy as np
def fonk1(x, mean, std_dev):
    return (1 / (2 * np.pi * std_dev**2)**0.5) * np.exp(-1 * (x - mean)**2 / (2 * std_dev**2))
def fonk2(file_path, b1 = " ", header=None):
    b2 = pd.read_csv(file_path, b1=b1, header=header)
    b3 = [str(i) for i in range(b2.shape[1] - 1)]
    b3.append("label")
    b2.b4 = b3
    return b2
def fonk3(b26, b25):
    b5 = b25[b25['label'] == 1].shape[0]
    b6 = b25[b25['label'] == -1].shape[0]
    b7 = b26['label']
    del b26['label']
    a1 = 0
    a2 = 0
    a3 = 0
    a4 = 0
    b8 = b26.shape[0]
    for i in range(b8):
        b9 = b26.iloc[i]
        a5 = 1
        a6 = 1
        for attribute, value in b9.iteritems():
            b10 = np.array(b25[b25['label'] == 1][attribute])
            b11 = np.average(b10)
            b12 = np.std(b10)
            b13 = np.array(b25[b25['label'] == -1][attribute])
            b14 = np.average(b13)
            b15 = np.std(b13)
            a5 *= fonk1(value, b11, b12)
            a6 *= fonk1(value, b14, b15)
        a5 = a5 * b5
        a6 = a6 * b6
        b16 = 1 if a5 > a6 else -1
        b17 = b7.values[i]
        if b16 = = 1:
            if b17 = = 1:
                a1 += 1
            else:
                a3 += 1
        elif b16 = = -1:
            if b17 = = -1:
                a2 += 1
            else:
                a4 += 1
    b18 = (a1 + a2) / b8
    b19 = a1 / (a1 + a4)
    b20 = a2 / (a3 + a2)
    b21 = a1 / (a1 + a3)
    return b18, b19, b20, b21
if b22 = = "__main__":
    b23 = "irisTraining.txt"
    b24 = "irisTesting.txt"
    b25 = fonk2(b23)
    b26 = fonk2(b24)
    b18, b19, b20, b21 = fonk3(b26, b25)
    print('Counts:')
    print('True Positive Count:', a1)
    print('True Negative Count:', a2)
    print('False Positive Count:', a3)
    print('False Negative Count:', a4)
    print('Metrics:')
    print('Accuracy:', b18)
    print('Sensitivity / Recall:', b19)
    print('Specificity:', b20)
    print('Precision:', b21)