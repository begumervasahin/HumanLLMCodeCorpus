import csv
import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.collocations import BigramCollocationFinder, BigramAssocMeasures
from string import punctuation
from collections import defaultdict
with open('rev.csv', 'r') as csv_file:
    b1 = csv.reader(csv_file)
    next(b1)
    b2 = [line[3] for line in b1]
b3 = PorterStemmer()
b4 = []
for review in b2:
    b5 = word_tokenize(review)
    b6 = [b3.stem(word) for word in b5]
    b4.append(b6)
b7 = set(stopwords.words('english'))
b8 = []
for b6 in b4:
    b9 = [word for word in b6 if word not in b7]
    b8.append(b9)
def fonk1(text):
    b7 = set(stopwords.words('english'))
    b5 = word_tokenize(text)
    b9 = [word for word in b5 if word not in b7 and word not in punctuation]
    return b9
b10 = ' '.join(b2)
b11 = fonk1(b10)
b12 = FreqDist(b11).most_common(10)
def fonk2(lst, n):
    return [tuple(lst[i:i+n]) for i in range(len(lst)-(n-1))]
def fonk3(lst, frequency, n):
    b13 = FreqDist(lst)
    return [ng for ng, b14 in b13.items() if b14 = = frequency][:n]
b15 = fonk2(b11, 2)
b16 = fonk3(b15, 2, 10)
def fonk4(bigrams):
    b17 = BigramAssocMeasures()
    b18 = BigramCollocationFinder.from_words(bigrams)
    b19 = b18.score_ngrams(b17.likelihood_ratio)
    return [score[0] for score in b19]
b20 = fonk4(b16)
b21 = word_tokenize(b10)
b22 = nltk.pos_tag(b21)
b23 = FreqDist(tag for _, tag in b22)
b24 = b23.most_common()
b25 = [word for (word, tag) in b22 if tag == 'PRP']
print("Most common words:", b12)
print("Most common POS tags:", b24)
print("Pronouns:", b25)