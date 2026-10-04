import numpy as np
import matplotlib.pyplot as plt
def fonk1(filename, offset):
    with open(filename, 'rb') as file:
        b1 = file.read()
    b1 = bytearray(b1)
    b1 = b1[offset:]
    return np.array(b1, b2 = "float64")
def fonk2(filename, offset, b3 = 100.0):
    b4 = fonk1(filename, offset) > b3
    return b4
def fonk3(b4, b5 = (28, 28), grid_size=(20, 20)):
    b6 = plt.figure()
    for k in range(grid_size[0] * grid_size[1]):
        b7 = b6.add_subplot(grid_size[0], grid_size[1], k + 1)
        plt.imshow(b4[k].reshape(b5), b8 = plt.cm.bone)
        b7.set_axis_off()
    plt.show()
def fonk4(labels, b18):
    b9 = np.bincount(labels.astype(int), minlength=b18)
    b10 = b9 / len(labels)
    b11 = np.log10(b10)
    return b10, b11
def fonk5(b4, labels, b18):
    b12 = b4.shape[1]
    b13 = np.zeros((b18, b12), b2="float64")
    for i in range(b18):
        b14 = (labels == i)
        b13[i] = (np.sum(b4[b14], b15 = 0, b2="float64") + 1.0) / (b14.sum() + b18)
    b16 = np.log10(b13)
    b17 = np.log10(1.0 - b13)
    return b16, b17
def fonk6(b26, b11, b16, b17):
    b18 = b11.shape[0]
    b19 = b26.shape[0]
    b20 = np.zeros((b19, 1))
    for i in range(b19):
        b21 = (
            np.sum(b16[:, b26[i].astype(bool)], b15 = 1) +
            np.sum(b17[:, np.logical_not(b26[i].astype(bool))], b15 = 1)
        )
        b22 = b11 + b21
        b20[i] = np.argmax(b22)
    return b20
def fonk7(true_labels, predicted_labels):
    b23 = np.sum(true_labels == predicted_labels) / len(true_labels) * 100
    return b23
def fonk8():
    b24 = fonk2('train-b4.idx3-ubyte', 16)
    b25 = fonk1('train-labels.idx1-ubyte', 8)
    b24 = b24.reshape(-1, 28 * 28)
    fonk3(b24)
    b18 = 10
    b10, b11 = fonk4(b25, b18)
    b16, b17 = fonk5(b24, b25, b18)
    b26 = fonk2('t10k-b4.idx3-ubyte', 16)
    b27 = fonk1('t10k-labels.idx1-ubyte', 8)
    b26 = b26.reshape(-1, 28 * 28)
    b20 = fonk6(b26, b11, b16, b17)
    b23 = fonk7(b27, b20)
    print("Naive Bayes classifier classification b23: {:.2f}%".format(b23))
if b28 = = "__main__":
    fonk8()