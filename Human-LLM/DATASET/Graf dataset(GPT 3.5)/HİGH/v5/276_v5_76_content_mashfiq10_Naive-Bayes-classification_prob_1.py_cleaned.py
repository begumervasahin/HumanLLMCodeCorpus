import numpy as np
import matplotlib.pyplot as plt
def fonk1(file_path):
    with open(file_path, 'rb') as file:
        b1 = bytearray(file.read())[16:]
    b2 = np.array(b1, dtype=np.float64) > 100.
    return b2
def fonk2(file_path):
    with open(file_path, 'rb') as file:
        b1 = bytearray(file.read())[8:]
    b3 = np.array(b1)
    b3 = b3.reshape(b3.shape[0], 1)
    return b3
def fonk3(b2):
    b4 = plt.figure()
    for k in range(20 * 20):
        b5 = b4.add_subplot(20, 20, k + 1)
        plt.imshow(b2[k].reshape(28, 28), b6 = plt.cm.bone)
        b5.set_axis_off()
    plt.show()
def fonk4(b2):
    b7 = 28 * 28
    b8 = b2.shape[0]
    return b2.reshape(int(b8), b7)
def fonk5(b3, a1):
    b9 = np.bincount(b3)
    b10 = b9 / b3.shape[0]
    b11 = np.log10(b10)
    b12 = np.zeros((a1, b7), dtype=np.float64)
    return b9, b10, b11, b12
def fonk6(b2, b3, b9, a1):
    b12 = np.zeros((a1, b7), dtype=np.float64)
    for i in range(a1):
        b13 = (b3 == i)
        b12[i] += (np.sum(b2[b13], b14 = 0, dtype=np.float64) + 1.) / (b9[i] + a1)
    b15 = np.log10(b12)
    b16 = np.log10(1. - b12)
    return b15, b16
def fonk7(images_file, labels_file):
    b2 = fonk1(images_file)
    b3 = fonk2(labels_file)
    b2 = fonk4(b2)
    return b2, b3
def fonk8(b2, b15, b16, b11):
    b17 = np.zeros((b2.shape[0], 1))
    for i in range(b2.shape[0]):
        b18 = np.sum(b15[:, b2[i].reshape(-1)], b14=1) + np.sum(b16[:, np.logical_not(b2[i].reshape(-1))], b14=1)
        b19 = b11 + b18
        b17[i] = np.argmax(b19)
    return b17
def fonk9(predicted_labels, actual_labels):
    b20 = np.sum(predicted_labels == actual_labels)
    b21 = (b20 / len(actual_labels)) * 100.
    return b21
train_images, b22 = fonk7('train-b2.idx3-ubyte', 'train-b3.idx1-ubyte')
fonk3(train_images)
a1 = 10
b7 = 28 * 28
b9, b10, b11, b12 = fonk5(b22, a1)
b15, b16 = fonk6(train_images, b22, b9, a1)
test_images, b23 = fonk7('t10k-b2.idx3-ubyte', 't10k-b3.idx1-ubyte')
b17 = fonk8(test_images, b15, b16, b11)
b21 = fonk9(b17, b23)
print("Naive Bayes classifier classification b21:", b21, '%')