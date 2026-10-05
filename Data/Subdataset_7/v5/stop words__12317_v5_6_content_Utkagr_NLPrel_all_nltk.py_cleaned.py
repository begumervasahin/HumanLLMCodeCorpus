import nltk
import random
import pickle
from nltk.corpus import stopwords, wordnet, movie_reviews
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
def fonk1(text):
    b1 = word_tokenize(text)
    b2 = set(stopwords.words("english"))
    return [word for word in b1 if word.lower() not in b2]
def fonk2(words):
    b3 = PorterStemmer()
    return [b3.stem(word) for word in words]
def fonk3(word):
    b4 = WordNetLemmatizer()
    return b4.lemmatize(word)
def fonk4(word):
    b5 = set()
    b6 = set()
    for synset in wordnet.synsets(word):
        for lemma in synset.lemmas():
            b5.add(lemma.name())
            if lemma.b6():
                b6.add(lemma.b6()[0].name())
    return b5, b6
def fonk5(word1, word2):
    b7 = wordnet.synsets(word1)
    b8 = wordnet.synsets(word2)
    if b7 and b8:
        return b7[0].wup_similarity(b8[0])
    return None
def fonk6(document, b19):
    b9 = set(document)
    b10 = {word: (word in b9) for word in b19}
    return b10
def fonk7(b21):
    b11 = nltk.NaiveBayesClassifier.train(b21)
    return b11
def fonk8(b11, b22):
    b12 = nltk.classify.b12(b11, b22) * 100
    print("Classifier b12 percent:", b12)
    b11.show_most_informative_features(15)
def fonk9(b11, filename):
    with open(filename, "wb") as save_file:
        pickle.dump(b11, save_file)
def fonk10(filename):
    with open(filename, "rb") as load_file:
        b11 = pickle.load(load_file)
    return b11
def fonk11():
    b13 = input("Enter a b13: ")
    b1 = fonk1(b13)
    b14 = fonk2(b1)
    b15 = fonk3("cats")
    b5, b6 = fonk4("good")
    b16 = fonk5("ship", "boat")
    b17 = [(list(movie_reviews.words(fileid)), category)
                 for category in movie_reviews.categories()
                 for fileid in movie_reviews.fileids(category)]
    random.shuffle(b17)
    b18 = nltk.FreqDist(w.lower() for w in movie_reviews.words())
    b19 = list(b18.keys())[:3000]
    b20 = [(fonk6(rev, b19), category) for (rev, category) in b17]
    b21 = b20[:1900]
    b22 = b20[1900:]
    b11 = fonk7(b21)
    fonk8(b11, b22)
    fonk9(b11, "naivebayes.pickle")
    b23 = fonk10("naivebayes.pickle")
if b24 = = "__main__":
    fonk11()