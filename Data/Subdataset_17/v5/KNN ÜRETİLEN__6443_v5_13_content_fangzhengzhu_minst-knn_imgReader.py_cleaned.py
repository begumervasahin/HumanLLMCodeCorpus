import os
import numpy as np
class DataSet:
    def __init__(self, image_file, label_file, num_samples, height=28, width=28):
        self.image_file = image_file
        self.label_file = label_file
        self.num_samples = num_samples
        self.height = height
        self.width = width
        self.data = np.zeros((self.num_samples, self.height * self.width), dtype=np.uint8)
        self.labels = np.zeros(self.num_samples, dtype=np.uint8)
    def read_images(self):
        with open(self.image_file, "rb") as file:
            self.skip_header(file)
            for i in range(self.num_samples):
                self.data[i] = np.frombuffer(file.read(self.height * self.width), dtype=np.uint8)
    def read_labels(self):
        with open(self.label_file, "rb") as file:
            self.skip_header(file, 8)
            self.labels = np.frombuffer(file.read(self.num_samples), dtype=np.uint8)
    @staticmethod
    def skip_header(file, offset=16):
        file.seek(offset, os.SEEK_CUR)
    def get_data(self):
        return self.data
    def get_labels(self):
        return self.labels
class TrainDataSet:
    def __init__(self, train_file, train_label_file, test_file, test_label_file):
        self.train_set = DataSet(train_file, train_label_file, 60000)
        self.test_set = DataSet(test_file, test_label_file, 10000)
    def load_data(self):
        self.train_set.read_images()
        self.train_set.read_labels()
        self.test_set.read_images()
        self.test_set.read_labels()
    def get_train_data(self):
        return self.train_set.get_data(), self.train_set.get_labels()
    def get_test_data(self):
        return self.test_set.get_data(), self.test_set.get_labels()
def main():
    train_file = input("Enter the training image file path: ")
    train_label_file = input("Enter the training label file path: ")
    test_file = input("Enter the testing image file path: ")
    test_label_file = input("Enter the testing label file path: ")
    dataset = TrainDataSet(train_file, train_label_file, test_file, test_label_file)
    dataset.load_data()
    train_data, train_labels = dataset.get_train_data()
    test_data, test_labels = dataset.get_test_data()
    print(f"Training data shape: {train_data.shape}")
    print(f"Training labels shape: {train_labels.shape}")
    print(f"Testing data shape: {test_data.shape}")
    print(f"Testing labels shape: {test_labels.shape}")
if __name__ == "__main__":
    main()