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
        for b19, value in self.b4.items():
            if value in self.b3.values():
                self.b6[b19] = value
            elif value not in self.b3.values():
                self.b6[self.b5] = value
                self.b5 += 1
    def fonk2(self, topic1, topic2):
        b7 = self.fonk3(topic1, self.b1)
        b8 = self.fonk3(topic2, self.b2)
        return self.fonk6(b7, b8, "Constant")
    def fonk3(self, topic, model):
        b9 = []
        b10 = sorted(model.get_topic_terms(topic, topn=model.num_terms))
        for b19, value in self.b6.items():
            if value in self.b3.values():
                b9.append((b19, b10[b19][1]))
            else:
                b9.append((b19, 0))
        return b9
    def fonk4(self, model_name, topic):
        b11 = []
        b12 = self.b1.b12 if model_name == "Model1" else self.b2.b12
        b13 = self.b2 if model_name == "Model1" else self.b1
        for x in range(b12):
            print(f"Topic {x}")
            b14 = self.fonk2(topic, x)
            b15 = (b14, x, b13.show_topic(x), self.b1.show_topic(topic) if model_name == "Model1" else self.b2.show_topic(topic))
            b11.append(b15)
        b11 = sorted(b11, b19=itemgetter(0), reverse=True)
        return b11
    def fonk5(self, model, topic):
        return
    def fonk6(self, top1, top2, b19):
        b16 = self.fonk7(top1, self.b1, b19)
        b17 = self.fonk7(top2, self.b2, b19)
        b18 = np.sqrt(0.5 * ((np.sqrt(b16) - np.sqrt(b17))**2).sum())
        return b18
    def fonk7(self, vector, model, b19):
        if b19 = = "Constant":
            return self.fonk8(vector, model)
        elif b19 = = "Dynamic":
            return self.fonk9(vector, model)
    def fonk8(self, sparse_vector, model):
        b20 = sorted(sparse_vector, b19=itemgetter(1), reverse=True)
        b20 = [item[0] for item in b20[:15]]
        b21 = gensim.matutils.sparse2full(sparse_vector, self.b5)
        for x in range(len(b21)):
            if x not in b20:
                b21[x] = 0
        return b21
    def fonk9(self, sparse_vector, model):
        b20 = sorted(sparse_vector, b19=itemgetter(1), reverse=True)
        a1 = 0
        b22 = b20[0][1]
        b22 = math.floor(b22 * (10 ** 7)) / (10 ** 7)
        b23 = [b20[0][0]]
        for item in b20[1:]:
            b24 = item[1]
            b24 = math.floor(b24 * (10 ** 7)) / (10 ** 7)
            b25 = b22 - b24
            if b25 = = 0:
                a1 += 1
                b23.append(item[0])
                if a1 = = 5:
                    break
            else:
                a1 = 0
                b23.append(item[0])
            b22 = b24
        b21 = gensim.matutils.sparse2full(sparse_vector, self.b5)
        for i, a2 in enumerate(b21):
            if i not in b23:
                a2 = 0
        return b21