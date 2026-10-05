import random
import os
import uuid
from keras.datasets import mnist
from PIL import Image
def fonk1(b1 = 5000, test_samples=1000):
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    b2 = "datasets/train/"
    b3 = "datasets/test/"
    fonk2(b2, b3)
    for i in range(b1 + test_samples):
        data, labels, b4 = fonk3(x_train, y_train, x_test, y_test, i, b1, b2, b3)
        b6, b5 = fonk4(data, labels)
        b6 = fonk5(b6)
        b6 = fonk6(b6)
        b7 = fonk7(b5, b4)
        fonk8(b6, b7)
def fonk2(b2, b3):
    os.makedirs(b2, b8 = True)
    os.makedirs(b3, b8 = True)
def fonk3(x_train, y_train, x_test, y_test, b9, b1, b2, b3):
    if b9 < b1:
        return x_train, y_train, b2
    else:
        return x_test, y_test, b3
def fonk4(data, labels):
    b9 = random.choice(range(data.shape[0]))
    b6 = Image.fromarray(data[b9])
    b5 = str(labels[b9])
    return b6, b5
def fonk5(b6):
    b10 = random.random() * 0.5 + 0.5
    b11 = (int(b6.size[0] * b10), int(b6.size[1] * b10))
    b6 = b6.resize(b11)
    b12 = random.randint(0, 90)
    b6 = b6.rotate(b12)
    return b6
def fonk6(b6):
    return b6.resize((28, 28))
def fonk7(b5, b4):
    return "{}{}-{}.jpg".format(b4, b5, uuid.uuid4().hex)
def fonk8(b6, b7):
    b6.save(b7)
if b13 = = "__main__":
    fonk1()