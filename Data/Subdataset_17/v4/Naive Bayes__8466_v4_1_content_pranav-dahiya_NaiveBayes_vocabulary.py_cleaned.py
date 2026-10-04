import glob
import pickle
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import numpy as np
def extract_vocabulary(folder):
    files = glob.glob(folder + "*.txt")
    vocabulary = {}
    for filename in files:
        with open(filename, 'r') as file:
            text = file.readlines()
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
def merge_vocabulary(old_vocab, new_vocab):
    for word, count in new_vocab.items():
        if word in old_vocab:
            old_vocab[word] += count
        else:
            old_vocab[word] = count
    return old_vocab
def remove_stop_words(vocabulary):
    stop_words = set(stopwords.words('english'))
    for word in stop_words:
        vocabulary.pop(word, None)
    return vocabulary
def lemmatize_vocabulary(vocabulary):
    lemmatizer = WordNetLemmatizer()
    lemmatized_vocabulary = {}
    for word in list(vocabulary.keys()):
        lemmatized_word = lemmatizer.lemmatize(word)
        if lemmatized_word != word:
            if lemmatized_word in lemmatized_vocabulary:
                lemmatized_vocabulary[lemmatized_word] += vocabulary[word]
            else:
                lemmatized_vocabulary[lemmatized_word] = vocabulary[word]
        else:
            lemmatized_vocabulary[word] = vocabulary[word]
    return lemmatized_vocabulary
def apply_threshold(vocabulary, percentile):
    values = np.fromiter(vocabulary.values(), dtype=float)
    lower_bound = np.percentile(values, percentile)
    upper_bound = np.percentile(values, 100 - percentile)
    print(f"Lower bound: {lower_bound}, Upper bound: {upper_bound}")
    filtered_vocabulary = {key: value for key, value in vocabulary.items() if lower_bound < value < upper_bound}
    return filtered_vocabulary
if __name__ == '__main__':
    vocabulary = {}
    for i in range(1, 11):
        folder = f"lingspam/part{i}/"
        vocabulary = merge_vocabulary(vocabulary, extract_vocabulary(folder))
    with open("vocabulary1.pickle", "wb") as file:
        pickle.dump(vocabulary, file)
    vocabulary = remove_stop_words(vocabulary)
    with open("vocabulary2.pickle", "wb") as file:
        pickle.dump(vocabulary, file)
    vocabulary = lemmatize_vocabulary(vocabulary)
    with open("vocabulary3.pickle", "wb") as file:
        pickle.dump(vocabulary, file)
    vocabulary = apply_threshold(vocabulary, 2)
    with open("vocabulary4.pickle", "wb") as file:
        pickle.dump(vocabulary, file)