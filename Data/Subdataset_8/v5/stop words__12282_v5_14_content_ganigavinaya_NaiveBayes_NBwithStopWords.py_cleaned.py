import os
import re
import io
import math
class NaiveBayes:
    def __init__(self, training_ham, training_spam, test_ham, test_spam):
        self.training_ham = training_ham
        self.training_spam = training_spam
        self.HAM = 0
        self.SPAM = 1
        self.total_word_list = []
        self.ham_count_dict = {}
        self.total_ham_word_count = 0
        self.spam_count_dict = {}
        self.total_spam_word_count = 0
        self.prior = {}
        self.total_cond_prob = {}
        self.test_ham = test_ham
        self.test_spam = test_spam
        self.stop_words = ["a", "about", "above", "after", "again", "against", "all", "am",
                           "an", "and", "any", "are", "aren't", "as", "at", "be", "because", "been", "before",
                           "being", "below", "between", "both", "but", "by", "can't", "cannot", "could", "couldn't",
                           "did", "didn't", "do", "does", "doesn't", "doing", "don't", "down", "during", "each", "few",
                           "for", "from", "further", "had", "hadn't", "has", "hasn't", "have", "haven't", "having", "he",
                           "he'd", "he'll", "he", "her", "here", "here", "hers", "herself", "him", "himself", "his",
                           "how", "how's", "i", "i'd", "i'll", "i", "ie", "if", "in", "into", "is", "isn't", "it", "it",
                           "it's", "itself", "let", "me", "more", "most", "mustn't", "my", "myself", "no", "nor", "not",
                           "of", "off", "on", "once", "only", "or", "other", "ought", "our", "ours", "ourselves", "out",
                           "over", "own", "same", "shan't", "she", "she'd", "she'll", "she", "should", "shouldn't",
                           "so", "some", "such", "than", "that", "that", "the", "their", "theirs", "them", "themselves",
                           "then", "there", "there", "these", "they", "they'd", "they'll", "they're", "they've", "this",
                           "those", "through", "to", "too", "under", "until", "up", "very", "was", "wasn't", "we", "we'd",
                           "we'll", "were", "we", "we're", "weren't", "what", "what", "when", "when", "where",
                           "where", "which", "while", "who", "who", "whom", "why", "why", "with", "won't", "would",
                           "wouldn't", "you", "you'd", "you'll", "you're", "you've", "your", "yours", "yourself", "yourselves",
                           "nt", "d", "ll", "re", "ve", "r", "t", "nd", "s"]
    def get_word_count_list(self, flag):
        filepath = self.training_ham if flag == self.HAM else self.training_spam
        training_file_list = os.listdir(filepath)
        count_dict = {}
        total_word_count = 0
        for file_name in training_file_list:
            with io.open(os.path.join(filepath, file_name), 'r', encoding='iso-8859-1') as file:
                lines = file.readlines()
                for line in lines:
                    letters_only = re.sub("[^a-zA-Z\s]", "", line).lower().split()
                    for word in letters_only:
                        if word not in self.stop_words:
                            count_dict[word] = count_dict.get(word, 0) + 1
                            total_word_count += 1
        self.total_word_list = list(set(self.total_word_list + list(count_dict.keys())))
        if flag == self.HAM:
            self.ham_count_dict = count_dict
            self.total_ham_word_count += total_word_count
        else:
            self.spam_count_dict = count_dict
            self.total_spam_word_count += total_word_count
    def calculate_cond_prob(self):
        for word in self.total_word_list:
            ham_count = self.ham_count_dict.get(word, 0) + 1
            spam_count = self.spam_count_dict.get(word, 0) + 1
            self.total_cond_prob[word] = [(ham_count / self.total_ham_word_count), (spam_count / self.total_spam_word_count)]
    def run(self):
        self.get_word_count_list(self.HAM)
        self.get_word_count_list(self.SPAM)
    def train(self):
        total_ham_files = len(os.listdir(self.training_ham))
        total_spam_files = len(os.listdir(self.training_spam))
        total_training_files = total_ham_files + total_spam_files
        self.prior[self.HAM] = total_ham_files / total_training_files
        self.prior[self.SPAM] = total_spam_files / total_training_files
        self.calculate_cond_prob()
    def get_classification(self, path):
        correct_count = 0
        test_file_list = os.listdir(path)
        for file_name in test_file_list:
            with io.open(os.path.join(path, file_name), 'r', encoding='iso-8859-1') as file:
                file_data = file.read().lower()
                letters_only = re.sub("[^a-zA-Z\s]", "", file_data)
                word_list = set(letters_only.split())
                score = {self.HAM: math.log2(self.prior[self.HAM]), self.SPAM: math.log2(self.prior[self.SPAM])}
                for word in word_list:
                    if word in self.total_word_list:
                        score[self.HAM] += math.log2(self.total_cond_prob[word][self.HAM])
                        score[self.SPAM] += math.log2(self.total_cond_prob[word][self.SPAM])
                if score[self.HAM] > score[self.SPAM]:
                    if path == self.test_ham:
                        correct_count += 1
                else:
                    if path == self.test_spam:
                        correct_count += 1
        return correct_count
    def test(self):
        ham_test_result = self.get_classification(self.test_ham)
        ham_test_files = len(os.listdir(self.test_ham))
        ham_accuracy = (ham_test_result / ham_test_files) * 100
        print("Ham test accuracy = {:.2f}%".format(ham_accuracy))
        spam_test_result = self.get_classification(self.test_spam)
        spam_test_files = len(os.listdir(self.test_spam))
        spam_accuracy = (spam_test_result / spam_test_files) * 100
        print("Spam test accuracy = {:.2f}%".format(spam_accuracy))
        total_test_files = ham_test_files + spam_test_files
        total_correct = ham_test_result + spam_test_result
        total_accuracy = (total_correct / total_test_files) * 100
        print("Total test accuracy = {:.2f}%".format(total_accuracy))
if __name__ == "__main__":
    nb = NaiveBayes("path_to_training_ham", "path_to_training_spam", "path_to_test_ham", "path_to_test_spam")
    nb.run()
    nb.train()
    nb.test()