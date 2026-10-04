
import numpy as np
class NaiveBayes:
    def __init__(self, alpha=None):
        self.alpha = alpha
        self.classifier_data = None
    def train(self, train_data, alpha_range=None, plot_validation=False):
        if self.alpha is None:
            self._validate(train_data, plot_validation, alpha_range)
            print(f'Validated alpha value = {self.alpha}')
        word_dict = {}
        for label, sentence in train_data:
            dict_index = 0 if label == 'neg' else 1
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
        neg_prob = pos_prob = 1
        for word in document:
            if word in self.classifier_data:
                pos_prob *= self._calculate_word_prob(word, 1)
                neg_prob *= self._calculate_word_prob(word, 0)
        return 'neg' if neg_prob > pos_prob else 'pos'
    def evaluate(self, test_data):
        test_labels = [label for label, _ in test_data]
        predictions = [self.classify(doc) for _, doc in test_data]
        correct_count = sum(1 for true, pred in zip(test_labels, predictions) if true == pred)
        incorrect_indices = [(i, true, pred) for i, (true, pred) in enumerate(zip(test_labels, predictions)) if true != pred]
        return correct_count / len(test_labels), incorrect_indices
    def print_top_words(self, n_highest):
        neg_sorted = self._sort_words_by_prob(0)
        pos_sorted = self._sort_words_by_prob(1)
        self._print_top_words('positive', pos_sorted, n_highest)
        self._print_top_words('negative', neg_sorted, n_highest)
        return neg_sorted, pos_sorted
    def _validate(self, train_data, plot_validation, alpha_range=None):
        if self.alpha is not None:
            raise ValueError("Alpha value is already defined. Set it to None to change it.")
        if alpha_range is None:
            alpha_range = range(20)
        val_alpha_accs = []
        val_train = train_data[int(len(train_data) * 0.2):]
        val_test = train_data[:int(len(train_data) * 0.2)]
        for alpha in alpha_range:
            self.alpha = alpha
            self.train(val_train)
            acc, _ = self._evaluate_validation(val_test)
            val_alpha_accs.append((alpha, acc))
        if plot_validation:
            self._plot_validation(val_alpha_accs)
        self.alpha = max(val_alpha_accs, key=lambda x: x[1])[0]
        return self.alpha
    def _evaluate_validation(self, test_data):
        test_labels = [label for label, _ in test_data]
        predictions = [self.classify(doc) for _, doc in test_data]
        correct_count = sum(1 for true, pred in zip(test_labels, predictions) if true == pred)
        incorrect_indices = [(i, true, pred) for i, (true, pred) in enumerate(zip(test_labels, predictions)) if true != pred]
        return correct_count / len(test_labels), incorrect_indices
    def _calculate_word_prob(self, word, label_index):
        total_count = sum(self.classifier_data[word])
        return self.classifier_data[word][label_index] / total_count
    def _sort_words_by_prob(self, label_index):
        return sorted(
            [(word, self._calculate_word_prob(word, label_index)) for word in self.classifier_data],
            key=lambda x: x[1],
            reverse=True
        )
    def _print_top_words(self, label, sorted_words, n_highest):
        print(f'Top {n_highest} indicative words of {label} reviews:')
        for i in range(n_highest):
            word, prob = sorted_words[i]
            print(f'{i + 1}. "{word}" with probability {prob}')
        print('---')
    def _plot_validation(self, val_alpha_accs):
        import matplotlib.pyplot as plt
        plt.bar(*zip(*val_alpha_accs))
        plt.ylabel('Validation Accuracy')
        plt.xlabel('Alpha Value')
        plt.title('Validation Accuracy for Alpha Value Selection')
        plt.xticks(np.arange(0, 20, 1.0))
        plt.savefig('alpha_validation_accuracies.png')
        plt.show()