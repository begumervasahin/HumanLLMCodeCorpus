import csv
import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.util import ngrams
from nltk.corpus import stopwords
from collections import Counter
from nltk.probability import FreqDist
from collections import defaultdict
from nltk.collocations import *
from nltk.metrics import *
from string import punctuation
import os
import numpy
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn import preprocessing
from textblob import Word
with open('rev.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    reviewsList=[]
    for line in csv_reader:
            reviewsList.append(line[3])
ps = PorterStemmer()
tokenizedList = []
stemsList = []
for r in reviewsList:
    tokenizedList.append(word_tokenize(r))
for r in tokenizedList:
    stems = []
    for word in r:
        stems.append(ps.stem(word))
    stemsList.append(stems)
print(stemsList)
stop_words = set(stopwords.words('english'))
all_filtered = []
for r in stemsList:
    filtered_Words = []
    for word in r:
      if word not in stop_words:
          filtered_Words.append(word)
    all_filtered.append(filtered_Words)
mostFreq = []
for r in all_filtered:
    frequency = FreqDist(r)
    mostFreq.append(frequency.most_common(10))
def preprocess(text):
    stop_words = set(stopwords.words('english'))
    tokenizedText = []
    textStems = []
    ps = PorterStemmer()
    tokenizedText = word_tokenize(text)
    filtered_Words = []
    for word in tokenizedText:
      if word not in stop_words:
          filtered_Words.append(word)
    filtered_Words2 = []
    for word in filtered_Words:
      if word not in punctuation:
          filtered_Words2.append(word)
    return filtered_Words2
reviewsText = ' '.join(reviewsList)
def freqMost(list,n):
        frequency = FreqDist(list)
        return frequency.most_common(n)
def listNgrams(list, n ):
    ngrams = []
    for i in range(len(list)-(n-1)):
        ngrams.append(tuple(list[i:i+n]))
    return ngrams
freqBigramList = []
freqBigramList = listNgrams(preprocess(reviewsText), 2)
def freq(list):
    freqList=[]
    for words in list:
        freqList.append(' '.join(words))
    return freqList
def listFreqBigram(list,frequency,n):
    newList=[]
    finalList=[]
    newList = freq(list)
    counts=0
    for sen in set(newList):
        if newList.count(sen) == frequency:
                finalList.append(tuple(sen.split()))
                counts+=1
                if counts==n:
                    break
                elif sen== range(len(set(newList))-1):
                    for sen in set(newList):
                        if newList.count(sen) > frequency:
                            finalList.append(tuple(sen.split()))
                            counts+=1
                            if counts==n:
                                break
    return finalList
scoreBigramList = []
scoreBigramList = listFreqBigram(freqBigramList,2,10)
def scoredBigram(filteredBigrams):
    splitedList=[]
    newList=[]
    splitedList= freq(filteredBigrams)
    newList= ' '.join(splitedList)
    newList=newList.split()
    bgm    = nltk.collocations.BigramAssocMeasures()
    finder = BigramCollocationFinder.from_words(newList)
    scored = finder.score_ngrams( bgm.likelihood_ratio )
    return(scored)
def sortedBigram(scoredBigrams):
     splitedList=[]
     for i in scoredBigrams:
         splitedList.append(i[0])
     return splitedList
text = word_tokenize(reviewsText)
taggedList = nltk.pos_tag(text)
def numOfTags(taggedlist):
     tag_fd = nltk.FreqDist(tag for (word, tag) in taggedlist)
     return tag_fd.most_common()
def findWords(taggedlist,posTag):
    word_tag_fd = nltk.FreqDist(taggedlist)
    return [wt[0] for (wt, _) in word_tag_fd.most_common() if wt[1] == posTag]
wordsList= findWords(taggedList,'PRP')