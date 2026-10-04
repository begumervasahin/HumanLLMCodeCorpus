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
    b3 = {' '.join(gram) for gram in b2}
    return b3
def fonk2(b15, b4 = (3, 3)):
    b1 = word_tokenize(b15)
    b5 = set(stopwords.words("english"))
    b6 = [word for word in b1 if word.lower() not in b5]
    b7 = CountVectorizer(b4=b4)
    b8 = b7.fit_transform([' '.join(b6)])
    b9 = TfidfTransformer()
    b10 = b9.fit_transform(b8)
    return b10.toarray()
def fonk3(kgrams, article_name):
    b11 = f'{article_name}_kgrams.txt'
    with open(b11, "w") as f:
        f.write(",".join(kgrams))
def fonk4(file_pattern, b12 = 3):
    b13 = glob.glob(file_pattern)
    for filepath in b13:
        with open(filepath, 'r', b14 = 'utf-8') as file:
            b15 = file.read()
            b16 = fonk1(b15, b12)
            fonk2(b15, b4 = (b12, b12))
            fonk3(b16, filepath)
if b17 = = "__main__":
    fonk4('/somePath/*.txt', b12 = 3)