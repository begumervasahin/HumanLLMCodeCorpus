from nltk.probability import ELEProbDist, FreqDist
import nltk
import Preprocessing
import json
import yaml
b1 = Preprocessing
b2 = open('b3.json').read()
b3 = yaml.safe_load(b2)
b4 = []
for i, komen in enumerate(b3):
	b5 = ()
	b6 = (b3[i][3])
	b7 = (b3[i][5])
	b5 = (b6,b7)
	b4.append(b5)
b8 = []
for (words, sentiment) in b4:
    b9 = [e.lower() for e in words.split() if len(e) >= 3]
    b8.append((b9, sentiment))
def fonk1(b8):
    b10 = []
    for (words, sentiment) in b8:
      b10.extend(words)
    return b10
def fonk2(b11):
    b11 = nltk.FreqDist(b11)
    b12 = b11.keys()
    return b12
def fonk3(document):
    b13 = set(document)
    b14 = {}
    for word in b12:
        b14['contains(%s)' % word] = (word in b13)
    return b14
b15 = []
b15.append("Buku rujukan kurang jelas mau pakai yang mana")
b15.append("Penyampaian materi terlalu lemah lembut")
b15.append("saya senang dengan pembelajaran ini")
b15.append("saya suka dengan pembelajaran fismod karena tidak terpacu rumus")
b12 = fonk2(fonk1(b8))
b16 = nltk.classify.apply_features(extract_features, b8)
b17 = nltk.NaiveBayesClassifier.train(b16)
print b17.show_most_informative_features(32)
for test in b15:
	print (test, b17.classify(fonk3(test.split())))