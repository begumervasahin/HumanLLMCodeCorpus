import os
import re
import io
import math
class NaiveBayes:
    def __init__(self, training_ham, training_spam, test_ham, test_spam):
        self.training_ham = training_ham
        self.training_spam = training_spam
        self.test_ham = test_ham
        self.test_spam = test_spam
        self.HAM = 0
        self.SPAM = 1
        self.total_word_list = []
        self.ham_word_count = {}
        self.total_ham_word_count = 0
        self.spam_word_count = {}
        self.total_spam_word_count = 0
        self.prior_prob = {}
        self.total_conditional_prob = {}
    def _count_words(self, directory, word_count_dict):
        files = os.listdir(directory)
        total_word_count = 0
        for filename in files:
            with io.open(os.path.join(directory, filename), 'r', encoding='iso-8859-1') as file:
                lines = file.readlines()
                for line in lines:
                    words = re.findall(r'\b\w+\b', line.lower())
                    for word in words:
                        word_count_dict[word] = word_count_dict.get(word, 0) + 1
                        total_word_count += 1
        return total_word_count
    def _calculate_conditional_probabilities(self):
        for word in self.total_word_list:
            ham_count = self.ham_word_count.get(word, 0) + 1
            spam_count = self.spam_word_count.get(word, 0) + 1
            self.total_conditional_prob[word] = [
                ham_count / (self.total_ham_word_count + len(self.total_word_list)),
                spam_count / (self.total_spam_word_count + len(self.total_word_list))
            ]
    def train(self):
        total_ham_files = len(os.listdir(self.training_ham))
        total_spam_files = len(os.listdir(self.training_spam))
        total_training_files = total_ham_files + total_spam_files
        self.prior_prob[self.HAM] = total_ham_files / total_training_files
        self.prior_prob[self.SPAM] = total_spam_files / total_training_files
        self.total_ham_word_count = self._count_words(self.training_ham, self.ham_word_count)
        self.total_spam_word_count = self._count_words(self.training_spam, self.spam_word_count)
        self.total_word_list = list(set(self.ham_word_count.keys()) | set(self.spam_word_count.keys()))
        self._calculate_conditional_probabilities()
    def _classify_documents(self, directory):
        correct_count = 0
        total_files = 0
        actual_class = self.HAM if directory == self.test_ham else self.SPAM
        files = os.listdir(directory)
        for filename in files:
            with io.open(os.path.join(directory, filename), 'r', encoding='iso-8859-1') as file:
                content = file.read().lower()
                words = re.findall(r'\b\w+\b', content)
                score = {self.HAM: math.log(self.prior_prob[self.HAM], 2),
                         self.SPAM: math.log(self.prior_prob[self.SPAM], 2)}
                for word in words:
                    if word in self.total_word_list:
                        score[self.HAM] += math.log(self.total_conditional_prob[word][self.HAM], 2)
                        score[self.SPAM] += math.log(self.total_conditional_prob[word][self.SPAM], 2)
                predicted_class = max(score, key=score.get)
                if predicted_class == actual_class:
                    correct_count += 1
                total_files += 1
        return correct_count, total_files
    def test(self):
        ham_correct, ham_total = self._classify_documents(self.test_ham)
        spam_correct, spam_total = self._classify_documents(self.test_spam)
        ham_accuracy = (ham_correct / ham_total) * 100 if ham_total != 0 else 0
        spam_accuracy = (spam_correct / spam_total) * 100 if spam_total != 0 else 0
        total_accuracy = ((ham_correct + spam_correct) / (ham_total + spam_total)) * 100 if (ham_total + spam_total) != 0 else 0
        print("Ham test accuracy =", ham_accuracy)
        print("Spam test accuracy =", spam_accuracy)
        print("Total test accuracy =", total_accuracy)
if __name__ == "__main__":
    training_ham = "path_to_training_ham_folder"
    training_spam = "path_to_training_spam_folder"
    test_ham = "path_to_test_ham_folder"
    test_spam = "path_to_test_spam_folder"
    classifier = NaiveBayes(training_ham, training_spam, test_ham, test_spam)
    classifier.train()
    classifier.test()