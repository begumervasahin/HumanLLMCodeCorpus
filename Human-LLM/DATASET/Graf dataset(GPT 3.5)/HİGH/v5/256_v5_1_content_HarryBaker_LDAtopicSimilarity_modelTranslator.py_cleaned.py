import gensim
import numpy as np
from operator import itemgetter
import math
class class1:
    def fonk1(self, b1, b2):
        self.b1 = b1
        self.b2 = b2
        self.b3 = self.b1.id2word
        self.b4 = self.b2.id2word
        self.b5 = len(self.b3)
        self.b6 = dict(self.b3)
        self.fonk2()
    def fonk2(self):
        for b16, value in self.b4.items():
            if value not in self.b3.values():
                self.b6[self.b5] = value
                self.b5 += 1
    def fonk3(self, topic1, topic2):
        b7 = self.fonk4(topic1, self.b1)
        b8 = self.fonk4(topic2, self.b2)
        return self.fonk7(b7, b8, "Constant")
    def fonk4(self, topic, model):
        b9 = []
        b10 = sorted(model.get_topic_terms(topic, topn=model.num_terms))
        for b16, value in self.b6.items():
            if value in self.b3.values():
                b9.append((b16, b10[b16][1]))
            else:
                b9.append((b16, 0))
        return b9
    def fonk5(self, model_name, topic):
        b11 = []
        b12 = self.b1.b12 if model_name == "Model1" else self.b2.b12
        b13 = self.b2 if model_name == "Model1" else self.b1
        for x in range(b12):
            print(f"Topic {x}")
            b14 = self.fonk3(topic, x)
            b15 = (b14, x, b13.show_topic(x), self.b1.show_topic(topic) if model_name == "Model1" else self.b2.show_topic(topic))
            b11.append(b15)
        b11.sort(b16 = itemgetter(0), reverse=True)
        return b11
    def fonk6(self, model, topic):
        return
    def fonk7(self, top1, top2, b16):
        b17 = self.fonk8(top1, self.b1, b16)
        b18 = self.fonk8(top2, self.b2, b16)
        b19 = np.sqrt(0.5 * ((np.sqrt(b17) - np.sqrt(b18))**2).sum())
        return b19
    def fonk8(self, vector, model, b16):
        if b16 = = "Constant":
            return self.fonk9(vector, model)
        elif b16 = = "Dynamic":
            return self.fonk10(vector, model)
    def fonk9(self, sparse_vector, model):
        b20 = sorted(sparse_vector, b16=itemgetter(1), reverse=True)[:15]
        b21 = [item[0] for item in b20]
        b22 = gensim.matutils.sparse2full(sparse_vector, self.b5)
        b22[~np.isin(np.arange(self.b5), b21)] = 0
        return b22
    def fonk10(self, sparse_vector, model):
        b20 = sorted(sparse_vector, b16=itemgetter(1), reverse=True)
        b23 = [b20[0][0]]
        a1 = 0
        for item in b20[1:]:
            b24 = math.floor(item[1] * (10 ** 7)) / (10 ** 7)
            b25 = math.floor((b20[0][1] - b24) * (10 ** 7)) / (10 ** 7)
            if b25 = = 0:
                a1 += 1
                b23.append(item[0])
                if a1 = = 5:
                    break
            else:
                a1 = 0
                b23.append(item[0])
        b22 = gensim.matutils.sparse2full(sparse_vector, self.b5)
        b22[~np.isin(np.arange(self.b5), b23)] = 0
        return b22