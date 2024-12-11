import pandas as pd
import numpy as np
def fonk1(x, m, s):
    return (1/(2 * np.pi * s**2)**0.5) * np.exp(-1 * (x-m)**2 / (2 * s**2))
b1 = "irisTraining.txt"
b2 = pd.read_csv(b1, sep=" ", header=None)
b3 = "irisTesting.txt"
b4 = pd.read_csv(b3, sep=" ", header=None)
b5 = [str(i) for i in range(b4.shape[1]-1)]
b5.append("label")
b2.b6 = b5
b4.b6 = b5
b7 = b2[b2['label'] == 1].shape[0]
b8 = b2[b2['label'] == -1].shape[0]
b9 = b4['label']
del b4['label']
a1 = 0
a2 = 0
a3 = 0
a4 = 0
b10 = b4.shape[0]
for i in range(b10):
    b11 = b4.iloc[i]
    a5 = 1
    a6 = 1
    for attribute, value in b11.iteritems():
        b12 = np.array(b2[b2['label'] == 1][attribute])
        b13 = np.average(b12)
        b14 = np.std(b12)
        b15 = np.array(b2[b2['label'] == -1][attribute])
        b16 = np.average(b15)
        b17 = np.std(b15)
        a5 *= fonk1(value, b13, b14)
        a6 *= fonk1(value, b16, b17)
    a5 = a5 * b7
    a6 = a6 * b8
    b18 = 1 if a5 > a6 else -1
    b19 = b9.values[i]
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
print('counts')
print('a1:', a1)
print('a2:', a2)
print('a3:', a3)
print('a4:', a4)
b20 = (a1 + a2) / b10
print('b20:', b20)
b21 = a1 / (a1 + a4)
print('b21 / recall:', b21)
b22 = a2 / (a3 + a2)
print('b22:', b22)
b23 = a1 / (a1 + a3)
print('b23:', b23)