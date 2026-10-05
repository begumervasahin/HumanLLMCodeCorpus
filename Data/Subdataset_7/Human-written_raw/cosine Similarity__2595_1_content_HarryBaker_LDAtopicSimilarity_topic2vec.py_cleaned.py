b1 = 'loaner'
import gensim
import numpy as np
import sympy
from operator import itemgetter
from gensim import matutils, models
import math
import random
import string
from gensim.corpora import Dictionary
class b12:
    def fonk1(self, b2, b3, flag, b4, b5, b6, b7):
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
        self.b5 = b5
        self.b6 = b6
        self.b7 = b7
        self.b8 = []
        self.b9 = gensim.corpora.Dictionary.load('/Users/loaner/Documents/Renncode_2016/SKPN/py-server/comTragDict')
        self.b10 = self.b9.token2id
        if flag:
            print "starting variation"
            print "There are %d many b2" % len(self.b2)
            self.fonk2(self.b2)
            random.shuffle(self.b8)
            b11 = self.b8
            self.b12 = models.Word2Vec(self.b8, b5=self.b5, b6=self.b6, min_count=self.b7, workers=2)
            self.b12.save(self.b4)
            random.shuffle(self.b2)
            self.b13 = models.Word2Vec(self.b2, b5=self.b5, b6=self.b6, min_count=3, workers=2)
            self.b12.save(self.b4 + "_w2v")
        self.b12 = models.Word2Vec.load(self.b4)
        self.b14 = []
        for b11 in range(0,50):
            self.b14.append(self.b3.show_topic(b11))
        self.b15 = []
        for b11 in range(0,50):
            self.b15.append(self.b12.most_similar(b16 = ["u" + str(b11)]))
        b17 = self.b15
        b18 = self.b14
        print self.b4 + "is finished"
    def fonk2(self, b2):
        b19 = []
        a1 = 0
        for sentance in b2:
            print a1
            a1+= 1
            b20 = self.fonk3(sentance)
            b19.append(b20)
        return b19
    def fonk3(self,sentance):
        b21 = []
        a2 = 0
        for word in sentance:
            b22 = self.fonk4(word, a2, sentance)
            b21.append(b22)
            a2 += 1
        return b21
    def fonk4(self, word, a2, sentance):
        b20 = list(sentance)
        if word in self.b10:
            b23 = self.b9.doc2bow([word])
            b24 = self.b3[b23]
            b25 = b24[-1][0]
            b20[a2] = "u" + str(b25)
        self.b8.append(b20)
        return b20
    def fonk5(self, word):
        b26 = (0,0)
        if word in self.b10:
            for b11 in range(0,50):
                b27 = self.b12.similarity("u" + word, "u" + str(b11))
                if b27 > b26[0]:
                    b26[0] = b27
                    b26[1] = "u" + str(b11)
        else:
            print "Word %s not in b9" % word
        return b26