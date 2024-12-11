import numpy as np
import matplotlib.pyplot as plt
def fonk1(file_path):
    with open(file_path, 'rb') as f:
        b1 = np.frombuffer(f.read(), dtype=np.uint8, offset=16)
    return b1
def fonk2(b4, rows, cols):
    fig, b2 = plt.subplots(rows, cols, figsize=(10, 10))
    for i, ax in enumerate(b2.flat):
        ax.imshow(b4[i].reshape(28, 28), b3 = 'binary')
        ax.axis('off')
    plt.show()
def fonk3(images_file, labels_file):
    b4 = fonk1(images_file)
    b5 = fonk1(labels_file)
    return b4, b5
def fonk4(training_images, b16, test_images):
    a1 = 10
    b6 = 28 * 28
    a2 = 1
    b7 = np.bincount(b16)
    b8 = b7 / len(b16)
    b9 = (np.sum(training_images, axis=0, dtype="float64") + a2) / (b7 + a2 * a1)
    b10 = np.log10(b9)
    b11 = np.log10(1. - b9)
    b12 = np.zeros(len(test_images), dtype=int)
    for i in range(len(test_images)):
        b13 = np.sum(b10[:, test_images[i].reshape(-1)], axis=1) + np.sum(b11[:, ~test_images[i].reshape(-1)], axis=1)
        b14 = np.log10(b8) + b13
        b12[i] = np.argmax(b14)
    return b12
def fonk5(true_labels, predicted_labels):
    b15 = np.mean(true_labels == predicted_labels) * 100
    return b15
def fonk6():
    training_images, b16 = fonk3('train-b4.idx3-ubyte', 'train-b5.idx1-ubyte')
    fonk2(training_images, 20, 20)
    test_images, b17 = fonk3('t10k-b4.idx3-ubyte', 't10k-b5.idx1-ubyte')
    b12 = fonk4(training_images, b16, test_images)
    b15 = fonk5(b17, b12)
    print("Naive Bayes classifier classification b15:", b15, "%")
if b18 = = "__main__":
    fonk6()