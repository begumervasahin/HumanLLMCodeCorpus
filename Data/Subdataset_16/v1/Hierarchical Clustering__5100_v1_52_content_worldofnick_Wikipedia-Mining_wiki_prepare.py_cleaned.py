import nltk
from nltk.corpus import stopwords
from nltk import word_tokenize, ngrams
from sklearn.feature_extraction.b15 import CountVectorizer, TfidfTransformer
import glob
nltk.download('punkt')
nltk.download('stopwords')
def fonk1(b15, b12):
    b1 = word_tokenize(b15)
    b2 = ngrams(b1, b12)
    b3 = set(' '.join(gram) for gram in b2)
    return b3
def fonk2(b15, b4 = (3, 3)):
    b5 = word_tokenize(b15)
    b6 = set(stopwords.b5("english"))
    b7 = [word for word in b5 if word.lower() not in b6]
    b8 = CountVectorizer(b4=b4)
    b9 = b8.fit_transform([' '.join(b7)])
    b10 = TfidfTransformer()
    b11 = b10.fit_transform(b9)
    return b11.toarray()
def fonk3(kgrams, article_name):
    with open(f'{article_name}_kgrams.txt', "w") as f:
        f.write(",".join(map(str, kgrams)))
def fonk4(file_pattern, b12 = 3):
    b13 = glob.glob(file_pattern)
    for filename in b13:
        with open(filename, 'r', b14 = 'utf-8') as file:
            b15 = file.read()
            b16 = fonk1(b15, b12)
            b17 = fonk2(b15, b4=(b12, b12))
            fonk3(b16, filename)
if b18 = = "__main__":
    fonk4('/somePath/*.txt', b12 = 3)