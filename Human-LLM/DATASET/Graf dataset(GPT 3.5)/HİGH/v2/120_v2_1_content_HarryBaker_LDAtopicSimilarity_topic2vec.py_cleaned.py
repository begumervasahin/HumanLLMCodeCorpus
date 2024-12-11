import gensim
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
        self.b8 = Dictionary.load('/path/to/dictionary').token2id
        if flag:
            self.fonk2()
            self.fonk5()
        self.b9 = models.Word2Vec.load(self.b3)
        self.b10 = [self.b2.show_topic(x) for x in range(50)]
        self.b11 = [self.b9.b23(positive=["u" + str(x)]) for x in range(50)]
        print(f"{self.b3} is finished")
    def fonk2(self):
        for sentence in self.b1:
            b12 = self.fonk3(sentence)
            self.b7.append(b12)
    def fonk3(self, sentence):
        b13 = []
        for index, b22 in enumerate(sentence):
            b14 = self.fonk4(b22)
            b13.append(b14)
        return b13
    def fonk4(self, b22):
        if b22 in self.b8:
            b15 = self.b2[self.b8[b22]]
            b16 = b15[-1][0] if b15 else ''
            return "u" + str(b16)
        return b22
    def fonk5(self):
        random.shuffle(self.b7)
        b17 = models.Word2Vec(self.b7, b4=self.b4, b5=self.b5, min_count=self.b6, workers=2)
        b17.save(self.b3)
        random.shuffle(self.b1)
        b18 = models.Word2Vec(self.b1, b4=self.b4, b5=self.b5, min_count=3, workers=2)
        b18.save(self.b3 + "_w2v")
    def fonk6(self, b22):
        if b22 in self.b8:
            b19 = [(self.b9.similarity("u" + b22, "u" + str(x)), "u" + str(x)) for x in range(50)]
            return max(b19, b20 = lambda x: x[0])
        else:
            print(f"Word {b22} not in dictionary")
            return (0, 0)
b1 = [['apple', 'banana', 'orange'], ['dog', 'cat', 'horse'], ['tree', 'flower', 'grass']]
b2 = gensim.models.ldamodel.LdaModel()
b21 = class1(b1, b2, True, 'b17', 100, 5, 1)
b22 = 'apple'
b23 = b21.fonk6(b22)
print(f"Most similar topic to '{b22}': {b23[1]} with similarity score {b23[0]}")