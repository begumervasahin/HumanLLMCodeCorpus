import csv
import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.collocations import BigramCollocationFinder, BigramAssocMeasures
from string import punctuation
def fonk1(file_path):
    with open(file_path, 'r') as csv_file:
        b1 = csv.reader(csv_file)
        next(b1)
        b2 = [line[3] for line in b1]
    return b2
def fonk2(texts):
    b3 = PorterStemmer()
    b4 = []
    for text in texts:
        b5 = word_tokenize(text)
        b6 = [b3.stem(word) for word in b5]
        b4.append(b6)
    return b4
def fonk3(texts):
    b7 = set(stopwords.words('english'))
    b8 = []
    for text in texts:
        b9 = [word for word in text if word not in b7]
        b8.append(b9)
    return b8
def fonk4(text):
    b7 = set(stopwords.words('english'))
    b5 = word_tokenize(text)
    b10 = [word for word in b5 if word not in b7 and word not in punctuation]
    return b10
def fonk5(texts, b11 = 10):
    b12 = fonk4(' '.join(texts))
    return FreqDist(b12).most_common(b11)
def fonk6(texts, b11, frequency, b13 = 10):
    b14 = [tuple(text[i:i+b11]) for text in texts for i in range(len(text)-(b11-1))]
    b15 = FreqDist(b14)
    return [ng for ng, b16 in b15.items() if b16 = = frequency][:b13]
def fonk7(texts):
    b17 = BigramAssocMeasures()
    b18 = BigramCollocationFinder.from_words(' '.join(texts))
    b19 = b18.score_ngrams(b17.likelihood_ratio)
    return [score[0] for score in b19]
def fonk8(text):
    b5 = word_tokenize(text)
    b20 = nltk.pos_tag(b5)
    b21 = FreqDist(tag for _, tag in b20)
    b22 = b21.most_common()
    b23 = [word for (word, tag) in b20 if tag == 'PRP']
    return b22, b23
if b24 = = "__main__":
    b25 = fonk1('rev.csv')
    b26 = fonk2(b25)
    b27 = fonk3(b26)
    print("Most common words:", fonk5(b27))
    print("Frequent bigrams:", fonk6(b27, 2, 2))
    print("Scored bigrams:", fonk7(b27))
    tags, b23 = fonk8(' '.join(b25))
    print("Most common POS tags:", tags)
    print("Pronouns:", b23)