import nltk
import random
import pickle
import re
from nltk.corpus import stopwords, state_union, gutenberg, wordnet, movie_reviews
from nltk.tokenize import PunktSentenceTokenizer, word_tokenize, sent_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('state_union')
nltk.download('gutenberg')
nltk.download('wordnet')
nltk.download('movie_reviews')
b1 = input("Enter a b1: ")
b2 = word_tokenize(b1)
b3 = set(stopwords.b15("english"))
b4 = [w for w in b2 if w not in b3]
b5 = PorterStemmer()
b6 = [b5.stem(w) for w in b4]
b7 = nltk.pos_tag(b2)
b8 = nltk.ne_chunk(b7)
b9 = WordNetLemmatizer()
b10 = [b9.lemmatize(w) for w in b2]
b11 = state_union.raw("2005-GWBush.txt")
b12 = state_union.raw("2006-GWBush.txt")
b13 = PunktSentenceTokenizer(b11)
b14 = b13.tokenize(b12)
def fonk1():
    try:
        for i in b14:
            b15 = word_tokenize(i)
            b16 = nltk.pos_tag(b15)
            b17 = r
            b18 = nltk.RegexpParser(b17)
            b19 = b18.parse(b16)
            print(b19)
    except Exception as e:
        print(str(e))
b20 = '''
Jessica is 15 years old, and Daniel is 27 years old.
Edward is 97, and his grandfather, Oscar, is 102.
'''
b21 = re.findall(r'\d{1,3}', b20)
b22 = re.findall(r'[A-Z][a-z]*', b20)
print("Ages:", b21)
print("Names:", b22)
b23 = wordnet.synsets("program")
print("Synsets:", b23)
print("First lemma name:", b23[0].lemmas()[0].name())
print("Definition:", b23[0].definition())
print("Examples:", b23[0].examples())
b24 = wordnet.synset("ship.n.01")
b25 = wordnet.synset("boat.n.01")
b26 = b24.wup_similarity(b25)
print("Similarity between 'ship' and 'boat':", b26)
b27 = [(list(movie_reviews.b15(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]
random.shuffle(b27)
b28 = nltk.FreqDist(w.lower() for w in movie_reviews.b15())
b29 = list(b28.keys())[:3000]
def fonk2(document):
    b15 = set(document)
    b30 = {}
    for w in b29:
        b30[w] = (w in b15)
    return b30
b31 = [(fonk2(rev), category) for (rev, category) in b27]
b32 = b31[:1900]
b33 = b31[1900:]
b34 = nltk.NaiveBayesClassifier.train(b32)
print("Classifier accuracy percent:", (nltk.classify.accuracy(b34, b33)) * 100)
b34.show_most_informative_features(15)
b35 = open("naivebayes.pickle", "wb")
pickle.dump(b34, b35)
b35.close()
b36 = open("naivebayes.pickle", "rb")
b34 = pickle.load(b36)
b36.close()