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
        b4 = {}
        for label, sentence in train_data:
            b5 = 0 if label == 'pos' else 1
            for word in sentence:
                if word in b4:
                    b4[word][b5] += 1
                elif b5 = = 1:
                    b4[word] = [self.b1, self.b1 + 1]
                else:
                    b4[word] = [self.b1 + 1, self.b1]
        self.b2 = b4
        return b4
    def fonk3(self, document):
        a1 = 1
        a2 = 1
        for word in document:
            if word not in self.b2:
                continue
            b6 = self.b2[word][1] / sum(self.b2[word])
            b7 = self.b2[word][0] / sum(self.b2[word])
            a2 *= b6
            a1 *= b7
        return 'neg' if a1 > a2 else 'pos'
    def fonk4(self, test_data):
        b8 = [label for label, document in test_data]
        b9 = [self.fonk3(document) for label, document in test_data]
        b10 = sum(1 for true_label, pred_label in zip(b8, b9) if true_label == pred_label)
        return b10 / len(b8), [(i, true_label, pred_label) for i, (true_label, pred_label) in enumerate(zip(b8, b9)) if true_label != pred_label]
    def fonk5(self, n_highest):
        b11 = sorted([(k, (v[0] / (v[0] + v[1]))) for k, v in self.b2.items()], b18=lambda x: x[1], reverse=True)
        b12 = sorted([(k, v[1] / (v[0] + v[1])) for k, v in self.b2.items()], b18=lambda x: x[1], reverse=True)
        print(f'Top {n_highest} indicative words of positive reviews:')
        for i, (word, prob) in enumerate(b12[:n_highest], b13 = 1):
            print(f'{i}. "{word}" with probability {prob}')
        print('---')
        print(f'Top {n_highest} indicative words of negative reviews: ')
        for i, (word, prob) in enumerate(b11[:n_highest], b13 = 1):
            print(f'{i}. "{word}" with probability {prob}')
        return b11, b12
    def fonk6(self, train_data, b3, plot_validation):
        if self.b1 is not None:
            raise ValueError("The model's b1 value is already defined. If you wish to change it, set it to None.")
        if b3 is None:
            b3 = range(20)
        b14 = []
        for b1 in b3:
            b15 = train_data[int(len(train_data) * 0.2):]
            b16 = train_data[:int(len(train_data) * 0.2)]
            self.b1 = b1
            b2 = self.fonk2(b15)
            self.b2 = b2
            acc, b17 = self.fonk7(b16)
            b14.append((b1, acc))
        if plot_validation:
            plt.bar(*zip(*b14))
            plt.ylabel('Validation Accuracy')
            plt.xlabel('Alpha Value')
            plt.title('Validation Accuracy for Alpha Value Selection')
            plt.xticks(np.arange(0, 20, 1.0))
            plt.savefig('alpha_validation_accuracies.png')
            plt.show()
        return max(b14, b18 = lambda x: x[1])[0]
    def fonk7(self, test_data):
        b8 = [label for label, document in test_data]
        b9 = [self.fonk3(document) for label, document in test_data]
        b10 = sum(1 for true_label, pred_label in zip(b8, b9) if true_label == pred_label)
        return b10 / len(b8), [(i, true_label, pred_label) for i, (true_label, pred_label) in enumerate(zip(b8, b9)) if true_label != pred_label]