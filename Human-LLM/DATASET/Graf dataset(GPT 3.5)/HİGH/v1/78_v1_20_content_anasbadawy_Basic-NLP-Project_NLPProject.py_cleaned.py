import csv
import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures
from string import punctuation
from collections import Counter
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
with open('rev.csv', 'r') as csv_file:
    b1 = csv.reader(csv_file)
    next(b1)
    b2 = [line[3] for line in b1]
b3 = PorterStemmer()
b4 = set(stopwords.b12('english'))
b5 = [word_tokenize(review) for review in b2]
b6 = [[b3.stem(word) for word in tokens] for tokens in b5]
b7 = [[word for word in stems if word not in b4] for stems in b6]
def fonk1(text):
    b8 = word_tokenize(text)
    b9 = [word for word in b8 if word not in b4 and word not in punctuation]
    return b9
b10 = ' '.join(b2)
b11 = Counter(fonk1(b10)).most_common(10)
def fonk2(text, n):
    b12 = fonk1(text)
    return list(zip(*[b12[i:] for i in range(n)]))
b13 = fonk2(b10, 2)
b14 = Counter(b13).most_common(10)
def fonk3(b13):
    b15 = BigramAssocMeasures()
    b16 = BigramCollocationFinder.from_documents([b13])
    b17 = b16.score_ngrams(b15.likelihood_ratio)
    return b17
b18 = fonk3(b13)
b19 = [bigram for bigram, score in b18]
def fonk4(text):
    b20 = nltk.pos_tag(word_tokenize(text))
    b21 = nltk.FreqDist(b23 for (word, b23) in b20)
    return b21.most_common()
b22 = fonk4(b10)
def fonk5(text, pos_tag):
    b20 = nltk.pos_tag(word_tokenize(text))
    return [word for word, b23 in b20 if b23 = = pos_tag]
b24 = fonk5(b10, 'PRP')
print("Most Common Words:", b11)
print("Most Common Bigrams:", b14)
print("Scored Bigrams:", b19)
print("Most Common POS Tags:", b22)
print("Pronouns:", b24)