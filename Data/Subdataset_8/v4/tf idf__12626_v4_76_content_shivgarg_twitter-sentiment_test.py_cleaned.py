import sys
import re
import nltk
import string
import operator
import random
import numpy as np
import cPickle as pickle
from sklearn import svm
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer, HashingVectorizer
from sklearn.model_selection import cross_val_score, ShuffleSplit
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import BernoulliNB, MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, SnowballStemmer
from sklearn.externals import joblib
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))
stemmer = SnowballStemmer('english')
with open('model/vector/vector.pkl', 'rb') as v:
    vectorizer = pickle.load(v)
input_file = open(str(sys.argv[1]) + '_twt')
output_file = open(str(sys.argv[2]), 'w')
x = vectorizer.transform(input_file)
input_file.close()
with open('model/binary_lin.pkl', 'rb') as model_file:
    svm_train = pickle.load(model_file)
predictions = svm_train.predict(x)
for prediction in predictions:
    output_file.write(str(prediction) + '\n')
output_file.close()