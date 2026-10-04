
import nltk
import random
from nltk.corpus import movie_reviews
import pickle
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.svm import SVC, LinearSVC, NuSVC
from sklearn.linear_model import LogisticRegression, SGDClassifier
from nltk.classify import ClassifierI
from statistics import mode
class class1(ClassifierI):
    def __init__ (self, *classifiers):
        self.b1 = classifiers
    def fonk1(self, b10):
        b2 = []
        for c in self.b1:
            b3 = c.fonk1(b10)
            b2.append(b3)
        return mode(b2)
    def fonk2(self, b10):
        b2 = []
        for c in self.b1:
            b3 = c.fonk1(b10)
            b2.append(b3)
        b4 = b2.count(mode(b2))
        b5 = b4/ len(b2)
        return b5
b6 = [ (list( movie_reviews.b9(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]
random.shuffle(b6)
print(b6[100])
b7 = []
for w in movie_reviews.b9():
    b7.append(w.lower())
b7 = nltk.FreqDist(b7)
'''print( b7.most_common(25))
print( b7["stupid"])'''
b8 = list(b7.keys())[:3500]
def fonk3(document):
    b9 = set(document)
    b10 = {}
    for w in b8:
        b10[w]=( w in b9)
    return b10
b11 = [(fonk3(rev), category) for (rev, category) in b6]
b12 = b11[:1900]
b13 = b11[1900:]
b14 = nltk.NaiveBayesClassifier.train(b12)
print("naive bayes:    ",nltk.classify.accuracy(b14, b13))
b15 = SklearnClassifier(MultinomialNB())
b15.train(b12)
print("b15 acc;   ", nltk.classify.accuracy(b15, b13))
b16 = SklearnClassifier(BernoulliNB())
b16.train(b12)
print("b16 acc;   ", nltk.classify.accuracy(b16, b13))
b17 = SklearnClassifier(LogisticRegression())
b17.train(b12)
print("b17 acc;   ", nltk.classify.accuracy(b17, b13))
b18 = class1( b14,b15,b16)
print("b18 accuracy:" ,nltk.classify.accuracy(b18, b13))
print("classification:  ", b18.fonk1(b13[1][0]) , "confidence: ", b18.fonk2(b13[1][0]))
print("classification:  ", b18.fonk1(b13[2][0]) , "confidence:  ", b18.fonk2(b13[2][0]))
print("classification:  ", b18.fonk1(b13[3][0]) , "confidence:  ", b18.fonk2(b13[3][0]))
print("classification:  ", b18.fonk1(b13[4][0]) , "confidence:  ", b18.fonk2(b13[4][0]))
'''b19 = open("naivebayes.pickle" , "rb")
b14 = pickle.load(b19)
b19.close() '''
b14.show_most_informative_features(15)
'''b20 = open("naivebayes.pickle", "wb")
pickle.dump(b14, b20)
b20.close() '''