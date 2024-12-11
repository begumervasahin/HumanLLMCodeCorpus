
import random
import os
import uuid
from keras.datasets import mnist
import matplotlib.pyplot as plt
from PIL import Image
def fonk1(b1 = 5000, test_samples=1000):
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    b2 = "datasets/train/"
    b3 = "datasets/test/"
    if not os.b10.exists(b2):
        os.makedirs(b2)
    if not os.b10.exists(b3):
        os.makedirs(b3)
    for i in range(b1 + test_samples):
        b4 = random.choice(range(x_train.shape[0]))
        b5 = Image.fromarray(x_train[b4])
        b6 = str(y_train[b4])
        b7 = random.random() * 0.5 + 0.5
        b8 = (int(b5.size[0] * b7), int(b5.size[1] * b7))
        b5 = b5.resize(b8)
        b9 = random.randint(0, 90)
        b5 = b5.rotate(b9)
        b5 = b5.resize((28, 28))
        if i < b1:
            b10 = "{}{}-{}.jpg".format(b2, b6, uuid.uuid4().hex)
        else:
            b10 = "{}{}-{}.jpg".format(b3, b6, uuid.uuid4().hex)
        b5.save(b10)
if b11 = = "__main__":
    fonk1()
