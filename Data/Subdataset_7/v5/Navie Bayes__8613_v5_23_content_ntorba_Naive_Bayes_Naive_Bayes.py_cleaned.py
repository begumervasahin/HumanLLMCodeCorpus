import numpy as np
import matplotlib.pyplot as plt
class class1:
    def fonk1(self, b1 = None):
        self.b1 = b1
        self.b2 = None
    def fonk2(self, train_data, b3 = None, plot_validation=False):
        if self.b1 is None:
            self.fonk6(train_data, plot_validation, b3 = b3)
            print(f'Validated b1 value: {self.b1}')
        b4 = self.fonk7(train_data)
        self.b2 = b4
        return b4
    def fonk3(self, document):
        neg_prob, b5 = 1, 1
        for word in document:
            if word in self.b2:
                neg_prob *= self.b2[word][0] / sum(self.b2[word])
                b5 *= self.b2[word][1] / sum(self.b2[word])
        return 'neg' if neg_prob > b5 else 'pos'
    def fonk4(self, test_data):
        b6 = [label for label, b16 in test_data]
        b7 = [self.fonk3(document) for b16, document in test_data]
        b8 = [(i, correct, predicted) for i, (correct, predicted) in enumerate(zip(b6, b7)) if correct != predicted]
        b9 = len(test_data) - len(b8)
        b10 = b9 / len(test_data)
        return b10, b8
    def fonk5(self, n_highest):
        b11 = sorted([(k, v[0] / sum(v)) for k, v in self.b2.items()], key=lambda x: x[1], reverse=True)
        b12 = sorted([(k, v[1] / sum(v)) for k, v in self.b2.items()], key=lambda x: x[1], reverse=True)
        self.fonk10('positive', b12, n_highest)
        self.fonk10('negative', b11, n_highest)
        return b11, b12
    def fonk6(self, train_data, plot_validation, b3 = None):
        if self.b1 is not None:
            raise Exception('The model\'s b1 value is already defined. If you wish to change it, set it to None.')
        if b3 is None:
            b3 = list(range(20))
        b13 = []
        for b1 in b3:
            b14 = train_data[int(len(train_data) * 0.2):]
            b15 = train_data[:int(len(train_data) * 0.2)]
            self.b1 = b1
            b2 = self.fonk2(b14)
            self.b2 = b2
            acc, b16 = self.fonk8(b2, b15)
            b13.append((b1, acc))
        if plot_validation:
            self.fonk9(b13)
        self.b1 = max(b13, key=lambda x: x[1])[0]
        return self.b1
    def fonk7(self, train_data):
        b4 = {}
        for label, sentence in train_data:
            for word in sentence:
                if word in b4:
                    b4[word][label] += 1
                else:
                    b4[word] = { 'pos': self.b1 + 1, 'neg': self.b1 + 1 }
                    b4[word][label] += 1
        return b4
    def fonk8(self, b2, test_data):
        b6 = [label for label, b16 in test_data]
        b7 = [self.fonk3(document) for b16, document in test_data]
        b8 = [(i, correct, predicted) for i, (correct, predicted) in enumerate(zip(b6, b7)) if correct != predicted]
        b9 = len(test_data) - len(b8)
        b10 = b9 / len(test_data)
        return b10, b8
    def fonk9(self, b13):
        alpha_values, b17 = zip(*b13)
        plt.bar(alpha_values, b17)
        plt.ylabel('Validation Accuracy')
        plt.xlabel('Alpha Value')
        plt.title('Validation Accuracy for Alpha Value Selection')
        plt.xticks(np.arange(0, 20, 1.0))
        plt.savefig('alpha_validation_accuracies.png')
        plt.show()
    def fonk10(self, sentiment, sorted_words, n_highest):
        print(f'Top {n_highest} indicative words of {sentiment} reviews:')
        for i, (word, prob) in enumerate(sorted_words[:n_highest], b18 = 1):
            print(f'{i}. "{word}" with probability {prob}')
        print('---')