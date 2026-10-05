import nltk
import random
import re
import pickle
from nltk.corpus import stopwords, state_union, wordnet, gutenberg, movie_reviews
from nltk.tokenize import word_tokenize, sent_tokenize, PunktSentenceTokenizer
from nltk.stem import PorterStemmer, WordNetLemmatizer
b1 = input("Enter a b1: ")
b2 = word_tokenize(b1)
b3 = set(stopwords.b7("english"))
b4 = [w for w in b2 if w not in b3]
b5 = PorterStemmer()
b6 = [b5.stem(w) for w in example_words]
def fonk1():
    try:
        for i in tokenized:
            b7 = word_tokenize(i)
            b8 = nltk.pos_tag(b7)
            print(b8)
    except Exception as e:
        print(str(e))
def fonk2():
    try:
        for i in tokenized:
            b7 = word_tokenize(i)
            b8 = nltk.pos_tag(b7)
            b9 = nltk.ne_chunk(b8)
            b9.draw()
            print(b8)
    except Exception as e:
        print(str(e))
b10 = WordNetLemmatizer()
print(b10.lemmatize("cats"))
b11 = []
b12 = []
for syn in wordnet.synsets("good"):
    for l in syn.lemmas():
        b11.append(l.name())
        if l.b12():
            b12.append(l.b12()[0].name())
b13 = wordnet.synset("ship.n.01")
b14 = wordnet.synset("boat.n.01")
print(b13.wup_similarity(b14))
b15 = [(list(movie_reviews.b7(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]
random.shuffle(b15)
b16 = nltk.FreqDist(w.lower() for w in movie_reviews.b7())
b17 = list(b16.keys())[:3000]
def fonk3(document):
    b7 = set(document)
    b18 = {w: (w in b7) for w in b17}
    return b18
b19 = [(fonk3(rev), category) for (rev, category) in b15]
b20 = b19[:1900]
b21 = b19[1900:]
b22 = nltk.NaiveBayesClassifier.train(b20)
print("Classifier accuracy percent:", (nltk.classify.accuracy(b22, b21)) * 100)
b22.show_most_informative_features(15)
with open("naivebayes.pickle", "wb") as save_classifier:
    pickle.dump(b22, save_classifier)
with open("naivebayes.pickle", "rb") as classifier_f:
    b22 = pickle.load(classifier_f)