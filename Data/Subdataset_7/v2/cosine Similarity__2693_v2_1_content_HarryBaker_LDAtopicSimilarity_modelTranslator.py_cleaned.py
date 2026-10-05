import gensim
import numpy as np
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
        for b20, value in self.b4.items():
            if value in self.b3.values():
                self.b6[b20] = value
            elif value not in self.b3.values():
                self.b6[self.b5] = value
                self.b5 += 1
    def fonk2(self, topic1, topic2):
        b7 = []
        b8 = []
        b9 = sorted(self.b1.get_topic_terms(topic1, topn=self.b1.num_terms))
        b10 = sorted(self.b2.get_topic_terms(topic2, topn=self.b2.num_terms))
        for b20, value in self.b6.items():
            if value in self.b3.values():
                b7.append((b20, b9[b20][1]))
            else:
                b7.append((b20, 0))
            for key1, b11 in self.b4.items():
                if b11 = = value:
                    b8.append((b20, b10[key1][1]))
                    break
            else:
                b8.append((b20, 0))
        return self.fonk5(b7, b8, "Constant")
    def fonk3(self, model, topic):
        b12 = []
        b13 = self.b1.b13 if model == "Model1" else self.b2.b13
        b14 = self.b2 if model == "Model1" else self.b1
        for x in range(b13):
            print(f"Topic {x}")
            b15 = self.fonk2(topic, x)
            b16 = (b15, x, b14.show_topic(x), self.b1.show_topic(topic) if model == "Model1" else self.b2.show_topic(topic))
            b12.append(b16)
        b12 = sorted(b12, b20=itemgetter(0), reverse=True)
        return b12
    def fonk4(self, model, topic):
        return
    def fonk5(self, top1, top2, b20):
        b17 = self.fonk6(top1, self.b1, b20)
        b18 = self.fonk6(top2, self.b2, b20)
        b19 = np.sqrt(0.5 * ((np.sqrt(b17) - np.sqrt(b18))**2).sum())
        return b19
    def fonk6(self, vector, model, b20):
        if b20 = = "Constant":
            return self.fonk7(vector, model)
        elif b20 = = "Dynamic":
            return self.fonk8(vector, model)
    def fonk7(self, sparse_vector, model):
        b21 = sorted(sparse_vector, b20=itemgetter(1), reverse=True)
        b21 = [item[0] for item in b21[:15]]
        b22 = matutils.sparse2full(sparse_vector, self.b5)
        for x in range(len(b22)):
            if x not in b21:
                b22[x] = 0
        return b22
    def fonk8(self, sparse_vector, model):
        b21 = sorted(sparse_vector, b20=itemgetter(1), reverse=True)
        a1 = 0
        b11 = b21[0][1]
        b11 = math.floor(b11 * (10 ** 7)) / (10 ** 7)
        b23 = [b21[0][0]]
        for item in b21[1:]:
            b24 = item[1]
            b24 = math.floor(b24 * (10 ** 7)) / (10 ** 7)
            b25 = b11 - b24
            if b25 = = 0:
                a1 += 1
                b23.append(item[0])
                if a1 = = 5:
                    break
            else:
                a1 = 0
                b23.append(item[0])
            b11 = b24
        b22 = matutils.sparse2full(sparse_vector, self.b5)
        for i, a2 in enumerate(b22):
            if i not in b23:
                a2 = 0
        return b22
b1 = gensim.models.LdaModel.load('model1_path')
b2 = gensim.models.LdaModel.load('model2_path')
b26 = class1(b1, b2)
b27 = b26.fonk3("Model1", topic=0)
print(b27)