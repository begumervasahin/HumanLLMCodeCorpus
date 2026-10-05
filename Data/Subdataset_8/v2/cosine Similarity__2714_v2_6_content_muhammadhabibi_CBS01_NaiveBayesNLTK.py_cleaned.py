import nltk
from nltk.probability import FreqDist
import Preprocessing
import yaml
pp = Preprocessing
with open('komentar.json') as file:
    komentar = yaml.safe_load(file)
data_komentar = [(item[3], item[5]) for item in komentar]
komentars = []
for words, sentiment in data_komentar:
    words_filtered = [word.lower() for word in words.split() if len(word) >= 3]
    komentars.append((words_filtered, sentiment))
def get_words_in_komentar(komentars):
    all_words = []
    for words, _ in komentars:
        all_words.extend(words)
    return all_words
def get_word_features(wordlist):
    wordlist = FreqDist(wordlist)
    return wordlist.keys()
def extract_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features
test_komentar = [
    "Buku rujukan kurang jelas mau pakai yang mana",
    "Penyampaian materi terlalu lemah lembut",
    "saya senang dengan pembelajaran ini",
    "saya suka dengan pembelajaran fismod karena tidak terpacu rumus"
]
word_features = get_word_features(get_words_in_komentar(komentars))
training_set = nltk.classify.apply_features(extract_features, komentars)
classifier = nltk.NaiveBayesClassifier.train(training_set)
print(classifier.show_most_informative_features(32))
for test in test_komentar:
    print(test, classifier.classify(extract_features(test.split())))