import nltk
import random
from nltk.corpus import movie_reviews
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.linear_model import LogisticRegression
from nltk.classify import ClassifierI
from statistics import mode
class class1(ClassifierI):
    def fonk1(self, *classifiers):
        self.b1 = classifiers
    def fonk2(self, b8):
        b2 = [c.fonk2(b8) for c in self.b1]
        return mode(b2)
    def fonk3(self, b8):
        b2 = [c.fonk2(b8) for c in self.b1]
        b3 = b2.count(mode(b2))
        return b3 / len(b2)
b4 = [(list(movie_reviews.b7(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]
random.shuffle(b4)
b5 = nltk.FreqDist(w.lower() for w in movie_reviews.b7())
b6 = list(b5.keys())[:3500]
def fonk4(document):
    b7 = set(document)
    b8 = {w: (w in b7) for w in b6}
    return b8
b9 = [(fonk4(rev), category) for (rev, category) in b4]
b10 = b9[:1900]
b11 = b9[1900:]
b12 = nltk.NaiveBayesClassifier.train(b10)
print("Naive Bayes accuracy:", nltk.classify.accuracy(b12, b11))
b13 = SklearnClassifier(MultinomialNB())
b13.train(b10)
print("Multinomial NB accuracy:", nltk.classify.accuracy(b13, b11))
b14 = SklearnClassifier(BernoulliNB())
b14.train(b10)
print("Bernoulli NB accuracy:", nltk.classify.accuracy(b14, b11))
b15 = SklearnClassifier(LogisticRegression(max_iter=10000))
b15.train(b10)
print("Logistic Regression accuracy:", nltk.classify.accuracy(b15, b11))
b16 = class1(b12, b13, b14)
print("Voted classifier accuracy:", nltk.classify.accuracy(b16, b11))
for i in range(5):
    print(f"Classification: {b16.fonk2(b11[i][0])}, "
          f"Confidence: {b16.fonk3(b11[i][0])}")
b12.show_most_informative_features(15)
