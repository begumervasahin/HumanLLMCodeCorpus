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
        self.vocabulary = set()
        self.learning_rate = 0.0001
        self.lambda_value = 5
        self.file_data = []
    def run(self):
        self.create_vocabulary()
        self.process_folders()
    def count_words(self, path):
        word_count = {}
        with io.open(path, 'r', encoding='iso-8859-1') as f:
            for line in f:
                letters_only = re.sub("[^a-zA-Z0-9\s]", "", line.lower()).split()
                for word in letters_only:
                    word_count[word] = word_count.get(word, 0) + 1
        return word_count
    def create_vocabulary(self):
        for folder in [self.train_ham, self.train_spam]:
            for file in os.listdir(folder):
                file_path = os.path.join(folder, file)
                word_count = self.count_words(file_path)
                self.vocabulary.update(word_count.keys())
        self.weights = {word: 0.0 for word in self.vocabulary}
    def process_folders(self):
        for folder, classification in [(self.train_ham, 1.0), (self.train_spam, 0.0)]:
            for file in os.listdir(folder):
                file_path = os.path.join(folder, file)
                word_count = self.count_words(file_path)
                self.file_data.append({'file_name': file_path, 'token': word_count, 'class': classification})
    def train(self):
        for _ in range(500):
            self.update_error()
            self.update_weights()
    def update_error(self):
        for data in self.file_data:
            token = data["token"]
            value = 1
            for word, count in token.items():
                value += count * self.weights[word]
            data["error"] = self.sigmoid(value)
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))
    def update_weights(self):
        for word in self.weights:
            val = sum((data["class"] - data["error"]) * token.get(word, 0) for data in self.file_data)
            self.weights[word] += (val * self.learning_rate) - (self.learning_rate * self.lambda_value * self.weights[word])
    def test(self):
        ham_correct = sum(self.classify_file(os.path.join(self.test_ham, file)) > 0.5 for file in os.listdir(self.test_ham))
        spam_correct = sum(self.classify_file(os.path.join(self.test_spam, file)) < 0.5 for file in os.listdir(self.test_spam))
        ham_accuracy = (ham_correct / len(os.listdir(self.test_ham))) * 100
        spam_accuracy = (spam_correct / len(os.listdir(self.test_spam))) * 100
        total_accuracy = ((ham_correct + spam_correct) / (len(os.listdir(self.test_ham)) + len(os.listdir(self.test_spam)))) * 100
        print("Ham accuracy is ", ham_accuracy)
        print("Spam accuracy is ", spam_accuracy)
        print("Total accuracy is ", total_accuracy)
    def classify_file(self, file_path):
        word_count = self.count_words(file_path)
        value = sum(self.weights[word] * count for word, count in word_count.items() if word in self.weights)
        return self.sigmoid(value)
if __name__ == "__main__":
    train_ham_folder = "train_ham_folder_path"
    train_spam_folder = "train_spam_folder_path"
    test_ham_folder = "test_ham_folder_path"
    test_spam_folder = "test_spam_folder_path"
    model = LogisticRegression(train_ham_folder, train_spam_folder, test_ham_folder, test_spam_folder)
    model.run()
    model.train()
    model.test()