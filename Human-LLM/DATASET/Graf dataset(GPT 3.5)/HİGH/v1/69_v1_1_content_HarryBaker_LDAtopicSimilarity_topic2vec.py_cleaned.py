import gensim
import numpy as np
import random
from gensim.corpora import Dictionary
from gensim import models
class class1:
    def fonk1(self, b1, b2, flag, b3, b4, b5, b6):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
        self.b5 = b5
        self.b6 = b6
        self.b7 = []
        self.b8 = Dictionary.load('/path/to/b8')
        self.b9 = self.b8.token2id
        if flag:
            print("Starting variation")
            print(f"There are {len(self.b1)} b1")
            self.fonk2(self.b1)
            random.shuffle(self.b7)
            self.b10 = models.Word2Vec(self.b7, b4=self.b4, b5=self.b5, min_count=self.b6, workers=2)
            self.b10.save(self.b3)
            random.shuffle(self.b1)
            self.b11 = models.Word2Vec(self.b1, b4=self.b4, b5=self.b5, min_count=3, workers=2)
            self.b11.save(self.b3 + "_w2v")
        self.b10 = models.Word2Vec.load(self.b3)
        self.b12 = [self.b2.show_topic(x) for x in range(50)]
        self.b13 = [self.b10.b24(positive=["u" + str(x)]) for x in range(50)]
        print(self.b3 + " is finished")
    def fonk2(self, b1):
        for sentence in b1:
            b14 = self.fonk3(sentence)
            self.b7.append(b14)
    def fonk3(self, sentence):
        b15 = []
        for index, b23 in enumerate(sentence):
            b16 = self.fonk4(b23, index, sentence)
            b15.append(b16)
        return b15
    def fonk4(self, b23, index, sentence):
        b14 = list(sentence)
        if b23 in self.b9:
            b17 = self.b8.doc2bow([b23])
            b18 = self.b2[b17]
            b19 = b18[-1][0]
            b14[index] = "u" + str(b19)
        return b14
    def fonk5(self, b23):
        b20 = (0, 0)
        if b23 in self.b9:
            for x in range(50):
                b21 = self.b10.similarity("u" + b23, "u" + str(x))
                if b21 > b20[0]:
                    b20 = (b21, "u" + str(x))
        else:
            print(f"Word {b23} not in b8")
        return b20
b1 = [['apple', 'banana', 'orange'], ['dog', 'cat', 'horse'], ['tree', 'flower', 'grass']]
b2 = gensim.models.ldamodel.LdaModel()
b22 = class1(b1, b2, True, 'topic2vec_model', 100, 5, 1)
b23 = 'apple'
b24 = b22.fonk5(b23)
print(f"Most similar b18 to '{b23}': {b24[1]} with similarity b20 {b24[0]}")