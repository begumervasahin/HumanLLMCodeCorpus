import numpy as np
import matplotlib.pyplot as plt
b1 = open('train-images.idx3-ubyte', 'rb')
b2 = bytearray(b1.read())[16:]
b1.close()
b2 = np.array(b2, dtype=np.float64) > 100.
b3 = plt.figure()
for a1 in range(20 * 20):
    b4 = b3.add_subplot(20, 20, a1 + 1)
    plt.imshow(b2[a1].reshape(28, 28), b5 = plt.cm.bone)
    b4.set_axis_off()
plt.show()
b6 = 28 * 28
b7 = b2.shape[0]
b2 = b2.reshape(int(b7), b6)
b8 = open('train-labels.idx1-ubyte', 'rb')
b9 = bytearray(b8.read())[8:]
b8.close()
b9 = np.array(b9)
b9 = b9.reshape(b9.shape[0], 1)
a1 = 10
b10 = np.bincount(b9)
b11 = b10 / b7
b12 = np.log10(b11)
b13 = np.zeros((a1, b6), dtype=np.float64)
for i in range(a1):
    b14 = (b9 == i)
    b13[i] += (np.sum(b2[b14], b15 = 0, dtype=np.float64) + 1.) / (b10[i] + a1)
b16 = np.log10(b13)
b17 = np.log10(1. - b13)
b18 = open('t10k-images.idx3-ubyte', 'rb')
b19 = bytearray(b18.read())[16:]
b18.close()
b19 = np.array(b19, dtype=np.float64) > 100.
b19 = b19.reshape(int(b7), b6)
b20 = open('t10k-labels.idx1-ubyte', 'rb')
b21 = bytearray(b20.read())[8:]
b20.close()
b21 = np.array(b21)
b21 = b21.reshape(b21.shape[0], 1)
b22 = np.zeros(b21.shape)
for i in range(b19.shape[0]):
    b23 = np.sum(b16[:, b19[i].reshape(-1)], b15=1) + np.sum(b17[:, np.logical_not(b19[i].reshape(-1))], b15=1)
    b24 = b12 + b23
    b22[i] = np.argmax(b24)
b25 = np.sum(b21 == b22)
b26 = float(b25 / len(b21)) * 100.
print("Naive Bayes classifier classification b26:", b26, '%')