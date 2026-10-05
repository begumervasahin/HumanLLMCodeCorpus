import sys
import re
from nltk.corpus import stopwords
import string
import operator
import random
from sklearn import svm
from nltk.stem import *
import pickle
from sklearn.externals import joblib
from sklearn import cross_validation
from sklearn.feature_extraction.text import TfidfVectorizer,CountVectorizer
from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.cross_validation import ShuffleSplit
import numpy as np
from sklearn.metrics import *
from nltk.stem.porter import *
from sklearn.naive_bayes import BernoulliNB
from sklearn.naive_bayes import MultinomialNB
from nltk.stem.snowball import SnowballStemmer
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
import nltk
import cPickle
with open('model/vector/vector.pkl','r') as v:
	b1 = cPickle.load(v)
b2 = open(str(sys.argv[1])+'_twt')
b3 = open(str(sys.argv[2]),'w')
b4 = b1.transform(b2)
b2.close()
with open('model/binary_lin.pkl','r') as v:
	b5 = cPickle.load(v)
b6 = b5.predict(b4)
for a in b6:
	b3.write(str(a)+'\n')
b3.close()