import nltk
from nltk.probability import FreqDist
import Preprocessing
import yaml
pp = Preprocessing
with open('komentar.json') as file:
    komentar = yaml.safe_load(file)
data_komentar = [(item[3], item[5]) for item in komentar]
def preprocess_data(data):
    preprocessed_data = []
    for words, sentiment in data:
        words_filtered = [word.lower() for word in words.split() if len(word) >= 3]
        preprocessed_data.append((words_filtered, sentiment))
    return preprocessed_data
def get_all_words(data):
    all_words = []
    for words, _ in data:
        all_words.extend(words)
    return all_words
def get_word_features(wordlist):
    word_freq = FreqDist(wordlist)
    return word_freq.keys()
def extract_features(document, word_features):
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
komentars = preprocess_data(data_komentar)
word_features = get_word_features(get_all_words(komentars))
training_set = nltk.classify.apply_features(lambda doc: extract_features(doc, word_features), komentars)
classifier = nltk.NaiveBayesClassifier.train(training_set)
print(classifier.show_most_informative_features(32))
for test in test_komentar:
    print(test, classifier.classify(extract_features(test.split(), word_features)))