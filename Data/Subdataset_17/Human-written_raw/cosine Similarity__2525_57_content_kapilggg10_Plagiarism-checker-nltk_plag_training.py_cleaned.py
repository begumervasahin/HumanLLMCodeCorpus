from nltk.tokenize import word_tokenize
import os
import string
from collections import Counter
from nltk.corpus import stopwords
from nltk.stem.porter import *
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem.porter import PorterStemmer
def get_tokenized(text):
    tokens = word_tokenize(text)
    return tokens
def stemming(tokens, stemmer):
    stemmed = []
    for item in tokens:
        stemmed.append(stemmer.stem(item))
    return stemmed
def preprocessing(text):
    tokens = get_tokenized(text)
    stemmer = PorterStemmer()
    stem = stemming(tokens,stemmer)
    return stem
def training_tfs():
    fs = []
    i = 0
    path = 'C:\\Users\\Kapil Goyal\\Desktop\\nlp_assignment\\files'
    token_dictionary = {}
    for subdir, dirs,files in os.walk(path):
        for file in files:
            file_path = subdir + os.path.sep + file
            f = open(file_path,'r')
            lowers = f.read().lower()
            no_punctuation = lowers.translate(string.punctuation)
            token_dictionary[file] = no_punctuation
            fs.append(file)
    tfidf = TfidfVectorizer(tokenizer = preprocessing,stop_words = 'english')
    tfs = tfidf.fit_transform(token_dictionary.values())
    return tfidf,tfs,fs