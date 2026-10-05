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
        word_dict = {}
        for label, sentence in train_data:
            dict_index = 0 if label == 'pos' else 1
            for word in sentence:
                if word in word_dict:
                    word_dict[word][dict_index] += 1
                elif dict_index == 1:
                    word_dict[word] = [self.alpha, self.alpha + 1]
                else:
                    word_dict[word] = [self.alpha + 1, self.alpha]
        self.classifier_data = word_dict
        return word_dict
    def classify(self, document):
        neg_prob = 1
        pos_prob = 1
        for word in document:
            if word in self.classifier_data:
                i_pos_prob = self.classifier_data[word][1] / (self.classifier_data[word][0] + self.classifier_data[word][1])
                i_neg_prob = self.classifier_data[word][0] / (self.classifier_data[word][0] + self.classifier_data[word][1])
                pos_prob *= i_pos_prob
                neg_prob *= i_neg_prob
        if neg_prob > pos_prob:
            return 'neg'
        else:
            return 'pos'
    def evaluate(self, test_data):
        test_labels = [label for label, document in test_data]
        test_labels_predicted = []
        correct_count = 0
        for label, document in test_data:
            predicted_label = self.classify(document)
            test_labels_predicted.append(predicted_label)
        incorrect_indices = [(i, correct, predicted) for i, (correct, predicted) in enumerate(zip(test_labels, test_labels_predicted)) if correct != predicted]
        correct_count = len(test_data) - len(incorrect_indices)
        accuracy = correct_count / len(test_data)
        return accuracy, incorrect_indices
    def print_top_words(self, n_highest):
        neg_sorted = sorted([(k, (v[0] / (v[0] + v[1]))) for k, v in self.classifier_data.items()], key=lambda x: x[1], reverse=True)
        pos_sorted = sorted([(k, v[1] / (v[0] + v[1])) for k, v in self.classifier_data.items()], key=lambda x: x[1], reverse=True)
        print(f'Top {n_highest} indicative words of positive reviews:')
        for i in range(n_highest):
            print(f'{i + 1}. "{pos_sorted[i][0]}" with probability {pos_sorted[i][1]}')
        print('---')
        print(f'Top {n_highest} indicative words of negative reviews:')
        for i in range(n_highest):
            print(f'{i + 1}. "{neg_sorted[i][0]}" with probability {neg_sorted[i][1]}')
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
            plt.bar(*zip(*val_alpha_accs))
            plt.ylabel('Validation Accuracy')
            plt.xlabel('Alpha Value')
            plt.title('Validation Accuracy for Alpha Value Selection')
            plt.xticks(np.arange(0, 20, 1.0))
            plt.savefig('alpha_validation_accuracies.png')
            plt.show()
        self.alpha = max(val_alpha_accs, key=lambda x: x[1])[0]
        return self.alpha
    def validation_eval(self, classifier_data, test_data):
        test_labels = [label for label, document in test_data]
        test_labels_predicted = []
        correct_count = 0
        for label, document in test_data:
            predicted_label = self.classify(document)
            test_labels_predicted.append(predicted_label)
        incorrect_indices = [(i, correct, predicted) for i, (correct, predicted) in enumerate(zip(test_labels, test_labels_predicted)) if correct != predicted]
        correct_count = len(test_data) - len(incorrect_indices)
        accuracy = correct_count / len(test_data)
        return accuracy, incorrect_indices