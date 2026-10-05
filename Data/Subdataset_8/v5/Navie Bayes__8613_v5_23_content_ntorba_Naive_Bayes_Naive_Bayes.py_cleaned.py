import numpy as np
import matplotlib.pyplot as plt
class NaiveBayesClassifier:
    def __init__(self, alpha=None):
        self.alpha = alpha
        self.classifier_data = None
    def train(self, train_data, alpha_range=None, plot_validation=False):
        if self.alpha is None:
            self.validate_alpha(train_data, plot_validation, alpha_range=alpha_range)
            print(f'Validated alpha value: {self.alpha}')
        word_dict = self.build_word_dictionary(train_data)
        self.classifier_data = word_dict
        return word_dict
    def classify(self, document):
        neg_prob, pos_prob = 1, 1
        for word in document:
            if word in self.classifier_data:
                neg_prob *= self.classifier_data[word][0] / sum(self.classifier_data[word])
                pos_prob *= self.classifier_data[word][1] / sum(self.classifier_data[word])
        return 'neg' if neg_prob > pos_prob else 'pos'
    def evaluate(self, test_data):
        test_labels = [label for label, _ in test_data]
        test_labels_predicted = [self.classify(document) for _, document in test_data]
        incorrect_indices = [(i, correct, predicted) for i, (correct, predicted) in enumerate(zip(test_labels, test_labels_predicted)) if correct != predicted]
        correct_count = len(test_data) - len(incorrect_indices)
        accuracy = correct_count / len(test_data)
        return accuracy, incorrect_indices
    def print_top_words(self, n_highest):
        neg_sorted = sorted([(k, v[0] / sum(v)) for k, v in self.classifier_data.items()], key=lambda x: x[1], reverse=True)
        pos_sorted = sorted([(k, v[1] / sum(v)) for k, v in self.classifier_data.items()], key=lambda x: x[1], reverse=True)
        self.print_top_indicative_words('positive', pos_sorted, n_highest)
        self.print_top_indicative_words('negative', neg_sorted, n_highest)
        return neg_sorted, pos_sorted
    def validate_alpha(self, train_data, plot_validation, alpha_range=None):
        if self.alpha is not None:
            raise Exception('The model\'s alpha value is already defined. If you wish to change it, set it to None.')
        if alpha_range is None:
            alpha_range = list(range(20))
        val_alpha_accs = []
        for alpha in alpha_range:
            val_train = train_data[int(len(train_data) * 0.2):]
            val_test = train_data[:int(len(train_data) * 0.2)]
            self.alpha = alpha
            classifier_data = self.train(val_train)
            self.classifier_data = classifier_data
            acc, _ = self.validation_eval(classifier_data, val_test)
            val_alpha_accs.append((alpha, acc))
        if plot_validation:
            self.plot_validation_accuracy(val_alpha_accs)
        self.alpha = max(val_alpha_accs, key=lambda x: x[1])[0]
        return self.alpha
    def build_word_dictionary(self, train_data):
        word_dict = {}
        for label, sentence in train_data:
            for word in sentence:
                if word in word_dict:
                    word_dict[word][label] += 1
                else:
                    word_dict[word] = { 'pos': self.alpha + 1, 'neg': self.alpha + 1 }
                    word_dict[word][label] += 1
        return word_dict
    def validation_eval(self, classifier_data, test_data):
        test_labels = [label for label, _ in test_data]
        test_labels_predicted = [self.classify(document) for _, document in test_data]
        incorrect_indices = [(i, correct, predicted) for i, (correct, predicted) in enumerate(zip(test_labels, test_labels_predicted)) if correct != predicted]
        correct_count = len(test_data) - len(incorrect_indices)
        accuracy = correct_count / len(test_data)
        return accuracy, incorrect_indices
    def plot_validation_accuracy(self, val_alpha_accs):
        alpha_values, accuracies = zip(*val_alpha_accs)
        plt.bar(alpha_values, accuracies)
        plt.ylabel('Validation Accuracy')
        plt.xlabel('Alpha Value')
        plt.title('Validation Accuracy for Alpha Value Selection')
        plt.xticks(np.arange(0, 20, 1.0))
        plt.savefig('alpha_validation_accuracies.png')
        plt.show()
    def print_top_indicative_words(self, sentiment, sorted_words, n_highest):
        print(f'Top {n_highest} indicative words of {sentiment} reviews:')
        for i, (word, prob) in enumerate(sorted_words[:n_highest], start=1):
            print(f'{i}. "{word}" with probability {prob}')
        print('---')