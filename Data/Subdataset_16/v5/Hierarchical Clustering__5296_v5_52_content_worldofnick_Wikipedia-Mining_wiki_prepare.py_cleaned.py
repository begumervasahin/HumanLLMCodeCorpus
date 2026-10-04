import nltk
from nltk.corpus import stopwords
from nltk import word_tokenize, ngrams
from sklearn.feature_extraction.b14 import CountVectorizer, TfidfTransformer
import glob
import os
nltk.download('punkt')
nltk.download('stopwords')
def fonk1(b14, b11):
    b1 = word_tokenize(b14)
    b2 = {' '.join(gram) for gram in ngrams(b1, b11)}
    return b2
def fonk2(b14, b3 = (3, 3)):
    b1 = word_tokenize(b14)
    b4 = set(stopwords.words("english"))
    b5 = [word for word in b1 if word.lower() not in b4]
    b6 = CountVectorizer(b3=b3)
    b7 = b6.fit_transform([' '.join(b5)])
    b8 = TfidfTransformer()
    b9 = b8.fit_transform(b7)
    return b9.toarray()
def fonk3(b2, article_name):
    b10 = f'{article_name}_kgrams.txt'
    with open(b10, "w") as f:
        f.write(",".join(b2))
def fonk4(file_pattern, b11 = 3):
    b12 = glob.glob(file_pattern)
    for filepath in b12:
        with open(filepath, 'r', b13 = 'utf-8') as file:
            b14 = file.read()
            b2 = fonk1(b14, b11)
            b15 = fonk2(b14, b3=(b11, b11))
            b16 = os.path.splitext(os.path.basename(filepath))[0]
            fonk3(b2, b16)
if b17 = = "__main__":
    fonk4('/somePath/*.txt', b11 = 3)