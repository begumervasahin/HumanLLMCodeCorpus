
import random
import os
import uuid
from keras.datasets import mnist
import matplotlib.pyplot as plt
from PIL import Image
def generate_dataset(train_samples=5000, test_samples=1000):
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    train_dir = "datasets/train/"
    test_dir = "datasets/test/"
    if not os.path.exists(train_dir):
        os.makedirs(train_dir)
    if not os.path.exists(test_dir):
        os.makedirs(test_dir)
    for i in range(train_samples + test_samples):
        index = random.choice(range(x_train.shape[0]))
        image = Image.fromarray(x_train[index])
        label = str(y_train[index])
        resize_ratio = random.random() * 0.5 + 0.5
        new_size = (int(image.size[0] * resize_ratio), int(image.size[1] * resize_ratio))
        image = image.resize(new_size)
        rotate_degree = random.randint(0, 90)
        image = image.rotate(rotate_degree)
        image = image.resize((28, 28))
        if i < train_samples:
            path = "{}{}-{}.jpg".format(train_dir, label, uuid.uuid4().hex)
        else:
            path = "{}{}-{}.jpg".format(test_dir, label, uuid.uuid4().hex)
        image.save(path)
if __name__ == "__main__":
    generate_dataset()
