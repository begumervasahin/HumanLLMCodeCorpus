import numpy as np
import matplotlib.pyplot as plt
class class1:
    def fonk1(self, b1 = None):
        self.b1 = b1
        self.b2 = None
    def fonk2(self, train_data, b3 = None, plot_validation=False):
        if self.b1 is None:
            self.b1 = self.fonk6(train_data, b3, plot_validation)
            print(f'Validated b1 value: {self.b1}')
        b4 = self.fonk7(train_data)
        self.b2 = b4
        return b4
    def fonk3(self, document):
        a1 = 1
        a2 = 1
        for word in document:
            if word not in self.b2:
                continue
            a2 *= self.b2[word][1] / sum(self.b2[word])
            a1 *= self.b2[word][0] / sum(self.b2[word])
        return 'neg' if a1 > a2 else 'pos'
    def fonk4(self, test_data):
        b5 = [label for label, b12 in test_data]
        b6 = [self.fonk3(document) for b12, document in test_data]
        b7 = sum(1 for true_label, pred_label in zip(b5, b6) if true_label == pred_label)
        return b7 / len(b5), [(i, true_label, pred_label) for i, (true_label, pred_label) in enumerate(zip(b5, b6)) if true_label != pred_label]
    def fonk5(self, n_highest):
        b15, b8 = self.fonk8()
        self.fonk9(n_highest, b8, 'positive')
        print('---')
        self.fonk9(n_highest, b15, 'negative')
        return b15, b8
    def fonk6(self, train_data, b3, plot_validation):
        if self.b1 is not None:
            raise ValueError("The model's b1 value is already defined. If you wish to change it, set it to None.")
        if b3 is None:
            b3 = range(20)
        b9 = []
        for b1 in b3:
            b10 = train_data[int(len(train_data) * 0.2):]
            b11 = train_data[:int(len(train_data) * 0.2)]
            self.b1 = b1
            b2 = self.fonk2(b10)
            self.b2 = b2
            acc, b12 = self.fonk10(b11)
            b9.append((b1, acc))
        if plot_validation:
            self.fonk11(b9)
        return max(b9, b13 = lambda x: x[1])[0]
    def fonk7(self, train_data):
        b4 = {}
        for label, sentence in train_data:
            b14 = 0 if label == 'pos' else 1
            for word in sentence:
                if word in b4:
                    b4[word][b14] += 1
                elif b14 = = 1:
                    b4[word] = [self.b1, self.b1 + 1]
                else:
                    b4[word] = [self.b1 + 1, self.b1]
        return b4
    def fonk8(self):
        b15 = sorted([(k, (v[0] / (v[0] + v[1]))) for k, v in self.b2.items()], b13=lambda x: x[1], reverse=True)
        b8 = sorted([(k, v[1] / (v[0] + v[1])) for k, v in self.b2.items()], b13=lambda x: x[1], reverse=True)
        return b15, b8
    def fonk9(self, n_highest, word_list, label):
        print(f'Top {n_highest} indicative words of {label} reviews:')
        for i, (word, prob) in enumerate(word_list[:n_highest], b16 = 1):
            print(f'{i}. "{word}" with probability {prob}')
    def fonk10(self, test_data):
        b5 = [label for label, b12 in test_data]
        b6 = [self.fonk3(document) for b12, document in test_data]
        b7 = sum(1 for true_label, pred_label in zip(b5, b6) if true_label == pred_label)
        return b7 / len(b5), [(i, true_label, pred_label) for i, (true_label, pred_label) in enumerate(zip(b5, b6)) if true_label != pred_label]
    def fonk11(self, b9):
        plt.bar(*zip(*b9))
        plt.ylabel('Validation Accuracy')
        plt.xlabel('Alpha Value')
        plt.title('Validation Accuracy for Alpha Value Selection')
        plt.xticks(np.arange(0, 20, 1.0))
        plt.savefig('alpha_validation_accuracies.png')
        plt.show()