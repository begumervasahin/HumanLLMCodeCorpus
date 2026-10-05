import random
import os
import uuid
from keras.datasets import mnist
from PIL import Image
def generate_data(train_samples=5000, test_samples=1000):
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    train_dir = "datasets/train/"
    test_dir = "datasets/test/"
    create_directories(train_dir, test_dir)
    for i in range(train_samples + test_samples):
        data, labels, directory = get_data_and_labels(x_train, y_train, x_test, y_test, i, train_samples, train_dir, test_dir)
        image, label = select_random_image(data, labels)
        image = apply_random_transformations(image)
        image = resize_image(image)
        filename = generate_filename(label, directory)
        save_image(image, filename)
def create_directories(train_dir, test_dir):
    os.makedirs(train_dir, exist_ok=True)
    os.makedirs(test_dir, exist_ok=True)
def get_data_and_labels(x_train, y_train, x_test, y_test, index, train_samples, train_dir, test_dir):
    if index < train_samples:
        return x_train, y_train, train_dir
    else:
        return x_test, y_test, test_dir
def select_random_image(data, labels):
    index = random.choice(range(data.shape[0]))
    image = Image.fromarray(data[index])
    label = str(labels[index])
    return image, label
def apply_random_transformations(image):
    resize_ratio = random.random() * 0.5 + 0.5
    new_size = (int(image.size[0] * resize_ratio), int(image.size[1] * resize_ratio))
    image = image.resize(new_size)
    rotate_degree = random.randint(0, 90)
    image = image.rotate(rotate_degree)
    return image
def resize_image(image):
    return image.resize((28, 28))
def generate_filename(label, directory):
    return "{}{}-{}.jpg".format(directory, label, uuid.uuid4().hex)
def save_image(image, filename):
    image.save(filename)
if __name__ == "__main__":
    generate_data()