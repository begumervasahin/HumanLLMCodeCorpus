
import numpy as np
class class1:
    def fonk1(self, b1 = None):
        self.b1 = b1
        self.b2 = None
    def fonk2(self, train_data, b3 = None, plot_validation=False):
        if self.b1 is None:
            self.fonk6(train_data, plot_validation, b3 = b3)
            print(f'validated b4 = {self.b1}')
        b5 = {}
        for b6, sentence in train_data:
            a1 = 0
            if b6 = = 'pos':
                a1 = 1
            for word in sentence:
                if word in b5:
                    b5[word][a1] += 1
                elif a1 = = 1:
                    b5[word] = [self.b1,self.b1+1]
                else:
                    b5[word] = [self.b1+1,self.b1]
        self.b2 = b5
        return b5
    def fonk3(self, document):
        a2 = 1
        a3 = 1
        for word in document:
            if word not in self.b2:
                pass
            else:
                b7 = self.b2[word][1]/(self.b2[word][0]+self.b2[word][1])
                b8 = self.b2[word][0]/(self.b2[word][0]+self.b2[word][1])
                a3 *= b7
                a2 *= b8
        if a2 > a3:
            return 'neg'
        else:
            return 'pos'
    def fonk4(self, test_data):
        b9 = [b6 for b6, document in test_data]
        b10 = []
        a4 = 0
        for b6, document in test_data:
            b11 = self.fonk3(document)
            b10.append(b11)
        a5 = 0
        b12 = []
        for b13, predicted in zip(b9, b10):
            if b13 = = predicted:
                a4+=1
            else:
                b12.append((a5, b13, predicted))
            a5+=1
        return a4/len(b9), b12
    def fonk5(self, n_highest):
        b14 = sorted([(k,(v[0]/(v[0]+v[1]))) for k,v in self.b2.items()], key=lambda x: x[1], reverse=True)
        b15 = sorted([(k,v[1]/(v[0]+v[1])) for k,v in self.b2.items()], key=lambda x: x[1], reverse=True)
        print(f'Top {n_highest} indicative words of postive reviews:')
        for i in range(n_highest):
            print(f'{i+1}. "{b15[i][0]}" with probability {b15[i][1]}')
        print('---')
        print(f'Top {n_highest} indicative words of negative reviews: ')
        for i in range(n_highest):
            print(f'{i+1}. "{b14[i][0]}" with probability {b14[i][1]}')
        return b14, b15
    def fonk6(self, train_data, plot_validation, b3 = None):
        if self.b1 != None:
            raise Exception('the models b1 value is already defined, if you wish to change it, set it to none')
        if b3 is None:
            b3 = [i for i in range(20)]
        b16 = []
        for b1 in b3:
            b17 = train_data[int(len(train_data)*0.2):]
            b18 = train_data[:int(len(train_data)*0.2)]
            self.b1 = b1
            b2 = self.fonk2(b17)
            self.b2 = b2
            acc, b12 = self.fonk7(b2, b18)
            b16.append((b1, acc))
        if plot_validation:
            import matplotlib.pyplot as plt
            plt.bar(*zip(*b16))
            plt.ylabel('validation accuracy')
            plt.xlabel('b4')
            plt.title('validation accuracy for b4 selection')
            plt.xticks(np.arange(0,20,1.0))
            plt.savefig('alpha_validation_accuracies.png')
            plt.show()
        self.b1 = max(b16, key=lambda x: x[1])[0]
        return self.b1
    def fonk7(self, b2, test_data):
        b9 = [b6 for b6, document in test_data]
        b10 = []
        a4 = 0
        for b6, document in test_data:
            b11 = self.fonk3(document)
            b10.append(b11)
        a5 = 0
        b12 = []
        for b13, predicted in zip(b9, b10):
            if b13 = = predicted:
                a4+=1
            else:
                b12.append((a5, b13, predicted))
            a5+=1
        return a4/len(b9), b12