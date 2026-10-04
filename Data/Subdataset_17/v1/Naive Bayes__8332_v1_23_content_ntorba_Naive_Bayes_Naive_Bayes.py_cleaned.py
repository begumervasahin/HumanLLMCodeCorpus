import numpy as np
class Naive_Bayes:
    def __init__(self, alpha=None):
        self.alpha = alpha
        self.classifier_data = None
    def train_nb(self, train_data, alpha_range=None, plot_validation=False):
        if self.alpha is None:
            self.validate__(train_data, plot_validation, alpha_range=alpha_range)
            print(f'validated alpha_val = {self.alpha}')
        word_dict = {}
        for label, sentence in train_data:
            dict_index = 0
            if label == 'pos':
                dict_index = 1
            for word in sentence:
                if word in word_dict:
                    word_dict[word][dict_index] += 1
                elif dict_index == 1:
                    word_dict[word] = [self.alpha, self.alpha + 1]
                else:
                    word_dict[word] = [self.alpha + 1, self.alpha]
        self.classifier_data = word_dict
        return word_dict
    def classify_nb(self, document):
        neg_prob = 1
        pos_prob = 1
        for word in document:
            if word not in self.classifier_data:
                continue
            else:
                i_pos_prob = self.classifier_data[word][1] / (self.classifier_data[word][0] + self.classifier_data[word][1])
                i_neg_prob = self.classifier_data[word][0] / (self.classifier_data[word][0] + self.classifier_data[word][1])
                pos_prob *= i_pos_prob
                neg_prob *= i_neg_prob
        if neg_prob > pos_prob:
            return 'neg'
        else:
            return 'pos'
    def evaluate_nb(self, test_data):
        test_labels = [label for label, document in test_data]
        test_labels_predicted = []
        correct_count = 0
        for label, document in test_data:
            predicted_label = self.classify_nb(document)
            test_labels_predicted.append(predicted_label)
        incorrect_indices = []
        for index, (correct, predicted) in enumerate(zip(test_labels, test_labels_predicted)):
            if correct == predicted:
                correct_count += 1
            else:
                incorrect_indices.append((index, correct, predicted))
        return correct_count / len(test_labels), incorrect_indices
    def print_top_nb(self, n_highest):
        neg_sorted = sorted([(k, (v[0] / (v[0] + v[1]))) for k, v in self.classifier_data.items()], key=lambda x: x[1], reverse=True)
        pos_sorted = sorted([(k, v[1] / (v[0] + v[1])) for k, v in self.classifier_data.items()], key=lambda x: x[1], reverse=True)
        print(f'Top {n_highest} indicative words of positive reviews:')
        for i in range(n_highest):
            print(f'{i + 1}. "{pos_sorted[i][0]}" with probability {pos_sorted[i][1]}')
        print('---')
        print(f'Top {n_highest} indicative words of negative reviews: ')
        for i in range(n_highest):
            print(f'{i + 1}. "{neg_sorted[i][0]}" with probability {neg_sorted[i][1]}')
        return neg_sorted, pos_sorted
    def validate__(self, train_data, plot_validation, alpha_range=None):
        if self.alpha is not None:
            raise Exception('The model\'s alpha value is already defined, if you wish to change it, set it to None.')
        if alpha_range is None:
            alpha_range = [i for i in range(20)]
        val_alpha_accs = []
        for alpha in alpha_range:
            val_train = train_data[int(len(train_data) * 0.2):]
            val_test = train_data[:int(len(train_data) * 0.2)]
            self.alpha = alpha
            classifier_data = self.train_nb(val_train)
            self.classifier_data = classifier_data
            acc, incorrect_indices = self.validation_eval__(classifier_data, val_test)
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
    def validation_eval__(self, classifier_data, test_data):
        test_labels = [label for label, document in test_data]
        test_labels_predicted = []
        correct_count = 0
        for label, document in test_data:
            predicted_label = self.classify_nb(document)
            test_labels_predicted.append(predicted_label)
        incorrect_indices = []
        for index, (correct, predicted) in enumerate(zip(test_labels, test_labels_predicted)):
            if correct == predicted:
                correct_count += 1
            else:
                incorrect_indices.append((index, correct, predicted))
        return correct_count / len(test_labels), incorrect_indices
if __name__ == "__main__":
    train_data = [('pos', 'I love this movie'.split()), ('neg', 'I hate this movie'.split()), ('pos', 'This film is great'.split()), ('neg', 'This film is terrible'.split())]
    test_data = [('pos', 'I love this film'.split()), ('neg', 'I hate this film'.split())]
    nb = Naive_Bayes(alpha=1)
    nb.train_nb(train_data)
    accuracy, incorrect_indices = nb.evaluate_nb(test_data)
    print(f'Accuracy: {accuracy}')
    print(f'Incorrect Indices: {incorrect_indices}')
    nb.print_top_nb(3)