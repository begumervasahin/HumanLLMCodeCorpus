import sys
import nltk
import numpy as np
import cPickle as pickle
from sklearn import svm
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))
stemmer = SnowballStemmer('english')
with open('model/vector/vector.pkl', 'rb') as file:
    vectorizer = pickle.load(file)
input_file = open(str(sys.argv[1]) + '_twt')
output_file = open(str(sys.argv[2]), 'w')
input_data = vectorizer.transform(input_file)
input_file.close()
with open('model/binary_lin.pkl', 'rb') as file:
    svm_model = pickle.load(file)
predictions = svm_model.predict(input_data)
for prediction in predictions:
    output_file.write(str(prediction) + '\n')
output_file.close()