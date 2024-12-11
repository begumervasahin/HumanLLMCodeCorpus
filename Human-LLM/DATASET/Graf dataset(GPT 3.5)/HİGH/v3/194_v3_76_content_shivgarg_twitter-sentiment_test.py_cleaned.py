import sys
import nltk
import cPickle
from sklearn.feature_extraction.text import TfidfVectorizer
nltk.download('stopwords')
def fonk1(file_path):
    with open(file_path, 'rb') as file:
        return cPickle.load(file)
b1 = 'model/vector/vector.pkl'
b2 = fonk1(b1)
b3 = sys.argv[1] + '_twt'
b4 = sys.argv[2]
with open(b3, 'r') as input_file:
    b5 = input_file.readlines()
b6 = b2.transform(b5)
b7 = 'model/binary_lin.pkl'
b8 = fonk1(b7)
b9 = b8.predict(b6)
with open(b4, 'w') as output_file:
    for prediction in b9:
        output_file.write(str(prediction) + '\n')
print("Predictions have been written to", b4)