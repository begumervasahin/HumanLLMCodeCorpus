import os
import string
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.b7 import TfidfVectorizer
def fonk1(b7):
    return word_tokenize(b7)
def fonk2(b1, b2):
    return [b2.stem(token) for token in b1]
def fonk3(b7):
    b1 = fonk1(b7)
    b2 = PorterStemmer()
    return fonk2(b1, b2)
def fonk4(b10):
    b3 = []
    b4 = []
    for subdir, _, b11 in os.walk(b10):
        for file in b11:
            b5 = os.path.join(subdir, file)
            with open(b5, 'r', b6 = 'utf-8') as f:
                b7 = f.read().lower()
                b7 = b7.translate(str.maketrans('', '', string.punctuation))
                b3.append(b7)
                b4.append(file)
    return b3, b4
def fonk5(b10):
    b3, b4 = fonk4(b10)
    b8 = TfidfVectorizer(tokenizer=preprocessing, stop_words='english')
    b9 = b8.fit_transform(b3)
    return b8, b9, b4
def fonk6():
    b10 = 'C:\\Users\\Kapil Goyal\\Desktop\\nlp_assignment\\b11'
    b8, b9, b11 = fonk5(b10)
    print(f"Filenames: {b11}")
    print(f"TF-IDF Matrix:\n{b9.toarray()}")
if b12 = = "__main__":
    fonk6()