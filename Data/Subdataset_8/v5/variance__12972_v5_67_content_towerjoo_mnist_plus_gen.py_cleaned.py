import random
import os
import uuid
from keras.datasets import mnist
from PIL import Image
def generate_dataset(train_samples=5000, test_samples=1000):
    (x_train, y_train), _ = mnist.load_data()
    train_dir = "datasets/train/"
    test_dir = "datasets/test/"
    create_directories(train_dir, test_dir)
    generate_data(x_train, y_train, train_dir, train_samples)
    _, (x_test, y_test) = mnist.load_data()
    generate_data(x_test, y_test, test_dir, test_samples)
def create_directories(train_dir, test_dir):
    for directory in [train_dir, test_dir]:
        if not os.path.exists(directory):
            os.makedirs(directory)
def generate_data(images, labels, directory, num_samples):
    for i in range(num_samples):
        index = random.choice(range(images.shape[0]))
        image = Image.fromarray(images[index])
        label = str(labels[index])
        image = apply_random_transformations(image)
        image = image.resize((28, 28))
        file_name = f"{label}-{uuid.uuid4().hex}.jpg"
        path = os.path.join(directory, file_name)
        image.save(path)
def apply_random_transformations(image):
    resize_ratio = random.random() * 0.5 + 0.5
    new_size = (int(image.size[0] * resize_ratio), int(image.size[1] * resize_ratio))
    image = image.resize(new_size)
    rotate_degree = random.randint(0, 90)
    image = image.rotate(rotate_degree)
    return image
if __name__ == "__main__":
    generate_dataset()