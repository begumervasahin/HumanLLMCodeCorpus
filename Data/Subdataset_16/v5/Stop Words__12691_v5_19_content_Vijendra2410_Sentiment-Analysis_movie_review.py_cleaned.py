import nltk
import random
from nltk.corpus import movie_reviews
from nltk.classify import ClassifierI
from statistics import mode
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.linear_model import LogisticRegression
import pickle
class class1(ClassifierI):
    def fonk1(self, *b17):
        self.b1 = b17
    def fonk2(self, features):
        b2 = [c.fonk2(features) for c in self.b1]
        return mode(b2)
    def fonk3(self, features):
        b2 = [c.fonk2(features) for c in self.b1]
        b3 = b2.count(mode(b2))
        return b3 / len(b2)
def fonk4():
    b4 = [(list(movie_reviews.b8(fileid)), category)
                 for category in movie_reviews.categories()
                 for fileid in movie_reviews.fileids(category)]
    random.shuffle(b4)
    return b4
def fonk5(b4, b5 = 3500):
    b6 = nltk.FreqDist(w.lower() for w in movie_reviews.b8())
    b7 = list(b6.keys())[:b5]
    def fonk6(document):
        b8 = set(document)
        return {w: (w in b8) for w in b7}
    b9 = [(fonk6(rev), category) for (rev, category) in b4]
    return b9, b7
def fonk7(b15):
    b10 = nltk.NaiveBayesClassifier.train(b15)
    b11 = SklearnClassifier(MultinomialNB()).train(b15)
    b12 = SklearnClassifier(BernoulliNB()).train(b15)
    b13 = SklearnClassifier(LogisticRegression()).train(b15)
    return b10, b11, b12, b13
def fonk8(b17, b16):
    for name, classifier in b17.items():
        b14 = nltk.classify.b14(classifier, b16)
        print(f"{name} Accuracy: {b14}")
def fonk9():
    b4 = fonk4()
    b9, b7 = fonk5(b4)
    b15 = b9[:1900]
    b16 = b9[1900:]
    b10, b11, b12, b13 = fonk7(b15)
    b17 = {
        "Naive Bayes": b10,
        "MultinomialNB": b11,
        "BernoulliNB": b12,
        "Logistic Regression": b13
    }
    fonk8(b17, b16)
    b18 = class1(b10, b11, b12)
    print("Voted Classifier Accuracy:", nltk.classify.b14(b18, b16))
    for i in range(1, 5):
        print(f"Classification: {b18.fonk2(b16[i][0])}, "
              f"Confidence: {b18.fonk3(b16[i][0])}")
    b10.show_most_informative_features(15)
    with open("naivebayes.pickle", "wb") as save_classifier:
        pickle.dump(b10, save_classifier)
if b19 = = "__main__":
    fonk9()