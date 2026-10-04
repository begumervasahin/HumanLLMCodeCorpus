import glob
import pickle
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import numpy as np
def extract_vocabulary(folder):
    files = glob.glob(f"{folder}*.txt")
    vocabulary = {}
    for filename in files:
        with open(filename, 'r') as f:
            text = f.readlines()
            for line in text:
                words = word_tokenize(line)
                for word in words:
                    word = word.lower()
                    vocabulary[word] = vocabulary.get(word, 0) + 1
    vocabulary.pop("", None)
    return vocabulary
def merge_vocabulary(old_vocab, new_vocab):
    for word, freq in new_vocab.items():
        old_vocab[word] = old_vocab.get(word, 0) + freq
    return old_vocab
def stop_word_removal(vocabulary):
    stop_words = set(stopwords.words('english'))
    for word in stop_words:
        vocabulary.pop(word, None)
    return vocabulary
def lemmatize(vocabulary):
    lemmatizer = WordNetLemmatizer()
    for word in list(vocabulary.keys()):
        lemmatized_word = lemmatizer.lemmatize(word)
        if lemmatized_word != word:
            vocabulary[lemmatized_word] = vocabulary.get(lemmatized_word, 0) + vocabulary[word]
            vocabulary.pop(word)
    return vocabulary
def threshold(vocabulary, percentile):
    values = np.fromiter(vocabulary.values(), dtype=float)
    lower_bound = np.percentile(values, percentile)
    upper_bound = np.percentile(values, 100 - percentile)
    print(f"Lower bound: {lower_bound}, Upper bound: {upper_bound}")
    return {key: value for key, value in vocabulary.items() if lower_bound < value < upper_bound}
def main():
    vocabulary = {}
    for i in range(1, 11):
        part_vocab = extract_vocabulary(f"lingspam/part{i}/")
        vocabulary = merge_vocabulary(vocabulary, part_vocab)
    with open("vocabulary1.pickle", "wb") as f:
        pickle.dump(vocabulary, f)
    vocabulary = stop_word_removal(vocabulary)
    with open("vocabulary2.pickle", "wb") as f:
        pickle.dump(vocabulary, f)
    vocabulary = lemmatize(vocabulary)
    with open("vocabulary3.pickle", "wb") as f:
        pickle.dump(vocabulary, f)
    vocabulary = threshold(vocabulary, 2)
    with open("vocabulary4.pickle", "wb") as f:
        pickle.dump(vocabulary, f)
if __name__ == '__main__':
    main()