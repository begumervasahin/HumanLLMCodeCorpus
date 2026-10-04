import nltk
import random
from nltk.corpus import movie_reviews
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.linear_model import LogisticRegression
from nltk.classify import ClassifierI
from statistics import mode
class VoteClassifier(ClassifierI):
    def __init__(self, *classifiers):
        self._classifiers = classifiers
    def classify(self, features):
        votes = [c.classify(features) for c in self._classifiers]
        return mode(votes)
    def confidence(self, features):
        votes = [c.classify(features) for c in self._classifiers]
        choice_votes = votes.count(mode(votes))
        return choice_votes / len(votes)
documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]
random.shuffle(documents)
all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
word_features = list(all_words.keys())[:3500]
def find_features(document):
    words = set(document)
    features = {w: (w in words) for w in word_features}
    return features
feature_sets = [(find_features(rev), category) for (rev, category) in documents]
training_set = feature_sets[:1900]
testing_set = feature_sets[1900:]
nb_classifier = nltk.NaiveBayesClassifier.train(training_set)
print("Naive Bayes accuracy:", nltk.classify.accuracy(nb_classifier, testing_set))
mnb_classifier = SklearnClassifier(MultinomialNB())
mnb_classifier.train(training_set)
print("Multinomial NB accuracy:", nltk.classify.accuracy(mnb_classifier, testing_set))
bernoulli_classifier = SklearnClassifier(BernoulliNB())
bernoulli_classifier.train(training_set)
print("Bernoulli NB accuracy:", nltk.classify.accuracy(bernoulli_classifier, testing_set))
logistic_classifier = SklearnClassifier(LogisticRegression(max_iter=10000))
logistic_classifier.train(training_set)
print("Logistic Regression accuracy:", nltk.classify.accuracy(logistic_classifier, testing_set))
voted_classifier = VoteClassifier(nb_classifier, mnb_classifier, bernoulli_classifier)
print("Voted classifier accuracy:", nltk.classify.accuracy(voted_classifier, testing_set))
for i in range(5):
    print(f"Classification: {voted_classifier.classify(testing_set[i][0])}, "
          f"Confidence: {voted_classifier.confidence(testing_set[i][0])}")
nb_classifier.show_most_informative_features(15)
