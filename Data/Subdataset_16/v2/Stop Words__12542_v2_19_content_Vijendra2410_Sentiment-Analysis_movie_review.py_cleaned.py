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
    def fonk2(self, b7):
        b2 = [c.fonk2(b7) for c in self.b1]
        return mode(b2)
    def fonk3(self, b7):
        b2 = [c.fonk2(b7) for c in self.b1]
        b3 = b2.count(mode(b2))
        return b3 / len(b2)
def fonk4():
    b4 = [(list(movie_reviews.b6(fileid)), category)
                 for category in movie_reviews.categories()
                 for fileid in movie_reviews.fileids(category)]
    random.shuffle(b4)
    return b4
def fonk5():
    b5 = nltk.FreqDist(w.lower() for w in movie_reviews.b6())
    return list(b5.keys())[:3500]
def fonk6(document, b12):
    b6 = set(document)
    b7 = {w: (w in b6) for w in b12}
    return b7
def fonk7(b4, b12):
    return [(fonk6(rev, b12), category) for (rev, category) in b4]
def fonk8(training_set):
    b8 = nltk.NaiveBayesClassifier.train(training_set)
    b9 = SklearnClassifier(MultinomialNB()).train(training_set)
    b10 = SklearnClassifier(BernoulliNB()).train(training_set)
    b11 = SklearnClassifier(LogisticRegression(max_iter=10000)).train(training_set)
    return b8, b9, b10, b11
def fonk9(b14, *classifiers):
    for classifier in classifiers:
        print(f"{classifier.__class__.b16} accuracy:", nltk.classify.accuracy(classifier, b14))
def fonk10():
    b4 = fonk4()
    b12 = fonk5()
    b13 = fonk7(b4, b12)
    training_set, b14 = b13[:1900], b13[1900:]
    b8, b9, b10, b11 = fonk8(training_set)
    fonk9(b14, b8, b9, b10, b11)
    b15 = class1(b8, b9, b10)
    print("Voted classifier accuracy:", nltk.classify.accuracy(b15, b14))
    for i in range(5):
        print(f"Classification: {b15.fonk2(b14[i][0])}, "
              f"Confidence: {b15.fonk3(b14[i][0])}")
    b8.show_most_informative_features(15)
if b16 = = "__main__":
    fonk10()