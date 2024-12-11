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
            if word in self.b2:
                b6 = self.b2[word][1] / (self.b2[word][0] + self.b2[word][1])
                b7 = self.b2[word][0] / (self.b2[word][0] + self.b2[word][1])
                a2 *= b6
                a1 *= b7
        if a1 > a2:
            return 'neg'
        else:
            return 'pos'
    def fonk4(self, test_data):
        b8 = [label for label, document in test_data]
        b9 = []
        a3 = 0
        for label, document in test_data:
            b10 = self.fonk3(document)
            b9.append(b10)
        b11 = [(i, correct, predicted) for i, (correct, predicted) in enumerate(zip(b8, b9)) if correct != predicted]
        a3 = len(test_data) - len(b11)
        b12 = a3 / len(test_data)
        return b12, b11
    def fonk5(self, n_highest):
        b13 = sorted([(k, (v[0] / (v[0] + v[1]))) for k, v in self.b2.items()], key=lambda x: x[1], reverse=True)
        b14 = sorted([(k, v[1] / (v[0] + v[1])) for k, v in self.b2.items()], key=lambda x: x[1], reverse=True)
        print(f'Top {n_highest} indicative words of positive reviews:')
        for i in range(n_highest):
            print(f'{i + 1}. "{b14[i][0]}" with probability {b14[i][1]}')
        print('---')
        print(f'Top {n_highest} indicative words of negative reviews:')
        for i in range(n_highest):
            print(f'{i + 1}. "{b13[i][0]}" with probability {b13[i][1]}')
        return b13, b14
    def fonk6(self, train_data, plot_validation, b3 = None):
        if self.b1 is not None:
            raise Exception('The model\'s b1 value is already defined. If you wish to change it, set it to None.')
        if b3 is None:
            b3 = list(range(20))
        b15 = []
        for b1 in b3:
            b16 = train_data[int(len(train_data) * 0.2):]
            b17 = train_data[:int(len(train_data) * 0.2)]
            self.b1 = b1
            b2 = self.fonk2(b16)
            self.b2 = b2
            acc, b18 = self.fonk7(b2, b17)
            b15.append((b1, acc))
        if plot_validation:
            plt.bar(*zip(*b15))
            plt.ylabel('Validation Accuracy')
            plt.xlabel('Alpha Value')
            plt.title('Validation Accuracy for Alpha Value Selection')
            plt.xticks(np.arange(0, 20, 1.0))
            plt.savefig('alpha_validation_accuracies.png')
            plt.show()
        self.b1 = max(b15, key=lambda x: x[1])[0]
        return self.b1
    def fonk7(self, b2, test_data):
        b8 = [label for label, document in test_data]
        b9 = []
        a3 = 0
        for label, document in test_data:
            b10 = self.fonk3(document)
            b9.append(b10)
        b11 = [(i, correct, predicted) for i, (correct, predicted) in enumerate(zip(b8, b9)) if correct != predicted]
        a3 = len(test_data) - len(b11)
        b12 = a3 / len(test_data)
        return b12, b11