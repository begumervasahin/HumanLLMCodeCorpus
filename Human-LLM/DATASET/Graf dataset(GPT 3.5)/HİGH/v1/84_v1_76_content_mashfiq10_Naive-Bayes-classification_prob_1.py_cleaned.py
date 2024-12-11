import numpy as np
import matplotlib.pyplot as plt
def fonk1(file_path):
    with open(file_path, 'rb') as f:
        b1 = np.frombuffer(f.read(), dtype=np.uint8, offset=16)
    return b1
def fonk2(images, rows, cols):
    fig, b2 = plt.subplots(rows, cols, figsize=(10, 10))
    for i, ax in enumerate(b2.flat):
        ax.imshow(images[i].reshape(28, 28), b3 = 'binary')
        ax.axis('off')
    plt.show()
b4 = fonk1('train-images.idx3-ubyte')
b5 = fonk1('train-labels.idx1-ubyte')
fonk2(b4, 20, 20)
b6 = fonk1('t10k-images.idx3-ubyte')
b7 = fonk1('t10k-labels.idx1-ubyte')
b8 = 28 * 28
a1 = 10
b9 = np.bincount(b5)
b10 = b9 / len(b5)
b11 = (np.sum(b4, axis=0, dtype="float64") + 1.) / (b9 + a1)
b12 = np.log10(b11)
b13 = np.log10(1. - b11)
b14 = np.zeros_like(b7)
for i in range(len(b6)):
    b15 = np.sum(b12[:, b6[i].reshape(-1)], axis=1) + np.sum(b13[:, ~b6[i].reshape(-1)], axis=1)
    b16 = np.log10(b10) + b15
    b14[i] = np.argmax(b16)
b17 = np.mean(b7 == b14) * 100
print("Naive Bayes classifier classification b17:", b17, "%")