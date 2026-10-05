import os
import re
import io
import math
class NaiveBayesClassifier:
    def __init__(self, training_ham_path, training_spam_path, test_ham_path, test_spam_path):
        self.training_paths = {'HAM': training_ham_path, 'SPAM': training_spam_path}
        self.test_paths = {'HAM': test_ham_path, 'SPAM': test_spam_path}
        self.word_counts = {'HAM': {}, 'SPAM': {}}
        self.total_words = {'HAM': 0, 'SPAM': 0}
        self.vocab = set()
        self.prior_probabilities = {}
        self.conditional_probabilities = {}
        self._init_stop_words()
    def _init_stop_words(self):
        self.stop_words = set([
        ])
    def _preprocess_text(self, text):
        cleaned_text = re.sub("[^a-zA-Z\s]", "", text).lower()
        words = cleaned_text.split()
        return [word for word in words if word not in self.stop_words]
    def train(self):
        for category, path in self.training_paths.items():
            for filename in os.listdir(path):
                with io.open(os.path.join(path, filename), 'r', encoding='iso-8859-1') as file:
                    words = self._preprocess_text(file.read())
                    for word in words:
                        self.vocab.add(word)
                        self.word_counts[category][word] = self.word_counts[category].get(word, 0) + 1
                        self.total_words[category] += 1
        self._calculate_prior_probabilities()
        self._calculate_conditional_probabilities()
    def _calculate_prior_probabilities(self):
        total_files = sum(len(os.listdir(path)) for path in self.training_paths.values())
        for category, path in self.training_paths.items():
            self.prior_probabilities[category] = len(os.listdir(path)) / total_files
    def _calculate_conditional_probabilities(self):
        vocab_size = len(self.vocab)
        for word in self.vocab:
            self.conditional_probabilities[word] = {}
            for category in self.training_paths.keys():
                word_count = self.word_counts[category].get(word, 0)
                self.conditional_probabilities[word][category] = (word_count + 1) / (self.total_words[category] + vocab_size)
    def classify(self, text):
        words = set(self._preprocess_text(text))
        scores = {category: math.log(self.prior_probabilities[category], 2) for category in self.training_paths.keys()}
        for word in words:
            if word in self.vocab:
                for category in self.training_paths.keys():
                    scores[category] += math.log(self.conditional_probabilities[word][category], 2)
        return max(scores, key=scores.get)
    def test(self):
        for category, path in self.test_paths.items():
            correct_predictions = sum(1 for filename in os.listdir(path)
                                      if self.classify(io.open(os.path.join(path, filename), 'r', encoding='iso-8859-1').read()) == category)
            accuracy = correct_predictions / len(os.listdir(path)) * 100
            print(f"{category} test accuracy: {accuracy:.2f}%")
