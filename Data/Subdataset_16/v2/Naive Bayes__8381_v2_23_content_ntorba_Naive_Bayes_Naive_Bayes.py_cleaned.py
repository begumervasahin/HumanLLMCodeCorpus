import numpy as np
class class1:
    def fonk1(self, b1 = None):
        self.b1 = b1
        self.b2 = None
    def fonk2(self, b21, b3 = None, plot_validation=False):
        if self.b1 is None:
            self.fonk6(b21, plot_validation, b3 = b3)
            print(f'Validated b1 value: {self.b1}')
        b4 = {}
        for label, sentence in b21:
            b5 = 1 if label == 'pos' else 0
            for word in sentence:
                if word in b4:
                    b4[word][b5] += 1
                else:
                    if b5 = = 1:
                        b4[word] = [self.b1, self.b1 + 1]
                    else:
                        b4[word] = [self.b1 + 1, self.b1]
        self.b2 = b4
        return b4
    def fonk3(self, document):
        neg_prob, b6 = 1, 1
        for word in document:
            if word in self.b2:
                b7 = self.b2[word][1] / (self.b2[word][0] + self.b2[word][1])
                b8 = self.b2[word][0] / (self.b2[word][0] + self.b2[word][1])
                b6 *= b7
                neg_prob *= b8
        return 'pos' if b6 > neg_prob else 'neg'
    def fonk4(self, b22):
        b9 = [label for label, b19 in b22]
        b10 = [self.fonk3(document) for b19, document in b22]
        b11 = sum(1 for true, pred in zip(b9, b10) if true == pred)
        b12 = [(i, true, pred) for i, (true, pred) in enumerate(zip(b9, b10)) if true != pred]
        b13 = b11 / len(b9)
        return b13, b12
    def fonk5(self, n_highest):
        b14 = sorted([(k, v[0] / (v[0] + v[1])) for k, v in self.b2.items()], key=lambda x: x[1], reverse=True)
        b15 = sorted([(k, v[1] / (v[0] + v[1])) for k, v in self.b2.items()], key=lambda x: x[1], reverse=True)
        print(f'Top {n_highest} indicative words of positive reviews:')
        for i, (word, prob) in enumerate(b15[:n_highest]):
            print(f'{i + 1}. "{word}" with probability {prob}')
        print('---')
        print(f'Top {n_highest} indicative words of negative reviews:')
        for i, (word, prob) in enumerate(b14[:n_highest]):
            print(f'{i + 1}. "{word}" with probability {prob}')
        return b14, b15
    def fonk6(self, b21, plot_validation, b3 = None):
        if self.b1 is not None:
            raise Exception('The model\'s b1 value is already defined. If you wish to change it, set it to None.')
        if b3 is None:
            b3 = range(20)
        b16 = []
        for b1 in b3:
            b17 = b21[int(len(b21) * 0.2):]
            b18 = b21[:int(len(b21) * 0.2)]
            self.b1 = b1
            self.b2 = self.fonk2(b17)
            acc, b19 = self.fonk7(self.b2, b18)
            b16.append((b1, acc))
        if plot_validation:
            import matplotlib.pyplot as plt
            plt.bar(*zip(*b16))
            plt.ylabel('Validation Accuracy')
            plt.xlabel('Alpha Value')
            plt.title('Validation Accuracy for Alpha Value Selection')
            plt.xticks(np.arange(0, 20, 1.0))
            plt.savefig('alpha_validation_accuracies.png')
            plt.show()
        self.b1 = max(b16, key=lambda x: x[1])[0]
        return self.b1
    def fonk7(self, b2, b22):
        b9 = [label for label, b19 in b22]
        b10 = [self.fonk3(document) for b19, document in b22]
        b11 = sum(1 for true, pred in zip(b9, b10) if true == pred)
        b12 = [(i, true, pred) for i, (true, pred) in enumerate(zip(b9, b10)) if true != pred]
        b13 = b11 / len(b9)
        return b13, b12
if b20 = = "__main__":
    b21 = [('pos', 'I love this movie'.split()), ('neg', 'I hate this movie'.split()), ('pos', 'This film is great'.split()), ('neg', 'This film is terrible'.split())]
    b22 = [('pos', 'I love this film'.split()), ('neg', 'I hate this film'.split())]
    b23 = class1(b1=1)
    b23.fonk2(b21)
    b13, b12 = b23.fonk4(b22)
    print(f'Accuracy: {b13}')
    print(f'Incorrect Indices: {b12}')
    b23.fonk5(3)