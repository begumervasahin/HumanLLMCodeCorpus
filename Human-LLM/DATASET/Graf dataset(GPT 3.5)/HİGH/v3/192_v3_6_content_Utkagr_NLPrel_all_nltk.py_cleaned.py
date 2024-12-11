import nltk
import random
import pickle
import re
def fonk1():
    nltk.download('punkt')
    nltk.download('stopwords')
    nltk.download('state_union')
    nltk.download('gutenberg')
    nltk.download('wordnet')
    nltk.download('movie_reviews')
def fonk2(b32):
    b1 = nltk.word_tokenize(b32)
    b2 = set(nltk.corpus.stopwords.b13("english"))
    b3 = [word for word in b1 if word not in b2]
    b4 = nltk.stem.PorterStemmer()
    b5 = [b4.stem(word) for word in b3]
    b6 = nltk.pos_tag(b1)
    b7 = nltk.ne_chunk(b6)
    b8 = nltk.stem.WordNetLemmatizer()
    b9 = [b8.lemmatize(word) for word in b1]
    return b1, b3, b5, b6, b7, b9
def fonk3(sample_text):
    b10 = nltk.corpus.state_union.raw("2005-GWBush.txt")
    b11 = nltk.tokenize.PunktSentenceTokenizer(b10)
    b12 = b11.tokenize(sample_text)
    for b32 in b12:
        b13 = nltk.word_tokenize(b32)
        b14 = nltk.pos_tag(b13)
        b15 = r
        b16 = nltk.RegexpParser(b15)
        b17 = b16.parse(b14)
        print(b17)
def fonk4(example_string):
    b18 = re.findall(r'\d{1,3}', example_string)
    b19 = re.findall(r'[A-Z][a-z]*', example_string)
    print("Ages:", b18)
    print("Names:", b19)
def fonk5():
    b20 = nltk.corpus.wordnet.b20("program")
    print("Synsets:", b20)
    print("First lemma name:", b20[0].lemmas()[0].name())
    print("Definition:", b20[0].definition())
    print("Examples:", b20[0].examples())
    b21 = nltk.corpus.wordnet.synset("ship.n.01")
    b22 = nltk.corpus.wordnet.synset("boat.n.01")
    b23 = b21.wup_similarity(b22)
    print("Similarity between 'ship' and 'boat':", b23)
def fonk6():
    b24 = [(list(nltk.corpus.movie_reviews.b13(fileid)), category)
                 for category in nltk.corpus.movie_reviews.categories()
                 for fileid in nltk.corpus.movie_reviews.fileids(category)]
    random.shuffle(b24)
    b25 = nltk.FreqDist(word.lower() for word in nltk.corpus.movie_reviews.b13())
    b26 = list(b25.keys())[:3000]
    def fonk7(document):
        b13 = set(document)
        b27 = {}
        for word in b26:
            b27[word] = (word in b13)
        return b27
    b28 = [(fonk7(review), category) for (review, category) in b24]
    b29 = b28[:1900]
    b30 = b28[1900:]
    b31 = nltk.NaiveBayesClassifier.train(b29)
    print("Classifier accuracy percent:", (nltk.classify.accuracy(b31, b30)) * 100)
    b31.show_most_informative_features(15)
    with open("naivebayes.pickle", "wb") as save_classifier:
        pickle.dump(b31, save_classifier)
    with open("naivebayes.pickle", "rb") as classifier_f:
        b31 = pickle.load(classifier_f)
def fonk8():
    fonk1()
    b32 = input("Enter a b32: ")
    b1, b3, b5, b6, b7, b9 = fonk2(b32)
    fonk3(sample_text)
    fonk4(example_string)
    fonk5()
    fonk6()
if b33 = = "__main__":
    fonk8()