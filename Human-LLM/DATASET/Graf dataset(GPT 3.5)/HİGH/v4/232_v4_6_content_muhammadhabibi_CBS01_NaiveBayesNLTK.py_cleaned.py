import nltk
import Preprocessing
import yaml
b1 = Preprocessing
with open('b2.json') as file:
    b2 = yaml.safe_load(file)
b3 = [(item[3], item[5]) for item in b2]
b4 = []
for words, sentiment in b3:
    b5 = [word.lower() for word in words.split() if len(word) >= 3]
    b4.append((b5, sentiment))
def fonk1(b4):
    b6 = []
    for words, _ in b4:
        b6.extend(words)
    return b6
def fonk2(wordlist):
    b7 = nltk.FreqDist(wordlist)
    return b7.keys()
def fonk3(document):
    b8 = set(document)
    b9 = {}
    for word in b11:
        b9['contains(%s)' % word] = (word in b8)
    return b9
b10 = [
    "Buku rujukan kurang jelas mau pakai yang mana",
    "Penyampaian materi terlalu lemah lembut",
    "saya senang dengan pembelajaran ini",
    "saya suka dengan pembelajaran fismod karena tidak terpacu rumus"
]
b11 = fonk2(fonk1(b4))
b12 = nltk.classify.apply_features(extract_features, b4)
b13 = nltk.NaiveBayesClassifier.train(b12)
print(b13.show_most_informative_features(32))
for test in b10:
    print(test, b13.classify(fonk3(test.split())))