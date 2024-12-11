import nltk
from nltk.probability import FreqDist
import Preprocessing
import yaml
b1 = Preprocessing
with open('b2.json') as file:
    b2 = yaml.safe_load(file)
b3 = [(item[3], item[5]) for item in b2]
def fonk1(data):
    b4 = []
    for words, sentiment in data:
        b5 = [word.lower() for word in words.split() if len(word) >= 3]
        b4.append((b5, sentiment))
    return b4
def fonk2(data):
    b6 = []
    for words, _ in data:
        b6.extend(words)
    return b6
def fonk3(wordlist):
    b7 = FreqDist(wordlist)
    return b7.keys()
def fonk4(document, b12):
    b8 = set(document)
    b9 = {}
    for word in b12:
        b9['contains(%s)' % word] = (word in b8)
    return b9
b10 = [
    "Buku rujukan kurang jelas mau pakai yang mana",
    "Penyampaian materi terlalu lemah lembut",
    "saya senang dengan pembelajaran ini",
    "saya suka dengan pembelajaran fismod karena tidak terpacu rumus"
]
b11 = fonk1(b3)
b12 = fonk3(fonk2(b11))
b13 = nltk.classify.apply_features(lambda doc: fonk4(doc, b12), b11)
b14 = nltk.NaiveBayesClassifier.train(b13)
print(b14.show_most_informative_features(32))
for test in b10:
    print(test, b14.classify(fonk4(test.split(), b12)))