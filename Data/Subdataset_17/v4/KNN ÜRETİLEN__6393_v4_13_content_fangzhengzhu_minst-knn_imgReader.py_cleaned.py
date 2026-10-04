import os
import numpy as np
class TrainDataSet:
    def __init__(self, train_file, train_label_file, test_file, test_label_file):
        self.train_img_file = train_file
        self.test_img_file = test_file
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
    def get_train_label(self):
        return self.train_label_set
    def get_test_set(self):
        return self.test_data_set
    def get_test_label(self):
        return self.test_label_set
    def read_test_img(self):
        with open(self.test_img_file, "rb") as fr:
            self.skip_header(fr)
            for i in range(self.TEST_NUM):
                self.test_data_set[i] = np.frombuffer(fr.read(self.HEIGHT * self.WIDTH), dtype=np.uint8)
    def read_train_img(self):
        with open(self.train_img_file, "rb") as fr:
            self.skip_header(fr)
            for i in range(self.TRAIN_NUM):
                self.train_data_set[i] = np.frombuffer(fr.read(self.HEIGHT * self.WIDTH), dtype=np.uint8)
    def read_test_label(self):
        with open(self.test_label_file, "rb") as fr:
            self.skip_header(fr, 8)
            self.test_label_set = np.frombuffer(fr.read(self.TEST_NUM), dtype=np.uint8)
    def read_train_label(self):
        with open(self.train_label_file, "rb") as fr:
            self.skip_header(fr, 8)
            self.train_label_set = np.frombuffer(fr.read(self.TRAIN_NUM), dtype=np.uint8)
    def skip_header(self, fr, offset=16):
        fr.seek(offset, os.SEEK_CUR)
if __name__ == "__main__":
    train_file = input("Enter the training image file path: ")
    train_label_file = input("Enter the training label file path: ")
    test_file = input("Enter the testing image file path: ")
    test_label_file = input("Enter the testing label file path: ")
    dataset = TrainDataSet(train_file, train_label_file, test_file, test_label_file)
    dataset.read_train_img()
    dataset.read_train_label()
    dataset.read_test_img()
    dataset.read_test_label()
    train_data = dataset.get_train_set()
    train_labels = dataset.get_train_label()
    test_data = dataset.get_test_set()
    test_labels = dataset.get_test_label()
    print(f"Training data shape: {train_data.shape}")
    print(f"Training labels shape: {train_labels.shape}")
    print(f"Testing data shape: {test_data.shape}")
    print(f"Testing labels shape: {test_labels.shape}")