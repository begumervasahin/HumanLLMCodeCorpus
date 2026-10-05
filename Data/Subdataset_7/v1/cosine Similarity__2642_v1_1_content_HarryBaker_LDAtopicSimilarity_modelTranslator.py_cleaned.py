import gensim
import numpy as np
import sympy
from operator import itemgetter
import math
from gensim import matutils
class class1:
    def fonk1(self, b1, b2):
        self.b1 = b1
        self.b2 = b2
        self.b3 = self.b1.id2word
        self.b4 = self.b2.id2word
        self.b5 = len(self.b3)
        self.b6 = dict(self.b3)
        for b19, value in self.b4.items():
            if value in self.b3.values():
                self.b6[b19] = value
            elif value not in self.b3.values():
                self.b6[self.b5] = value
                self.b5 += 1
    def fonk2(self, topic1, topic2):
        b7 = []
        b8 = []
        b9 = sorted(self.b1.get_topic_terms(topic1, topn=self.b1.num_terms))
        b10 = sorted(self.b2.get_topic_terms(topic2, topn=self.b2.num_terms))
        for b19, value in self.b6.items():
            if value in self.b3.values():
                b7.append((b19, b9[b19][1]))
            else:
                b7.append((b19, 0))
            for key1, b11 in self.b4.items():
                if b11 = = value:
                    b8.append((b19, b10[key1][1]))
                    break
            else:
                b8.append((b19, 0))
        return self.fonk5(b7, b8, "Constant")
    def fonk3(self, b13, topic):
        b12 = []
        if b13 = = "Model1":
            for x in range(50):
                print(f"Topic {x}")
                b14 = self.fonk2(topic, x)
                b15 = (b14, x, self.b2.show_topic(x), self.b1.show_topic(topic))
                b12.append(b15)
        elif b13 = = "Model2":
            for x in range(50):
                print(f"Topic {x}")
                b14 = self.fonk2(topic, x)
                b15 = (b14, x, self.b1.show_topic(x), self.b2.show_topic(topic))
                b12.append(b15)
        b12 = sorted(b12, b19=itemgetter(0), reverse=True)
        return b12
    def fonk4(self, b13, topic):
        return
    def fonk5(self, top1, top2, b19):
        b16 = self.fonk6(top1, self.b1, b19)
        b17 = self.fonk6(top2, self.b2, b19)
        b18 = np.sqrt(0.5 * ((np.sqrt(b16) - np.sqrt(b17))**2).sum())
        return b18
    def fonk6(self, vector, b13, b19):
        if b19 = = "Constant":
            return self.fonk7(vector, b13)
        elif b19 = = "Dynamic":
            return self.fonk8(vector, b13)
    def fonk7(self, sparse_vector, b13):
        b20 = sorted(sparse_vector, b19=itemgetter(1), reverse=True)
        b20 = [item[0] for item in b20[:15]]
        b21 = matutils.sparse2full(sparse_vector, self.b5)
        for x in range(len(b21)):
            if x not in b20:
                b21[x] = 0
        return b21
    def fonk8(self, sparse_vector, b13):
        b20 = sorted(sparse_vector, b19=itemgetter(1), reverse=True)
        a1 = 0
        b11 = b20[0][1]
        b11 = math.floor(b11 * (10 ** 7)) / (10 ** 7)
        b22 = [b20[0][0]]
        for item in b20[1:]:
            b23 = item[1]
            b23 = math.floor(b23 * (10 ** 7)) / (10 ** 7)
            b24 = b11 - b23
            if b24 = = 0:
                a1 += 1
                b22.append(item[0])
                if a1 = = 5:
                    break
            else:
                a1 = 0
                b22.append(item[0])
            b11 = b23
        b21 = matutils.sparse2full(sparse_vector, self.b5)
        for i, a2 in enumerate(b21):
            if i not in b22:
                a2 = 0
        return b21
b1 = gensim.models.LdaModel.load('model1_path')
b2 = gensim.models.LdaModel.load('model2_path')
b25 = class1(b1, b2)
b26 = b25.fonk3("Model1", topic=0)
print(b26)