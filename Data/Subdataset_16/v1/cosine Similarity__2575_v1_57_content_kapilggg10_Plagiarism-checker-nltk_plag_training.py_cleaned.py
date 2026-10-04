import os
import string
from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
def fonk1(text):
    return word_tokenize(text)
def fonk2(b1, b2):
    return [b2.stem(token) for token in b1]
def fonk3(text):
    b1 = fonk1(text)
    b2 = PorterStemmer()
    return fonk2(b1, b2)
def fonk4(b13):
    b3 = []
    b4 = []
    b5 = {}
    for subdir, dirs, b14 in os.walk(b13):
        for file in b14:
            b6 = os.path.join(subdir, file)
            with open(b6, 'r', b7 = 'utf-8') as f:
                b8 = f.read().lower()
                b9 = b8.translate(str.maketrans('', '', string.punctuation))
                b5[file] = b9
                b3.append(b9)
                b4.append(file)
    b10 = TfidfVectorizer(tokenizer=preprocessing, stop_words='english')
    b11 = b10.fit_transform(b3)
    return b10, b11, b4
if b12 = = "__main__":
    b13 = 'C:\\Users\\Kapil Goyal\\Desktop\\nlp_assignment\\b14'
    tfidf_vectorizer, tfidf_matrix, b14 = fonk4(b13)
    print(f"Filenames: {b14}")
    print(f"TF-IDF Matrix: {tfidf_matrix.toarray()}")