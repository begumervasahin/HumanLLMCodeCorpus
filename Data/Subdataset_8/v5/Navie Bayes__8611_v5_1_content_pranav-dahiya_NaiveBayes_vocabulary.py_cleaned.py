import glob
import pickle
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import numpy as np
class VocabularyExtractor:
    def __init__(self):
        pass
    def extract_vocabulary(self, folder):
        files = glob.glob(folder + "*.txt")
        vocabulary = {}
        for filename in files:
            with open(filename) as f:
                text = f.readlines()
                for line in text:
                    words = word_tokenize(line)
                    for word in words:
                        word = word.lower()
                        if word in vocabulary:
                            vocabulary[word] += 1
                        else:
                            vocabulary[word] = 1
        vocabulary.pop("", None)
        return vocabulary
    def merge_vocabulary(self, old_vocab, new_vocab):
        for word, count in new_vocab.items():
            if word in old_vocab:
                old_vocab[word] += count
            else:
                old_vocab[word] = count
        return old_vocab
    def stop_word_removal(self, vocabulary):
        stop_words = set(stopwords.words('english'))
        for word in stop_words:
            vocabulary.pop(word, None)
        return vocabulary
    def lemmatize(self, vocabulary):
        lemmatizer = WordNetLemmatizer()
        for word in list(vocabulary.keys()):
            lemmatized_word = lemmatizer.lemmatize(word)
            if lemmatized_word != word:
                try:
                    vocabulary[lemmatized_word] += vocabulary[word]
                except KeyError:
                    pass
                vocabulary.pop(word)
        return vocabulary
    def threshold(self, vocabulary, percentile):
        lower_bound = np.percentile(list(vocabulary.values()), percentile)
        upper_bound = np.percentile(list(vocabulary.values()), 100 - percentile)
        vocabulary = {key: value for key, value in vocabulary.items() if lower_bound < value < upper_bound}
        return vocabulary
if __name__ == '__main__':
    extractor = VocabularyExtractor()
    vocabulary = {}
    for i in range(1, 11):
        vocabulary = extractor.merge_vocabulary(vocabulary, extractor.extract_vocabulary("lingspam/part" + str(i) + "/"))
    with open("vocabulary1.pickle", "wb") as f:
        pickle.dump(vocabulary, f)
    vocabulary = extractor.stop_word_removal(vocabulary)
    with open("vocabulary2.pickle", "wb") as f:
        pickle.dump(vocabulary, f)
    vocabulary = extractor.lemmatize(vocabulary)
    with open("vocabulary3.pickle", "wb") as f:
        pickle.dump(vocabulary, f)
    vocabulary = extractor.threshold(vocabulary, 2)
    with open("vocabulary4.pickle", "wb") as f:
        pickle.dump(vocabulary, f)