
import numpy as np
class class1:
    def fonk1(self, b1 = None):
        self.b1 = b1
        self.b2 = None
    def fonk2(self, train_data, b3 = None, plot_validation=False):
        if self.b1 is None:
            self.fonk6(train_data, plot_validation, b3)
            print(f'Validated b1 b4 = {self.b1}')
        b5 = {}
        for label, sentence in train_data:
            b6 = 0 if label == 'neg' else 1
            for word in sentence:
                if word in b5:
                    b5[word][b6] += 1
                elif b6 = = 1:
                    b5[word] = [self.b1, self.b1 + 1]
                else:
                    b5[word] = [self.b1 + 1, self.b1]
        self.b2 = b5
        return b5
    def fonk3(self, document):
        b7 = pos_prob = 1
        for word in document:
            if word in self.b2:
                pos_prob *= self.fonk8(word, 1)
                b7 *= self.fonk8(word, 0)
        return 'neg' if b7 > pos_prob else 'pos'
    def fonk4(self, test_data):
        b8 = [label for label, b17 in test_data]
        b9 = [self.fonk3(doc) for b17, doc in test_data]
        b10 = sum(1 for true, pred in zip(b8, b9) if true == pred)
        b11 = [(i, true, pred) for i, (true, pred) in enumerate(zip(b8, b9)) if true != pred]
        return b10 / len(b8), b11
    def fonk5(self, n_highest):
        b12 = self.fonk9(0)
        b13 = self.fonk9(1)
        self.fonk10('positive', b13, n_highest)
        self.fonk10('negative', b12, n_highest)
        return b12, b13
    def fonk6(self, train_data, plot_validation, b3 = None):
        if self.b1 is not None:
            raise ValueError("Alpha b4 is already defined. Set it to None to change it.")
        if b3 is None:
            b3 = range(20)
        b14 = []
        b15 = train_data[int(len(train_data) * 0.2):]
        b16 = train_data[:int(len(train_data) * 0.2)]
        for b1 in b3:
            self.b1 = b1
            self.fonk2(b15)
            acc, b17 = self.fonk7(b16)
            b14.append((b1, acc))
        if plot_validation:
            self.fonk11(b14)
        self.b1 = max(b14, b19=lambda x: x[1])[0]
        return self.b1
    def fonk7(self, test_data):
        b8 = [label for label, b17 in test_data]
        b9 = [self.fonk3(doc) for b17, doc in test_data]
        b10 = sum(1 for true, pred in zip(b8, b9) if true == pred)
        b11 = [(i, true, pred) for i, (true, pred) in enumerate(zip(b8, b9)) if true != pred]
        return b10 / len(b8), b11
    def fonk8(self, word, label_index):
        b18 = sum(self.b2[word])
        return self.b2[word][label_index] / b18
    def fonk9(self, label_index):
        return sorted(
            [(word, self.fonk8(word, label_index)) for word in self.b2],
            b19 = lambda x: x[1],
            b20 = True
        )
    def fonk10(self, label, sorted_words, n_highest):
        print(f'Top {n_highest} indicative words of {label} reviews:')
        for i in range(n_highest):
            word, b21 = sorted_words[i]
            print(f'{i + 1}. "{word}" with probability {b21}')
        print('---')
    def fonk11(self, b14):
        import matplotlib.pyplot as plt
        plt.bar(*zip(*b14))
        plt.ylabel('Validation Accuracy')
        plt.xlabel('Alpha Value')
        plt.title('Validation Accuracy for Alpha Value Selection')
        plt.xticks(np.arange(0, 20, 1.0))
        plt.savefig('alpha_validation_accuracies.png')
        plt.show()