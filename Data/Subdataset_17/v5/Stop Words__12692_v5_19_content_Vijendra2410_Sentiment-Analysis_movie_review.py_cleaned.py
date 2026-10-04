import nltk
import random
from nltk.corpus import movie_reviews
from nltk.classify import ClassifierI
from statistics import mode
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.linear_model import LogisticRegression
import pickle
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
def prepare_data():
    documents = [(list(movie_reviews.words(fileid)), category)
                 for category in movie_reviews.categories()
                 for fileid in movie_reviews.fileids(category)]
    random.shuffle(documents)
    return documents
def extract_features(documents, num_features=3500):
    all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
    word_features = list(all_words.keys())[:num_features]
    def find_features(document):
        words = set(document)
        return {w: (w in words) for w in word_features}
    feature_sets = [(find_features(rev), category) for (rev, category) in documents]
    return feature_sets, word_features
def train_classifiers(training_set):
    naive_bayes_classifier = nltk.NaiveBayesClassifier.train(training_set)
    mnb_classifier = SklearnClassifier(MultinomialNB()).train(training_set)
    bern_classifier = SklearnClassifier(BernoulliNB()).train(training_set)
    logistic_classifier = SklearnClassifier(LogisticRegression()).train(training_set)
    return naive_bayes_classifier, mnb_classifier, bern_classifier, logistic_classifier
def evaluate_classifiers(classifiers, testing_set):
    for name, classifier in classifiers.items():
        accuracy = nltk.classify.accuracy(classifier, testing_set)
        print(f"{name} Accuracy: {accuracy}")
def main():
    documents = prepare_data()
    feature_sets, word_features = extract_features(documents)
    training_set = feature_sets[:1900]
    testing_set = feature_sets[1900:]
    naive_bayes_classifier, mnb_classifier, bern_classifier, logistic_classifier = train_classifiers(training_set)
    classifiers = {
        "Naive Bayes": naive_bayes_classifier,
        "MultinomialNB": mnb_classifier,
        "BernoulliNB": bern_classifier,
        "Logistic Regression": logistic_classifier
    }
    evaluate_classifiers(classifiers, testing_set)
    voted_classifier = VoteClassifier(naive_bayes_classifier, mnb_classifier, bern_classifier)
    print("Voted Classifier Accuracy:", nltk.classify.accuracy(voted_classifier, testing_set))
    for i in range(1, 5):
        print(f"Classification: {voted_classifier.classify(testing_set[i][0])}, "
              f"Confidence: {voted_classifier.confidence(testing_set[i][0])}")
    naive_bayes_classifier.show_most_informative_features(15)
    with open("naivebayes.pickle", "wb") as save_classifier:
        pickle.dump(naive_bayes_classifier, save_classifier)
if __name__ == "__main__":
    main()