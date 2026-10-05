import LRHelper as helper
import Mail as m
import os
import math
import sys
class LogisticRegression:
    def __init__(self, learning_rate, penalty):
        self.training_set = {}
        self.test_set = {}
        self.vocab_set = set()
        self.learning_rate = float(learning_rate)
        self.penalty = float(penalty)
        self.weight_vector = {}
    def extract_vocab(self):
        for key, mail in self.training_set.items():
            for word in mail.words:
                self.vocab_set.add(word)
    def initialize_weights(self):
        for word in self.vocab_set:
            self.weight_vector[word] = 0.0
    def train(self, iterations):
        for _ in range(int(iterations)):
            for word in self.weight_vector:
                gradient = 0.0
                for mail in self.training_set.values():
                    y_label = 1 if mail.is_spam else 0
                    if word in mail.words:
                        gradient += mail.word_freq[word] * (y_label - self.calculate_conditional_probability(1, mail))
                self.weight_vector[word] += (self.learning_rate * gradient) - (self.learning_rate * self.penalty * self.weight_vector[word])
    def calculate_conditional_probability(self, class_num, mail):
        sum_value = 0.0
        for key, value in mail.word_freq.items():
            if key not in self.weight_vector:
                self.weight_vector[key] = 0.0
            sum_value += self.weight_vector[key] * value
        if class_num == 1:
            return math.exp(sum_value) / (1 + math.exp(sum_value))
        elif class_num == 0:
            return 1 / (1 + math.exp(sum_value))
    def classify_mail(self, mail):
        score = {0: self.calculate_conditional_probability(0, mail), 1: self.calculate_conditional_probability(1, mail)}
        return 0 if score[0] > score[1] else 1
    def evaluate_accuracy(self):
        correct_predictions = 0
        for mail in self.test_set.values():
            if self.classify_mail(mail) == mail.is_spam:
                correct_predictions += 1
        accuracy = (correct_predictions / len(self.test_set)) * 100
        print("Accuracy: {:.2f}%".format(accuracy))
    def load_data(self, directory_path, is_spam):
        files = os.listdir(directory_path)
        for file in files:
            file_path = os.path.join(directory_path, file)
            with open(file_path, encoding='utf-8', errors="ignore") as mail_file:
                words = helper.get_words(mail_file.read())
                word_freq = helper.get_word_freq(words)
                self.test_set[file] = m.Mail(words, word_freq, is_spam)
    def load_data_without_stopwords(self, directory_path, is_spam, stop_path):
        stop_words = helper.read_stop_words(stop_path)
        files = os.listdir(directory_path)
        for file in files:
            file_path = os.path.join(directory_path, file)
            with open(file_path, encoding='utf-8', errors="ignore") as mail_file:
                words = helper.get_words_without_stopwords(mail_file.read(), stop_words)
                word_freq = helper.get_word_freq(words)
                self.test_set[file] = m.Mail(words, word_freq, is_spam)
def main():
    if len(sys.argv) != 9:
        print("Usage: python script.py spam_training_path ham_training_path spam_test_path ham_test_path learning_rate penalty iterations_threshold stop_path")
        return
    lr = LogisticRegression(sys.argv[5], sys.argv[6])
    spam_training_path = sys.argv[1]
    ham_training_path = sys.argv[2]
    spam_test_path = sys.argv[3]
    ham_test_path = sys.argv[4]
    lr.load_data(spam_training_path, 1)
    lr.load_data(ham_training_path, 0)
    lr.load_data(spam_test_path, 1)
    lr.load_data(ham_test_path, 0)
    lr.extract_vocab()
    lr.initialize_weights()
    lr.train(sys.argv[7])
    print("Accuracy without removing stopwords:")
    lr.evaluate_accuracy()
    lr2 = LogisticRegression(sys.argv[5], sys.argv[6])
    lr2.load_data_without_stopwords(spam_training_path, 1, sys.argv[8])
    lr2.load_data_without_stopwords(ham_training_path, 0, sys.argv[8])
    lr2.load_data_without_stopwords(spam_test_path, 1, sys.argv[8])
    lr2.load_data_without_stopwords(ham_test_path, 0, sys.argv[8])
    lr2.extract_vocab()
    lr2.initialize_weights()
    lr2.train(sys.argv[7])
    print("Accuracy after removing stopwords:")
    lr2.evaluate_accuracy()
if __name__ == "__main__":
    main()