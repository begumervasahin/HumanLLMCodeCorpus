import nltk
from nltk.probability import FreqDist
import Preprocessing
import yaml
b1 = Preprocessing
b2 = open('b3.json').read()
b3 = yaml.safe_load(b2)
b4 = [(item[3], item[5]) for item in b3]
b5 = []
for words, sentiment in b4:
    b6 = [word.lower() for word in words.split() if len(word) >= 3]
    b5.append((b6, sentiment))
def fonk1(b5):
    b7 = []
    for words, _ in b5:
        b7.extend(words)
    return b7
def fonk2(b8):
    b8 = FreqDist(b8)
    return b8.keys()
def fonk3(document):
    b9 = set(document)
    b10 = {}
    for word in b12:
        b10['contains(%s)' % word] = (word in b9)
    return b10
b11 = [
    "Buku rujukan kurang jelas mau pakai yang mana",
    "Penyampaian materi terlalu lemah lembut",
    "saya senang dengan pembelajaran ini",
    "saya suka dengan pembelajaran fismod karena tidak terpacu rumus"
]
b12 = fonk2(fonk1(b5))
b13 = nltk.classify.apply_features(extract_features, b5)
b14 = nltk.NaiveBayesClassifier.train(b13)
print(b14.show_most_informative_features(32))
for test in b11:
    print(test, b14.classify(fonk3(test.split())))