import numpy as np
import matplotlib.pyplot as plt
b1 = open('train-images.idx3-ubyte','rb')
b2 = b1.read()
b2 = bytearray(b2)
b2 = b2[16:]
b1.close()
b2 = np.array(b2,"float64") > 100.
b3 = 28 * 28
b4 = b2.shape[0] / b3
a1 = 1
b5 = plt.figure()
for a2 in range(20*20):
    b6 = b5.add_subplot(20, 20, a2 + 1)
    plt.imshow(b2[(a1-1)*b3: a1*b3].reshape(28,28), b7 = plt.cm.bone)
    b6.set_axis_off()
    a1 += 1
plt.show()
b2 = b2.reshape(int(b4), b3)
b8 = open('train-labels.idx1-ubyte','rb')
b9 = b8.read()
b9 = bytearray(b9)
b9 = b9[8:]
b8.close()
b9 = np.array(b9)
b10 = b9.reshape(b9.shape[0], 1)
a2 = 10
b11 = np.bincount(b9)
b12 = b11 / b4
b13 = np.log10(b12)
b14 = np.zeros((a2, b3), "float64")
for a1 in range(a2):
        b15 = (b9 == a1)
        b14[a1] += (np.sum(b2[b15], b16 = 0, dtype="float64") + 1.) / (b11[a1] + a2)
b17 = np.log10(b14)
b18 = np.log10(1. - b14)
b19 = open('t10k-images.idx3-ubyte','rb')
b20 = b19.read()
b20 = bytearray(b20)
b20 = b20[16:]
b19.close()
b20 = np.array(b20,"float64") > 100.
b3 = 28 * 28
b4 = b20.shape[0] / b3
b20 = b20.reshape(int(b4), b3)
b21 = open('t10k-labels.idx1-ubyte','rb')
b22 = b21.read()
b22 = bytearray(b22)
b22 = b22[8:]
b21.close()
b22 = np.array(b22)
b23 = b22.reshape(b22.shape[0], 1)
b24 = np.zeros(b23.shape)
for a1 in range(b20.shape[0]):
    b25 = np.sum(b17[:, b20[a1].reshape(-1)], b16=1) + np.sum(b18[:, np.logical_not(b20[a1].reshape(-1))], b16=1)
    b26 = b13 + b25
    b24[a1] = np.argmax(b26)
b27 = np.sum(b23 == b24)
print("Naive Bayes classifier classification accuracy:", float(b27 / len(b23))*100., '%')