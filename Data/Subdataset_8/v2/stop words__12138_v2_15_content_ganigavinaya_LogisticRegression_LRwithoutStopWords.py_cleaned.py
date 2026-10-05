import os
import io
import re
import numpy as np
class LogisticRegression:
    def __init__(self, train_ham, train_spam, test_ham, test_spam):
        self.train_ham = train_ham
        self.train_spam = train_spam
        self.test_ham = test_ham
        self.test_spam = test_spam
        self.weights = {}
        self.vocabulary = []
        self.learning_rate = 0.0001
        self.lambda_value = 5
        self.file_data = []
    def run(self):
        self.create_vocabulary()
        self.process_folder(self.train_ham, 1.0)
        self.process_folder(self.train_spam, 0.0)
    def count_words(self, path, word_count):
        with io.open(path, 'r', encoding='iso-8859-1') as f:
            lines = f.readlines()
            for line in lines:
                letters_only = re.sub("[^a-zA-Z0-9\s]", "", line).lower().split()
                for word in letters_only:
                    word_count[word] = word_count.get(word, 0) + 1
    def create_vocabulary(self):
        ham_words = {}
        self.process_folder(self.train_ham, 1.0, word_count=ham_words)
        spam_words = {}
        self.process_folder(self.train_spam, 0.0, word_count=spam_words)
        self.vocabulary = set(ham_words.keys()).union(spam_words.keys())
        for word in self.vocabulary:
            self.weights[word] = 0.0
    def process_folder(self, folder, classification, word_count=None):
        files = os.listdir(folder)
        for file in files:
            file_path = os.path.join(folder, file)
            if word_count is None:
                word_count = {}
            self.count_words(file_path, word_count)
            self.file_data.append({'file_name': file_path, 'token': word_count, 'class': classification})
    def train(self):
        for _ in range(500):
            self.update_error()
            self.update_weights()
    def update_error(self):
        total_error = 0
        for file_data in self.file_data:
            token = file_data["token"]
            value = 1
            for every_token in token:
                value += token[every_token] * self.weights[every_token]
            file_data["error"] = self.sigmoid(value)
            total_error += file_data["error"]
    def sigmoid(self, x):
        denom = 1 + np.exp(-x)
        return 1 / denom
    def update_weights(self):
        for token in self.weights.keys():
            val = 0
            error_sum = 0
            for file_data in self.file_data:
                tokens = file_data["token"]
                true_value = file_data["class"]
                if token in tokens:
                    temp = true_value - file_data["error"]
                    error_sum += temp
                    val += tokens[token] * temp
            self.weights[token] += ((val * self.learning_rate) - (self.learning_rate * self.lambda_value * self.weights[token]))
    def test(self):
        ham_folder = os.listdir(self.test_ham)
        ham_correct = 0
        for file in ham_folder:
            ham_dict = {}
            value = 0
            file_path = os.path.join(self.test_ham, file)
            self.count_words(file_path, ham_dict)
            for token in ham_dict:
                if token in self.weights:
                    value += self.weights[token] * ham_dict[token]
            result = self.sigmoid(value)
            if result > 0.5:
                ham_correct += 1
        ham_accuracy = (ham_correct / len(ham_folder)) * 100
        print("Ham accuracy is ", ham_accuracy)
        spam_folder = os.listdir(self.test_spam)
        spam_correct = 0
        for file in spam_folder:
            spam_dict = {}
            value = 0
            file_path = os.path.join(self.test_spam, file)
            self.count_words(file_path, spam_dict)
            for token in spam_dict:
                if token in self.weights:
                    value += self.weights[token] * spam_dict[token]
            result = self.sigmoid(value)
            if result < 0.5:
                spam_correct += 1
        spam_accuracy = (spam_correct / len(spam_folder)) * 100
        print("Spam accuracy is ", spam_accuracy)
        total_accuracy = ((spam_correct + ham_correct) / (len(ham_folder) + len(spam_folder))) * 100
        print("Total accuracy is ", total_accuracy)
if __name__ == "__main__":
    train_ham_folder = "train_ham_folder_path"
    train_spam_folder = "train_spam_folder_path"
    test_ham_folder = "test_ham_folder_path"
    test_spam_folder = "test_spam_folder_path"
    model = LogisticRegression(train_ham_folder, train_spam_folder, test_ham_folder, test_spam_folder)
    model.run()
    model.train()
    model.test()