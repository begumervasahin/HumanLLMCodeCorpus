import numpy as np
import matplotlib.pyplot as plt
def fonk1(filename):
    with open(filename, 'rb') as f:
        b1 = f.read()
    b1 = bytearray(b1)
    b1 = np.array(b1[16:], dtype='float64') > 100.
    return b1
def fonk2(filename):
    with open(filename, 'rb') as f:
        b2 = f.read()
    b2 = bytearray(b2)
    b2 = np.array(b2[8:])
    return b2
def fonk3(b1, b3 = 400, cols=20):
    b4 = 28 * 28
    b5 = b3
    b6 = plt.figure(figsize=(10, 10))
    for a1 in range(b3):
        b7 = b6.add_subplot(b5, cols, a1 + 1)
        plt.imshow(b1[a1*b4:(a1+1)*b4].reshape(28, 28), b8 = plt.cm.bone)
        b7.set_axis_off()
    plt.show()
b9 = fonk1('train-b1.idx3-ubyte')
b10 = fonk2('train-b2.idx1-ubyte')
fonk3(b9)
b4 = 28 * 28
b11 = b9.shape[0]
b9 = b9.reshape(int(b11), b4)
a1 = 10
b12 = np.bincount(b10)
b13 = b12 / b11
b14 = np.log10(b13)
b15 = np.zeros((a1, b4), dtype='float64')
for i in range(a1):
    b16 = (b10 == i)
    b15[i] = (np.sum(b9[b16], b17 = 0, dtype='float64') + 1.) / (b12[i] + a1)
b18 = np.log10(b15)
b19 = np.log10(1. - b15)
b20 = fonk1('t10k-b1.idx3-ubyte')
b21 = fonk2('t10k-b2.idx1-ubyte')
b22 = b20.shape[0]
b20 = b20.reshape(int(b22), b4)
b23 = np.zeros(b21.shape, dtype=int)
for i in range(b20.shape[0]):
    b24 = np.sum(b18[:, b20[i].reshape(-1)], b17=1) + \
                     np.sum(b19[:, np.logical_not(b20[i].reshape(-1))], b17 = 1)
    b25 = b14 + b24
    b23[i] = np.argmax(b25)
b26 = np.mean(b21 == b23)
print("Naive Bayes classifier classification b26:", b26 * 100., '%')