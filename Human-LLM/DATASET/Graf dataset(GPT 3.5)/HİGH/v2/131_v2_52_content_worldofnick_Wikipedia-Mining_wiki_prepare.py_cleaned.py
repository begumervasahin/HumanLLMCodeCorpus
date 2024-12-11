import glob
import nltk
from nltk.corpus import stopwords
from nltk.util import ngrams
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
def fonk1(text, k):
    b1 = ngrams(text.split(), k)
    b2 = set()
    for gram in b1:
        b2.add(' '.join(gram))
    return b2
def fonk2(text):
    b3 = nltk.word_tokenize(text)
    b4 = set(stopwords.b3("english"))
    b5 = [word for word in b3 if word not in b4]
    b6 = CountVectorizer(ngram_range=(3, 3))
    b7 = b6.fit_transform(b5)
    b8 = TfidfTransformer()
    return b8.fit_transform(b7).toarray()
def fonk3(kgrams, file_name):
    with open(f'{file_name}_kgrams.txt', "w") as file:
        file.write(",".join(map(lambda x: str(x), kgrams)))
b9 = glob.glob('/somePath/*.txt')
for file_name in b9:
    with open(file_name) as file:
        b10 = fonk2(file.read())
        fonk3(b10, file_name)