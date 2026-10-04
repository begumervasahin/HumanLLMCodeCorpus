import os
import numpy as np
class TrainDataSet:
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
    def get_train_label(self):
        return self.train_label_set
    def get_test_set(self):
        return self.test_data_set
    def get_test_label(self):
        return self.test_label_set
    def read_test_img(self):
        self._read_images(self.test_img_file, self.test_data_set, self.TEST_NUM)
    def read_train_img(self):
        self._read_images(self.train_img_file, self.train_data_set, self.TRAIN_NUM)
    def read_test_label(self):
        self._read_labels(self.test_label_file, self.test_label_set, self.TEST_NUM)
    def read_train_label(self):
        self._read_labels(self.train_label_file, self.train_label_set, self.TRAIN_NUM)
    def _read_images(self, file_path, data_set, num_images):
        with open(file_path, "rb") as file:
            if not file:
                print(f"Error: {file_path} not found.")
                return
            self._skip_header(file)
            for i in range(num_images):
                data_set[i] = np.frombuffer(file.read(self.HEIGHT * self.WIDTH), dtype=np.uint8)
    def _read_labels(self, file_path, label_set, num_labels):
        with open(file_path, "rb") as file:
            if not file:
                print(f"Error: {file_path} not found.")
                return
            self._skip_header(file, 8)
            label_set[:] = np.frombuffer(file.read(num_labels), dtype=np.uint8)
    def _skip_header(self, file, offset=16):
        file.seek(offset, os.SEEK_CUR)
if __name__ == "__main__":
    print("Place the MNIST dataset files in the same directory as this script.")
    train_img_file = input("Enter the name of the training image file: ")
    train_label_file = input("Enter the name of the training label file: ")
    test_img_file = input("Enter the name of the testing image file: ")
    test_label_file = input("Enter the name of the testing label file: ")
    dataset = TrainDataSet(train_img_file, train_label_file, test_img_file, test_label_file)
    dataset.read_train_img()
    dataset.read_train_label()
    dataset.read_test_img()
    dataset.read_test_label()
    print("Training images and labels read successfully.")
    print("Testing images and labels read successfully.")