import sys
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
import cPickle
nltk.download('stopwords')
with open('model/vector/vector.pkl', 'rb') as v:
    vectorizer = cPickle.load(v)
input_file_path = sys.argv[1] + '_twt'
output_file_path = sys.argv[2]
with open(input_file_path, 'r') as f:
    input_text = f.readlines()
x = vectorizer.transform(input_text)
with open('model/binary_lin.pkl', 'rb') as svm_model_file:
    svm_model = cPickle.load(svm_model_file)
predictions = svm_model.predict(x)
with open(output_file_path, 'w') as g:
    for pred in predictions:
        g.write(str(pred) + '\n')
print("Predictions written to", output_file_path)