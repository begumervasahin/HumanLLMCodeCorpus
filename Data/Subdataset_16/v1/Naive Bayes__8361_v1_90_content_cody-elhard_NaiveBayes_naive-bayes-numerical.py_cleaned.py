import pandas as pd
import numpy as np
b1 = "irisTraining.txt"
b2 = "irisTesting.txt"
b3 = pd.read_csv(b1, sep=" ", header=None)
b4 = pd.read_csv(b2, sep=" ", header=None)
b5 = b4.shape[1]
b6 = list(range(b5 - 1)) + ["label"]
b3.b6 = b6
b4.b6 = b6
b7 = b3[b3['label'] == 1].shape[0]
b8 = b3[b3['label'] == -1].shape[0]
b9 = b4['label']
b4 = b4.drop(b6=['label'])
a1 = 0
a2 = 0
a3 = 0
a4 = 0
def fonk1(x, mean, std):
    return (1 / (np.sqrt(2 * np.pi) * std)) * np.exp(-((x - mean) ** 2) / (2 * std ** 2))
for i in range(b4.shape[0]):
    b10 = b4.iloc[i]
    a5 = 1
    a6 = 1
    for attribute, value in b10.iteritems():
        b11 = b3[b3['label'] == 1][attribute]
        b12 = b3[b3['label'] == -1][attribute]
        yes_mean, b13 = b11.mean(), b11.std()
        no_mean, b14 = b12.mean(), b12.std()
        a5 *= fonk1(value, yes_mean, b13)
        a6 *= fonk1(value, no_mean, b14)
    a5 *= b7
    a6 *= b8
    b15 = 1 if a5 > a6 else -1
    b16 = b9.iloc[i]
    if b15 = = 1:
        if b16 = = 1:
            a1 += 1
        else:
            a3 += 1
    else:
        if b16 = = -1:
            a2 += 1
        else:
            a4 += 1
print('--- ---')
print('counts')
print(f'a1: {a1}')
print(f'a2: {a2}')
print(f'a3: {a3}')
print(f'a4: {a4}')
b17 = b4.shape[0]
b18 = (a1 + a2) / b17
b19 = a1 / (a1 + a4)
b20 = a2 / (a2 + a3)
b21 = a1 / (a1 + a3)
print(f'b18: {b18:.2f}')
print(f'b19 / recall: {b19:.2f}')
print(f'b20: {b20:.2f}')
print(f'b21: {b21:.2f}')