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
                    if word:
                        vocabulary[word] = vocabulary.get(word, 0) + 1
    return vocabulary
def merge_vocabulary(old_vocab, new_vocab):
    for word, count in new_vocab.items():
        old_vocab[word] = old_vocab.get(word, 0) + count
    return old_vocab
def remove_stop_words(vocabulary):
    stop_words = set(stopwords.words('english'))
    for word in stop_words:
        vocabulary.pop(word, None)
    return vocabulary
def lemmatize_vocabulary(vocabulary):
    lemmatizer = WordNetLemmatizer()
    lemmatized_vocabulary = {}
    for word, count in vocabulary.items():
        lemmatized_word = lemmatizer.lemmatize(word)
        if lemmatized_word in lemmatized_vocabulary:
            lemmatized_vocabulary[lemmatized_word] += count
        else:
            lemmatized_vocabulary[lemmatized_word] = count
    return lemmatized_vocabulary
def apply_threshold(vocabulary, percentile):
    values = np.array(list(vocabulary.values()))
    lower_bound = np.percentile(values, percentile)
    upper_bound = np.percentile(values, 100 - percentile)
    print(f"Lower bound: {lower_bound}, Upper bound: {upper_bound}")
    filtered_vocabulary = {word: count for word, count in vocabulary.items() if lower_bound < count < upper_bound}
    return filtered_vocabulary
def save_vocabulary(vocabulary, filename):
    with open(filename, "wb") as file:
        pickle.dump(vocabulary, file)
def main():
    vocabulary = {}
    for i in range(1, 11):
        folder = f"lingspam/part{i}/"
        vocabulary = merge_vocabulary(vocabulary, extract_vocabulary(folder))
    save_vocabulary(vocabulary, "vocabulary1.pickle")
    vocabulary = remove_stop_words(vocabulary)
    save_vocabulary(vocabulary, "vocabulary2.pickle")
    vocabulary = lemmatize_vocabulary(vocabulary)
    save_vocabulary(vocabulary, "vocabulary3.pickle")
    vocabulary = apply_threshold(vocabulary, 2)
    save_vocabulary(vocabulary, "vocabulary4.pickle")
if __name__ == '__main__':
    main()