import random
import os
import uuid
from keras.datasets import mnist
from PIL import Image
def fonk1(b1 = 5000, test_samples=1000):
    (x_train, y_train), b2 = mnist.load_data()
    b3 = "datasets/train/"
    b4 = "datasets/test/"
    fonk2(b3, b4)
    fonk3(x_train, y_train, b3, b1)
    b2, (x_test, y_test) = mnist.load_data()
    fonk3(x_test, y_test, b4, test_samples)
def fonk2(b3, b4):
    for directory in [b3, b4]:
        if not os.b9.exists(directory):
            os.makedirs(directory)
def fonk3(images, labels, directory, num_samples):
    for i in range(num_samples):
        b5 = random.choice(range(images.shape[0]))
        b6 = Image.fromarray(images[b5])
        b7 = str(labels[b5])
        b6 = fonk4(b6)
        b6 = b6.resize((28, 28))
        b8 = f"{b7}-{uuid.uuid4().hex}.jpg"
        b9 = os.b9.join(directory, b8)
        b6.save(b9)
def fonk4(b6):
    b10 = random.random() * 0.5 + 0.5
    b11 = (int(b6.size[0] * b10), int(b6.size[1] * b10))
    b6 = b6.resize(b11)
    b12 = random.randint(0, 90)
    b6 = b6.rotate(b12)
    return b6
if b13 = = "__main__":
    fonk1()