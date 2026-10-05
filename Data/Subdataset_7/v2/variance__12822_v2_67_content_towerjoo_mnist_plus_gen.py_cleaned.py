import random
import os
import uuid
from keras.datasets import mnist
from PIL import Image
def fonk1(b1 = 5000, test_samples=1000):
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    b2 = "datasets/train/"
    b3 = "datasets/test/"
    if not os.path.exists(b2):
        os.makedirs(b2)
    if not os.path.exists(b3):
        os.makedirs(b3)
    for i in range(b1 + test_samples):
        if i < b1:
            b4 = x_train
            b5 = y_train
            b6 = b2
        else:
            b4 = x_test
            b5 = y_test
            b6 = b3
        b7 = random.choice(range(b4.shape[0]))
        b8 = Image.fromarray(b4[b7])
        b9 = str(b5[b7])
        b10 = random.random() * 0.5 + 0.5
        b11 = (int(b8.size[0] * b10), int(b8.size[1] * b10))
        b8 = b8.resize(b11)
        b12 = random.randint(0, 90)
        b8 = b8.rotate(b12)
        b8 = b8.resize((28, 28))
        b13 = "{}{}-{}.jpg".format(b6, b9, uuid.uuid4().hex)
        b8.save(b13)
if b14 = = "__main__":
    fonk1()