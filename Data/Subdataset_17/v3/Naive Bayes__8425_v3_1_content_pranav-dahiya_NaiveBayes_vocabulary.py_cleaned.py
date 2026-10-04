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
def remove_stop_words(vocabulary):
    stop_words = set(stopwords.words('english'))
    filtered_vocab = {word: freq for word, freq in vocabulary.items() if word not in stop_words}
    return filtered_vocab
def lemmatize_vocabulary(vocabulary):
    lemmatizer = WordNetLemmatizer()
    lemmatized_vocab = {}
    for word, freq in vocabulary.items():
        lemmatized_word = lemmatizer.lemmatize(word)
        if lemmatized_word in lemmatized_vocab:
            lemmatized_vocab[lemmatized_word] += freq
        else:
            lemmatized_vocab[lemmatized_word] = freq
    return lemmatized_vocab
def apply_threshold(vocabulary, percentile):
    values = np.fromiter(vocabulary.values(), dtype=float)
    lower_bound = np.percentile(values, percentile)
    upper_bound = np.percentile(values, 100 - percentile)
    print(f"Lower bound: {lower_bound}, Upper bound: {upper_bound}")
    filtered_vocab = {word: freq for word, freq in vocabulary.items() if lower_bound < freq < upper_bound}
    return filtered_vocab
def main():
    vocabulary = {}
    for i in range(1, 11):
        part_vocab = extract_vocabulary(f"lingspam/part{i}/")
        vocabulary = merge_vocabulary(vocabulary, part_vocab)
    with open("vocabulary1.pickle", "wb") as f:
        pickle.dump(vocabulary, f)
    vocabulary = remove_stop_words(vocabulary)
    with open("vocabulary2.pickle", "wb") as f:
        pickle.dump(vocabulary, f)
    vocabulary = lemmatize_vocabulary(vocabulary)
    with open("vocabulary3.pickle", "wb") as f:
        pickle.dump(vocabulary, f)
    vocabulary = apply_threshold(vocabulary, 2)
    with open("vocabulary4.pickle", "wb") as f:
        pickle.dump(vocabulary, f)
if __name__ == '__main__':
    main()