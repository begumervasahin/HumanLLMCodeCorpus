import nltk
import random
import re
import pickle
from nltk.corpus import stopwords, state_union, wordnet, gutenberg, movie_reviews
from nltk.tokenize import word_tokenize, sent_tokenize, PunktSentenceTokenizer
from nltk.stem import PorterStemmer, WordNetLemmatizer
sentence = input("Enter a sentence: ")
tokens = word_tokenize(sentence)
stop_words = set(stopwords.words("english"))
filtered_tokens = [w for w in tokens if w not in stop_words]
ps = PorterStemmer()
stemmed_words = [ps.stem(w) for w in example_words]
def process_content():
    try:
        for i in tokenized:
            words = word_tokenize(i)
            tagged = nltk.pos_tag(words)
            print(tagged)
    except Exception as e:
        print(str(e))
def process_content():
    try:
        for i in tokenized:
            words = word_tokenize(i)
            tagged = nltk.pos_tag(words)
            namedEnt = nltk.ne_chunk(tagged)
            namedEnt.draw()
            print(tagged)
    except Exception as e:
        print(str(e))
lemmatizer = WordNetLemmatizer()
print(lemmatizer.lemmatize("cats"))
synonyms = []
antonyms = []
for syn in wordnet.synsets("good"):
    for l in syn.lemmas():
        synonyms.append(l.name())
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())
w1 = wordnet.synset("ship.n.01")
w2 = wordnet.synset("boat.n.01")
print(w1.wup_similarity(w2))
documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]
random.shuffle(documents)
all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
word_features = list(all_words.keys())[:3000]
def find_features(document):
    words = set(document)
    features = {w: (w in words) for w in word_features}
    return features
featuresets = [(find_features(rev), category) for (rev, category) in documents]
training_set = featuresets[:1900]
testing_set = featuresets[1900:]
classifier = nltk.NaiveBayesClassifier.train(training_set)
print("Classifier accuracy percent:", (nltk.classify.accuracy(classifier, testing_set)) * 100)
classifier.show_most_informative_features(15)
with open("naivebayes.pickle", "wb") as save_classifier:
    pickle.dump(classifier, save_classifier)
with open("naivebayes.pickle", "rb") as classifier_f:
    classifier = pickle.load(classifier_f)