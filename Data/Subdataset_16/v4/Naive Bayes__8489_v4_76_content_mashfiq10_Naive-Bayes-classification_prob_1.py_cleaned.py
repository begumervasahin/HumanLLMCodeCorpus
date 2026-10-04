import numpy as np
import matplotlib.pyplot as plt
def fonk1(filename, offset):
    with open(filename, 'rb') as file:
        b1 = file.read()
    b1 = bytearray(b1)
    b1 = b1[offset:]
    return np.array(b1, b2 = "float64")
b3 = fonk1('train-images.idx3-ubyte', 16) > 100.0
b4 = 28 * 28
b5 = b3.shape[0]
b6 = plt.figure()
for a1 in range(20 * 20):
    b7 = b6.add_subplot(20, 20, a1 + 1)
    plt.imshow(b3[a1 * b4: (a1 + 1) * b4].reshape(28, 28), b8 = plt.cm.bone)
    b7.set_axis_off()
plt.show()
b3 = b3.reshape(int(b5), b4)
b9 = fonk1('train-labels.idx1-ubyte', 8)
b10 = b9.reshape(b9.shape[0], 1)
a1 = 10
b11 = np.bincount(b9)
b12 = b11 / b5
b13 = np.log10(b12)
b14 = np.zeros((a1, b4), b2="float64")
for i in range(a1):
    b15 = (b9 == i)
    b14[i] = (np.sum(b3[b15], b16 = 0, b2="float64") + 1.0) / (b11[i] + a1)
b17 = np.log10(b14)
b18 = np.log10(1.0 - b14)
b19 = fonk1('t10k-images.idx3-ubyte', 16) > 100.0
b20 = b19.shape[0]
b19 = b19.reshape(int(b20), b4)
b21 = fonk1('t10k-labels.idx1-ubyte', 8)
b22 = b21.reshape(b21.shape[0], 1)
b23 = np.zeros(b22.shape)
for i in range(b19.shape[0]):
    b24 = (
        np.sum(b17[:, b19[i].astype(bool)], b16 = 1) +
        np.sum(b18[:, np.logical_not(b19[i].astype(bool))], b16 = 1)
    )
    b25 = b13 + b24
    b23[i] = np.argmax(b25)
b26 = np.sum(b22 == b23) / len(b22) * 100
print("Naive Bayes classifier classification b26: {:.2f}%".format(b26))