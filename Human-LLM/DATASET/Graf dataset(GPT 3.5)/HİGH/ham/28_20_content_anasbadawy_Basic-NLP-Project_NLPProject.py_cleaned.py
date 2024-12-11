import csv
import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.util import b16
from nltk.corpus import stopwords
from collections import Counter
from nltk.probability import FreqDist
from collections import defaultdict
from nltk.collocations import *
from nltk.metrics import *
from string import punctuation
import os
import numpy
from sklearn.feature_extraction.b27 import CountVectorizer
from sklearn.feature_extraction.b27 import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn import preprocessing
from textblob import Word
with open('rev.csv','r') as csv_file:
    b1 = csv.reader(csv_file)
    next(b1)
    b2 = []
    for line in b1:
            b2.append(line[3])
b3 = PorterStemmer()
b4 = []
b5 = []
for r in b2:
    b4.append(word_tokenize(r))
for r in b4:
    b6 = []
    for word in r:
        b6.append(b3.stem(word))
    b5.append(b6)
print(b5)
b7 = set(stopwords.words('english'))
b8 = []
for r in b5:
    b9 = []
    for word in r:
      if word not in b7:
          b9.append(word)
    b8.append(b9)
b10 = []
for r in b8:
    b11 = FreqDist(r)
    b10.append(b11.most_common(10))
def fonk1(b27):
    b7 = set(stopwords.words('english'))
    b12 = []
    b13 = []
    b3 = PorterStemmer()
    b12 = word_tokenize(b27)
    b9 = []
    for word in b12:
      if word not in b7:
          b9.append(word)
    b14 = []
    for word in b9:
      if word not in punctuation:
          b14.append(word)
    return b14
b15 = ' '.join(b2)
def fonk2(list,n):
        b11 = FreqDist(list)
        return b11.most_common(n)
def fonk3(list, n ):
    b16 = []
    for i in range(len(list)-(n-1)):
        b16.append(tuple(list[i:i+n]))
    return b16
b17 = []
b17 = fonk3(fonk1(b15), 2)
def fonk4(list):
    b18 = []
    for words in list:
        b18.append(' '.join(words))
    return b18
def fonk5(list,b11,n):
    b19 = []
    b20 = []
    b19 = fonk4(list)
    a1 = 0
    for b21 in set(b19):
        if b19.count(b21) == b11:
                b20.append(tuple(b21.split()))
                a1+=1
                if a1 = =n:
                    break
                elif b21 = = range(len(set(b19))-1):
                    for b21 in set(b19):
                        if b19.count(b21) > b11:
                            b20.append(tuple(b21.split()))
                            a1+=1
                            if a1 = =n:
                                break
    return b20
b22 = []
b22 = fonk5(b17,2,10)
def fonk6(filteredBigrams):
    b23 = []
    b19 = []
    b23 = fonk4(filteredBigrams)
    b19 = ' '.join(b23)
    b19 = b19.split()
    b24 = nltk.collocations.BigramAssocMeasures()
    b25 = BigramCollocationFinder.from_words(b19)
    b26 = b25.score_ngrams( b24.likelihood_ratio )
    return(b26)
def fonk7(scoredBigrams):
     b23 = []
     for i in scoredBigrams:
         b23.append(i[0])
     return b23
b27 = word_tokenize(b15)
b28 = nltk.pos_tag(b27)
def fonk8(taggedlist):
     b29 = nltk.FreqDist(tag for (word, tag) in taggedlist)
     return b29.most_common()
def fonk9(taggedlist,posTag):
    b30 = nltk.FreqDist(taggedlist)
    return [wt[0] for (wt, _) in b30.most_common() if wt[1] == posTag]
b31 = fonk9(b28,'PRP')