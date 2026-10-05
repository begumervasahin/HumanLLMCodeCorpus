import sys
import nltk
import cPickle
from sklearn.feature_extraction.text import TfidfVectorizer
nltk.download('stopwords')
with open('model/vector/vector.pkl', 'rb') as vectorizer_file:
    b1 = cPickle.load(vectorizer_file)
b2 = sys.argv[1] + '_twt'
b3 = sys.argv[2]
with open(b2, 'r') as input_file:
    b4 = input_file.readlines()
b5 = b1.transform(b4)
with open('model/binary_lin.pkl', 'rb') as svm_model_file:
    b6 = cPickle.load(svm_model_file)
b7 = b6.predict(b5)
with open(b3, 'w') as output_file:
    for prediction in b7:
        output_file.write(str(prediction) + '\n')
print("Predictions have been written to", b3)