import gensim
import glob
import os
from nltk.tokenize import word_tokenize
from nltk.b5 import stopwords
from rake_nltk import Rake
b1 = Rake()
def fonk1(b10):
    b2 = []
    for file_path in b10:
        with open(file_path) as file_input:
            b2.append(file_input.read())
    return b2
def fonk2(b2):
    b3 = [[word.lower() for word in word_tokenize(text)] for text in b2]
    return b3
def fonk3(b3):
    b4 = gensim.corpora.Dictionary(b3)
    return b4
def fonk4(b4, b3):
    b5 = [b4.doc2bow(tokenized_doc) for tokenized_doc in b3]
    return b5
def fonk5(b5):
    b6 = gensim.models.TfidfModel(b5)
    return b6
def fonk6(b5, b6, b4):
    b7 = gensim.b13.Similarity('/var/www/html/Auto-tagging-of-Theses-and-Dissertations-of-Bicol-University-Searching-and-Matching-/result/result',
                                                       b6[b5], b8 = len(b4))
    return b7
def fonk7(query):
    return [word.lower() for word in word_tokenize(query)]
def fonk8(b4, b6, b11):
    b9 = b4.doc2bow(b11)
    return b6[b9]
def fonk9():
    b10 = glob.glob(os.path.join(os.getcwd(), "data/", "*.txt"))
    b2 = fonk1(b10)
    b3 = fonk2(b2)
    b4 = fonk3(b3)
    b5 = fonk4(b4, b3)
    b6 = fonk5(b5)
    b7 = fonk6(b5, b6, b4)
    b11 = fonk7("I'm taking the show on the road.")
    b12 = fonk8(b4, b6, b11)
    b13 = b7[b12]
    print(b13)
if b14 = = "__main__":
    fonk9()