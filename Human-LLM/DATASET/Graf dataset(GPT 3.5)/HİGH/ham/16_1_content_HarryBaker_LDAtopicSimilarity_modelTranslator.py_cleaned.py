b1 = 'loaner'
import gensim
import numpy as np
import sympy
from operator import itemgetter
from gensim import matutils
import math
import json
from LDATopicSimilarity import TopicSimilarity
class class1:
    def fonk1(self, b2, b3):
        self.b2 = b2
        self.b3 = b3
        self.b4 = self.b2.id2word
        self.b5 = self.b3.id2word
        self.b6 = len(self.b4)
        self.b7 = dict(self.b4)
        for b22, value in self.b5.iteritems():
            if value in self.b4.itervalues():
                self.b7[b22] = value
            elif value not in self.b4.itervalues():
                self.b7[self.b6] = value
                self.b6 += 1
    def fonk2(self, topic1, topic2):
        b8 = []
        b9 = []
        b10 = sorted(self.b2.get_topic_terms(topic1, topn=self.b2.num_terms))
        b11 = sorted(self.b3.get_topic_terms(topic2, topn=self.b3.num_terms))
        b12 = True
        for b22, value in self.b7.iteritems():
            if value in self.b4.itervalues():
                b8.append((b22, b10[b22][1]))
            else:
                b8.append((b22, 0))
            for key1,b13 in self.b5.iteritems():
                if b13 = = value:
                    b9.append((b22, b11[key1][1]))
                    b12 = True
                    break
                b12 = False
            if b12 = = False:
                b9.append((b22,0))
        return self.fonk5(b8, b9, "Constant")
    def fonk3(self, b15, topic):
        b14 = []
        if b15 = = "Model1":
            for x in range(0,50):
                print "Topic %d" % x
                b16 = self.fonk2(topic,x)
                b17 = (b16, x, self.b3.show_topic(x), self.b2.show_topic(topic))
                b14.append(b17)
        if b15 = = "Model2":
            for x in range(0,50):
                print "Topic %d" % x
                b16 = self.fonk2(topic,x)
                b17 = (b16, x, self.b2.show_topic(x), self.b3.show_topic(topic))
                b14.append(b17)
        b14 = sorted(b14, b22=itemgetter(0), reverse=True)
        return b14
    def fonk4(self,b15,topic):
        return
    def fonk5(self, top1, top2, b22):
        b18 = []
        b19 = self.fonk6(top1,self.b2,b22)
        b20 = self.fonk6(top2,self.b3,b22)
        b21 = np.sqrt(0.5 * ((np.sqrt(b19) - np.sqrt(b20))**2).sum())
        return b21
    def fonk6(self,vector,b15,b22):
        if b22 = = "Constant":
            return self.fonk7(vector,b15)
        elif b22 = = "Dynamic":
            return self.fonk8(vector,b15)
    def fonk7(self, sparseVector,b15):
        b23 = sparseVector
        b24 = sorted(sparseVector, b22=itemgetter(1), reverse=True)
        b24 = [item[0] for item in b24[:15]]
        b25 = gensim.matutils.sparse2full(b23, self.b6)
        for x in range (0, b25.__len__()):
            if x not in b24:
                b25[x] = 0
        return b25
    def fonk8(self, sparseVector, b15):
        b23 = sparseVector
        b24 = sorted(sparseVector, b22=itemgetter(1), reverse=True)
        a1 = 0
        b13 = b24[0][1]
        b13 = math.floor(b13 * (10 ** 7)) / (10 ** 7)
        b26 = [b24[0][0]]
        for item in b24[1:]:
            b27 = item[1]
            b27 = math.floor(b27 * (10 ** 7)) / (10 ** 7)
            b28 = b13 - b27
            if b28 = = 0:
                a1 +=1
                b26.append(item[0])
                if a1 = = 5:
                    break
            else:
                a1 = 0
                b26.append(item[0])
            b13 = b27
        b25 = gensim.matutils.sparse2full(b23, self.b6)
        a2 = 0
        for a3 in b25:
            if a2 not in b26:
                a3 = 0
            a2+=1
        for x in range (0, b25.__len__()):
            if x not in b26:
                b25[x] = 0
        return b25