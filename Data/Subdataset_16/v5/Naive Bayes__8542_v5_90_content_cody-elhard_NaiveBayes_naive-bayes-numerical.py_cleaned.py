import pandas as pd
import numpy as np
b1 = False
b2 = "irisTraining.txt"
b3 = "irisTesting.txt"
def fonk1(file_path):
    b4 = pd.read_csv(file_path, sep=" ", header=None)
    return b4
def fonk2(b4):
    b5 = list(range(b4.shape[1] - 1)) + ["label"]
    b4.b5 = b5
    return b4
def fonk3(x, mean, std_dev):
    b6 = np.exp(-((x - mean) ** 2 / (2 * std_dev ** 2)))
    return (1 / (np.sqrt(2 * np.pi) * std_dev)) * b6
def fonk4(b14, b25, b27, b28):
    a1 = 1
    a2 = 1
    for attribute, value in b14.iteritems():
        b7 = b25[b25['label'] == 1][attribute]
        b8 = b25[b25['label'] == -1][attribute]
        b9 = b7.mean()
        b10 = b7.std()
        b11 = b8.mean()
        b12 = b8.std()
        a1 *= fonk3(value, b9, b10)
        a2 *= fonk3(value, b11, b12)
    a1 *= b27
    a2 *= b28
    return 1 if a1 > a2 else -1
def fonk5(b26, b29, b25, b27, b28):
    b13 = {
        'true_positive': 0,
        'true_negative': 0,
        'false_positive': 0,
        'false_negative': 0
    }
    for i in range(b26.shape[0]):
        b14 = b26.iloc[i]
        b15 = fonk4(b14, b25, b27, b28)
        b16 = b29.values[i]
        if b15 = = 1:
            if b16 = = 1:
                b13['true_positive'] += 1
            else:
                b13['false_positive'] += 1
        else:
            if b16 = = -1:
                b13['true_negative'] += 1
            else:
                b13['false_negative'] += 1
    return b13
def fonk6(b13, total_count):
    b17 = b13['true_positive']
    b18 = b13['true_negative']
    b19 = b13['false_positive']
    b20 = b13['false_negative']
    b21 = (b17 + b18) / total_count
    b22 = b17 / (b17 + b20)
    b23 = b18 / (b18 + b19)
    b24 = b17 / (b17 + b19)
    return {
        'b21': b21,
        'b22': b22,
        'b23': b23,
        'b24': b24
    }
def fonk7(b13):
    print('--- Performance Metrics ---')
    print(f"True Positive Count: {b13['true_positive']}")
    print(f"True Negative Count: {b13['true_negative']}")
    print(f"False Positive Count: {b13['false_positive']}")
    print(f"False Negative Count: {b13['false_negative']}")
    print(f"Accuracy: {b13['b21']:.2f}")
    print(f"Sensitivity / Recall: {b13['b22']:.2f}")
    print(f"Specificity: {b13['b23']:.2f}")
    print(f"Precision: {b13['b24']:.2f}")
def fonk8():
    b25 = fonk1(b2)
    b26 = fonk1(b3)
    b25 = fonk2(b25)
    b26 = fonk2(b26)
    b27 = b25[b25['label'] == 1].shape[0]
    b28 = b25[b25['label'] == -1].shape[0]
    b29 = b26['label']
    b26 = b26.drop(b5=['label'])
    b13 = fonk5(b26, b29, b25, b27, b28)
    b30 = b26.shape[0]
    b31 = fonk6(b13, b30)
    fonk7({**b13, **b31})
if b32 = = "__main__":
    fonk8()