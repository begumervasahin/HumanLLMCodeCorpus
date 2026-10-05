import os
import numpy as np
class DataSetLoader:
    def __init__(self, train_img_file, train_label_file, test_img_file, test_label_file):
        self.train_img_file = train_img_file
        self.test_img_file = test_img_file
        self.train_label_file = train_label_file
        self.test_label_file = test_label_file
        self.TRAIN_NUM = 60000
        self.TEST_NUM = 10000
        self.HEIGHT = 28
        self.WIDTH = 28
        self.train_data_set = np.zeros((self.TRAIN_NUM, self.HEIGHT * self.WIDTH), dtype=np.uint8)
        self.test_data_set = np.zeros((self.TEST_NUM, self.HEIGHT * self.WIDTH), dtype=np.uint8)
        self.train_label_set = np.zeros(self.TRAIN_NUM, dtype=np.uint8)
        self.test_label_set = np.zeros(self.TEST_NUM, dtype=np.uint8)
    def get_train_set(self):
        return self.train_data_set
    def get_train_labels(self):
        return self.train_label_set
    def get_test_set(self):
        return self.test_data_set
    def get_test_labels(self):
        return self.test_label_set
    def read_test_images(self):
        with open(self.test_img_file, "rb") as file:
            self.skip_header(file)
            for i in range(self.TEST_NUM):
                self.test_data_set[i] = np.frombuffer(file.read(self.HEIGHT * self.WIDTH), dtype=np.uint8)
    def read_train_images(self):
        with open(self.train_img_file, "rb") as file:
            self.skip_header(file)
            for i in range(self.TRAIN_NUM):
                self.train_data_set[i] = np.frombuffer(file.read(self.HEIGHT * self.WIDTH), dtype=np.uint8)
    def read_test_labels(self):
        with open(self.test_label_file, "rb") as file:
            self.skip_header(file, 8)
            self.test_label_set = np.frombuffer(file.read(self.TEST_NUM), dtype=np.uint8)
    def read_train_labels(self):
        with open(self.train_label_file, "rb") as file:
            self.skip_header(file, 8)
            self.train_label_set = np.frombuffer(file.read(self.TRAIN_NUM), dtype=np.uint8)
    def skip_header(self, file, offset=16):
        file.seek(offset, os.SEEK_CUR)
train_img_file = "train-images.idx3-ubyte"
train_label_file = "train-labels.idx1-ubyte"
test_img_file = "t10k-images.idx3-ubyte"
test_label_file = "t10k-labels.idx1-ubyte"
loader = DataSetLoader(train_img_file, train_label_file, test_img_file, test_label_file)
loader.read_train_images()
loader.read_train_labels()
loader.read_test_images()
loader.read_test_labels()
train_set = loader.get_train_set()
train_labels = loader.get_train_labels()
test_set = loader.get_test_set()
test_labels = loader.get_test_labels()