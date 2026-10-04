from nltk.tokenize import word_tokenize
import os
import string
from collections import Counter
from nltk.corpus import stopwords
from nltk.b4.porter import *
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.b4.porter import PorterStemmer
def fonk1(text):
    b1 = word_tokenize(text)
    return b1
def fonk2(b1, b3):
    b2 = []
    for item in b1:
        b2.append(b3.b4(item))
    return b2
def fonk3(text):
    b1 = fonk1(text)
    b3 = PorterStemmer()
    b4 = fonk2(b1,b3)
    return b4
def fonk4():
    b5 = []
    a1 = 0
    b6 = 'C:\\Users\\Kapil Goyal\\Desktop\\nlp_assignment\\files'
    b7 = {}
    for subdir, dirs,files in os.walk(b6):
        for file in files:
            b8 = subdir + os.b6.sep + file
            b9 = open(b8,'r')
            b10 = b9.read().lower()
            b11 = b10.translate(string.punctuation)
            b7[file] = b11
            b5.append(file)
    b12 = TfidfVectorizer(tokenizer = preprocessing,stop_words = 'english')
    b13 = b12.fit_transform(b7.values())
    return b12,b13,b5