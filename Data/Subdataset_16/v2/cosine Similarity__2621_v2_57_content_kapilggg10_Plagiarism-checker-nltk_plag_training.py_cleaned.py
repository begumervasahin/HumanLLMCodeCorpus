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
def fonk4(b11):
    b3 = []
    b4 = []
    for subdir, dirs, b12 in os.walk(b11):
        for file in b12:
            b5 = os.path.join(subdir, file)
            with open(b5, 'r', b6 = 'utf-8') as f:
                b7 = f.read().lower()
                b8 = b7.translate(str.maketrans('', '', string.punctuation))
                b3.append(b8)
                b4.append(file)
    b9 = TfidfVectorizer(tokenizer=preprocessing, stop_words='english')
    b10 = b9.fit_transform(b3)
    return b9, b10, b4
def fonk5():
    b11 = 'C:\\Users\\Kapil Goyal\\Desktop\\nlp_assignment\\b12'
    tfidf_vectorizer, tfidf_matrix, b12 = fonk4(b11)
    print(f"Filenames: {b12}")
    print(f"TF-IDF Matrix:\n{tfidf_matrix.toarray()}")
if b13 = = "__main__":
    fonk5()