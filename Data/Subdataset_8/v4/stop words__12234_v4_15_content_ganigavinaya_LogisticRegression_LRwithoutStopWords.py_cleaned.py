import os
import io
import re
import numpy as np
class LogisticRegression:
    def __init__(self, trainHam, trainSpam, testHam, testSpam):
        self.trainHam = trainHam
        self.trainSpam = trainSpam
        self.testHam = testHam
        self.testSpam = testSpam
        self.weights = {}
        self.vocabulary = []
        self.learning_rate = 0.0001
        self.lambda_val = 5
        self.file_data = []
    def run(self):
        self.create_vocabulary()
        self.process_folders(self.trainHam, 1.0)
        self.process_folders(self.trainSpam, 0.0)
    def count_words(self, path, word_count):
        with io.open(path, 'r', encoding='iso-8859-1') as f:
            lines = f.readlines()
            for line in lines:
                letters_only = re.sub("[^a-zA-Z0-9\s]", "", line).lower().split()
                for word in letters_only:
                    if word in word_count:
                        word_count[word] += 1
                    else:
                        word_count[word] = 1
    def create_vocabulary(self):
        ham_words = {}
        self.process_folders_and_count_words(self.trainHam, ham_words)
        spam_words = {}
        self.process_folders_and_count_words(self.trainSpam, spam_words)
        self.vocabulary = set(ham_words.keys()).union(spam_words.keys())
        for word in self.vocabulary:
            self.weights[word] = 0.0
    def process_folders_and_count_words(self, folder_path, word_count):
        folder = os.listdir(folder_path)
        for file_name in folder:
            file_path = os.path.join(folder_path, file_name)
            self.count_words(file_path, word_count)
    def process_folders(self, folder_path, classification):
        folder = os.listdir(folder_path)
        for file_name in folder:
            file_path = os.path.join(folder_path, file_name)
            word_count = {}
            self.count_words(file_path, word_count)
            self.file_data.append({'fileName': file_path, 'token': word_count, 'class': classification})
    def train(self):
        for _ in range(500):
            self.update_error()
            self.update_weights()
    def update_error(self):
        for file_data in self.file_data:
            tokens = file_data["token"]
            value = 1
            for token in tokens:
                value += tokens[token] * self.weights[token]
            file_data["error"] = self.sigmoid(value)
    def sigmoid(self, x):
        denom = 1 + np.exp(-x)
        return 1 / denom
    def update_weights(self):
        for token in self.weights.keys():
            val = 0
            for file_data in self.file_data:
                tokens = file_data["token"]
                true_value = file_data["class"]
                if token in tokens:
                    temp = true_value - file_data["error"]
                    val += tokens[token] * temp
            self.weights[token] += ((val * self.learning_rate) - (self.learning_rate * self.lambda_val * self.weights[token]))
    def test(self):
        ham_correct = self.test_folder_accuracy(self.testHam, threshold=0.5)
        spam_correct = self.test_folder_accuracy(self.testSpam, threshold=0.5)
        ham_accuracy = (ham_correct / len(os.listdir(self.testHam))) * 100
        spam_accuracy = (spam_correct / len(os.listdir(self.testSpam))) * 100
        total_accuracy = ((ham_correct + spam_correct) / (len(os.listdir(self.testHam)) + len(os.listdir(self.testSpam)))) * 100
        print("Ham accuracy is ", ham_accuracy)
        print("Spam accuracy is ", spam_accuracy)
        print("Total accuracy is ", total_accuracy)
    def test_folder_accuracy(self, folder_path, threshold):
        correct = 0
        folder = os.listdir(folder_path)
        for file_name in folder:
            file_path = os.path.join(folder_path, file_name)
            file_dict = {}
            value = 0
            self.count_words(file_path, file_dict)
            for token in file_dict:
                if token in self.weights:
                    value += self.weights[token] * file_dict[token]
            result = self.sigmoid(value)
            if (result > threshold and folder_path == self.testHam) or (result < threshold and folder_path == self.testSpam):
                correct += 1
        return correct
