import numpy as np
class NaiveBayes:
    def __init__(self, alpha=None):
        self.alpha = alpha
        self.classifier_data = None
    def train(self, train_data, alpha_range=None, plot_validation=False):
        if self.alpha is None:
            self._validate(train_data, plot_validation, alpha_range=alpha_range)
            print(f'Validated alpha value: {self.alpha}')
        word_dict = {}
        for label, sentence in train_data:
            dict_index = 1 if label == 'pos' else 0
            for word in sentence:
                if word in word_dict:
                    word_dict[word][dict_index] += 1
                else:
                    if dict_index == 1:
                        word_dict[word] = [self.alpha, self.alpha + 1]
                    else:
                        word_dict[word] = [self.alpha + 1, self.alpha]
        self.classifier_data = word_dict
        return word_dict
    def classify(self, document):
        neg_prob, pos_prob = 1, 1
        for word in document:
            if word in self.classifier_data:
                pos_word_prob = self.classifier_data[word][1] / (self.classifier_data[word][0] + self.classifier_data[word][1])
                neg_word_prob = self.classifier_data[word][0] / (self.classifier_data[word][0] + self.classifier_data[word][1])
                pos_prob *= pos_word_prob
                neg_prob *= neg_word_prob
        return 'pos' if pos_prob > neg_prob else 'neg'
    def evaluate(self, test_data):
        test_labels = [label for label, _ in test_data]
        test_labels_predicted = [self.classify(document) for _, document in test_data]
        correct_count = sum(1 for true, pred in zip(test_labels, test_labels_predicted) if true == pred)
        incorrect_indices = [(i, true, pred) for i, (true, pred) in enumerate(zip(test_labels, test_labels_predicted)) if true != pred]
        accuracy = correct_count / len(test_labels)
        return accuracy, incorrect_indices
    def print_top_words(self, n_highest):
        neg_sorted = sorted([(k, v[0] / (v[0] + v[1])) for k, v in self.classifier_data.items()], key=lambda x: x[1], reverse=True)
        pos_sorted = sorted([(k, v[1] / (v[0] + v[1])) for k, v in self.classifier_data.items()], key=lambda x: x[1], reverse=True)
        print(f'Top {n_highest} indicative words of positive reviews:')
        for i, (word, prob) in enumerate(pos_sorted[:n_highest]):
            print(f'{i + 1}. "{word}" with probability {prob}')
        print('---')
        print(f'Top {n_highest} indicative words of negative reviews:')
        for i, (word, prob) in enumerate(neg_sorted[:n_highest]):
            print(f'{i + 1}. "{word}" with probability {prob}')
        return neg_sorted, pos_sorted
    def _validate(self, train_data, plot_validation, alpha_range=None):
        if self.alpha is not None:
            raise Exception('The model\'s alpha value is already defined. If you wish to change it, set it to None.')
        if alpha_range is None:
            alpha_range = range(20)
        val_alpha_accs = []
        for alpha in alpha_range:
            val_train = train_data[int(len(train_data) * 0.2):]
            val_test = train_data[:int(len(train_data) * 0.2)]
            self.alpha = alpha
            self.classifier_data = self.train(val_train)
            acc, _ = self._validation_eval(self.classifier_data, val_test)
            val_alpha_accs.append((alpha, acc))
        if plot_validation:
            import matplotlib.pyplot as plt
            plt.bar(*zip(*val_alpha_accs))
            plt.ylabel('Validation Accuracy')
            plt.xlabel('Alpha Value')
            plt.title('Validation Accuracy for Alpha Value Selection')
            plt.xticks(np.arange(0, 20, 1.0))
            plt.savefig('alpha_validation_accuracies.png')
            plt.show()
        self.alpha = max(val_alpha_accs, key=lambda x: x[1])[0]
        return self.alpha
    def _validation_eval(self, classifier_data, test_data):
        test_labels = [label for label, _ in test_data]
        test_labels_predicted = [self.classify(document) for _, document in test_data]
        correct_count = sum(1 for true, pred in zip(test_labels, test_labels_predicted) if true == pred)
        incorrect_indices = [(i, true, pred) for i, (true, pred) in enumerate(zip(test_labels, test_labels_predicted)) if true != pred]
        accuracy = correct_count / len(test_labels)
        return accuracy, incorrect_indices
if __name__ == "__main__":
    train_data = [('pos', 'I love this movie'.split()), ('neg', 'I hate this movie'.split()), ('pos', 'This film is great'.split()), ('neg', 'This film is terrible'.split())]
    test_data = [('pos', 'I love this film'.split()), ('neg', 'I hate this film'.split())]
    nb = NaiveBayes(alpha=1)
    nb.train(train_data)
    accuracy, incorrect_indices = nb.evaluate(test_data)
    print(f'Accuracy: {accuracy}')
    print(f'Incorrect Indices: {incorrect_indices}')
    nb.print_top_words(3)