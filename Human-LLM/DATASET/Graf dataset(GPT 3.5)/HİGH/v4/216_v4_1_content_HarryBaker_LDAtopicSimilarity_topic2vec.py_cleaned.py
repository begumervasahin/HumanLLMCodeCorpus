import gensim
import random
class class1:
    def fonk1(self, b1, b2, use_variation, b3, b4, b5, b6):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
        self.b5 = b5
        self.b6 = b6
        self.b7 = []
        self.b8 = gensim.corpora.Dictionary.load('/path/to/b8').token2id
        if use_variation:
            print("Starting sentence variation...")
            print(f"There are {len(self.b1)} b1.")
            self.fonk2()
            random.shuffle(self.b7)
            self.fonk5()
            random.shuffle(self.b1)
            self.fonk6()
            print(f"class1 model saved as {self.b3}.")
        self.b9 = gensim.models.Word2Vec.load(self.b3)
        self.b10 = [self.b2.show_topic(x) for x in range(50)]
        self.b11 = [self.b9.b22(positive=["u" + str(x)]) for x in range(50)]
        print(f"{self.b3} model loaded.")
    def fonk2(self):
        for sentence in self.b1:
            b12 = self.fonk3(sentence)
            self.b7.append(b12)
    def fonk3(self, sentence):
        b12 = []
        for index, b21 in enumerate(sentence):
            b13 = self.fonk4(b21, index, sentence)
            b12.append(b13)
        return b12
    def fonk4(self, b21, index, sentence):
        if b21 in self.b8:
            b14 = self.b8.doc2bow([b21])
            b15 = self.b2[b14]
            b16 = b15[-1][0] if b15 else ''
            return "u" + str(b16)
        return b21
    def fonk5(self):
        self.b9 = gensim.models.Word2Vec(self.b7, b4=self.b4, b5=self.b5, b6=self.b6, workers=2)
        self.b9.save(self.b3)
    def fonk6(self):
        self.b17 = gensim.models.Word2Vec(self.b1, b4=self.b4, b5=self.b5, b6=3, workers=2)
        self.b17.save(self.b3 + "_w2v")
    def fonk7(self, b21):
        if b21 in self.b8:
            b18 = [(self.b9.similarity("u" + b21, "u" + str(x)), "u" + str(x)) for x in range(50)]
            return max(b18, b19 = lambda x: x[0])
        else:
            print(f"Word {b21} not found in b8")
            return (0, 0)
b1 = [['apple', 'banana', 'orange'], ['dog', 'cat', 'horse'], ['tree', 'flower', 'grass']]
b2 = gensim.models.ldamodel.LdaModel()
b20 = class1(b1, b2, True, 'topic2vec_model', 100, 5, 1)
b21 = 'apple'
b22 = b20.fonk7(b21)
print(f"Most similar b15 to '{b21}': {b22[1]} with similarity score {b22[0]}")