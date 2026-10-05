import os
import re
import io
import math
class NaiveBayesClassifier:
    def __init__(self, training_ham_path, training_spam_path, test_ham_path, test_spam_path):
        self.training_ham_path = training_ham_path
        self.training_spam_path = training_spam_path
        self.test_ham_path = test_ham_path
        self.test_spam_path = test_spam_path
        self.categories = ['HAM', 'SPAM']
        self.word_counts = {'HAM': {}, 'SPAM': {}}
        self.total_words = {'HAM': 0, 'SPAM': 0}
        self.vocab = set()
        self.prior_probabilities = {}
        self.conditional_probabilities = {}
        self.stop_words = set([
            "a", "about", "above", "after", "again", "against", "all", "am",
            "an", "and", "any", "are", "as", "at", "be", "because", "been",
            "before", "being", "below", "between", "both", "but", "by",
            "could", "did", "do", "does", "doing", "down", "during", "each",
            "few", "for", "from", "further", "had", "has", "have", "having",
            "he", "her", "here", "hers", "him", "himself", "his", "how",
            "i", "if", "in", "into", "is", "it", "its", "itself", "me",
            "more", "most", "my", "myself", "no", "nor", "not", "of", "off",
            "on", "once", "only", "or", "other", "our", "ours", "ourselves",
            "out", "over", "own", "same", "she", "should", "so", "some", "such",
            "than", "that", "the", "their", "theirs", "them", "themselves",
            "then", "there", "these", "they", "this", "those", "through", "to",
            "too", "under", "until", "up", "very", "was", "we", "were", "what",
            "when", "where", "which", "while", "who", "whom", "why", "with",
            "you", "your", "yours", "yourself", "yourselves"
        ])
    def preprocess_text(self, text):
        letters_only_text = re.sub("[^a-zA-Z\s]", "", text).lower()
        words = letters_only_text.split()
        words = [word for word in words if word not in self.stop_words]
        return words
    def train(self):
        for category in self.categories:
            path = self.training_ham_path if category == 'HAM' else self.training_spam_path
            files = os.listdir(path)
            for file_name in files:
                with io.open(os.path.join(path, file_name), 'r', encoding='iso-8859-1') as file:
                    words = self.preprocess_text(file.read())
                    for word in words:
                        if word not in self.vocab:
                            self.vocab.add(word)
                        if word in self.word_counts[category]:
                            self.word_counts[category][word] += 1
                        else:
                            self.word_counts[category][word] = 1
                        self.total_words[category] += 1
        total_files = sum(len(os.listdir(path)) for path in [self.training_ham_path, self.training_spam_path])
        for category in self.categories:
            path = self.training_ham_path if category == 'HAM' else self.training_spam_path
            self.prior_probabilities[category] = len(os.listdir(path)) / total_files
        vocab_size = len(self.vocab)
        for word in self.vocab:
            self.conditional_probabilities[word] = {}
            for category in self.categories:
                word_count = self.word_counts[category].get(word, 0)
                self.conditional_probabilities[word][category] = (word_count + 1) / (self.total_words[category] + vocab_size)
    def classify(self, text):
        words = set(self.preprocess_text(text))
        scores = {}
        for category in self.categories:
            scores[category] = math.log(self.prior_probabilities[category], 2)
            for word in words:
                if word in self.vocab:
                    scores[category] += math.log(self.conditional_probabilities[word][category], 2)
        return 'HAM' if scores['HAM'] > scores['SPAM'] else 'SPAM'
    def test(self):
        results = {}
        for category in ['HAM', 'SPAM']:
            path = self.test_ham_path if category == 'HAM' else self.test_spam_path
            correct = 0
            files = os.listdir(path)
            for file_name in files:
                with io.open(os.path.join(path, file_name), 'r', encoding='iso-8859-1') as file:
                    classification = self.classify(file.read())
                    if classification == category:
                        correct += 1
            accuracy = correct / len(files) * 100
            results[category] = accuracy
            print(f"{category} test accuracy: {accuracy:.2f}%")
        total_accuracy = sum(results.values()) / 2
        print(f"Total test accuracy: {total_accuracy:.2f}%")
if __name__ == "__main__":
    classifier = NaiveBayesClassifier("path/to/training/ham", "path/to/training/spam", "path/to/test/ham", "path/to/test/spam")
    classifier.train()
    classifier.test()