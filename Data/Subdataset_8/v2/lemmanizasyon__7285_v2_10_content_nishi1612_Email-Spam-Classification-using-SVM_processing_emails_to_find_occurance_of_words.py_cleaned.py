import os
import string
import numpy as np
import pandas as pd
from time import time
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
def read_word_list(filename):
    df = pd.read_csv(filename, header=0)
    return df['word']
def preprocess_word(word, lemmatizer, stopword_set):
    word = lemmatizer.lemmatize(word.lower())
    return word if word not in stopword_set and word not in string.punctuation and len(word) > 2 and not word.isdigit() else None
def process_email(file_path, words, lemmatizer, stopword_set):
    words_list_array = np.zeros(len(words))
    with open(file_path, "r", encoding='utf-8', errors='ignore') as file_reading:
        for word in file_reading.read().split():
            processed_word = preprocess_word(word, lemmatizer, stopword_set)
            if processed_word:
                for i, w in enumerate(words):
                    if w == processed_word:
                        words_list_array[i] += 1
                        break
    return words_list_array
def write_csv_header(filename, words):
    with open(filename, "w+") as f:
        f.write(','.join(map(str, words)) + ',output\n')
def main():
    start_time = time()
    words = read_word_list('wordslist.csv')
    lmtzr = WordNetLemmatizer()
    stopword_set = set(stopwords.words('english'))
    write_csv_header("frequency.csv", words)
    directory = os.fsencode("emails/")
    k = 0
    for file in os.listdir(directory):
        file = file.decode("utf-8")
        file_name = str(os.getcwd()) + '/emails/' + ''.join(c for c in file if c not in {'b', "'"})
        k += 1
        words_list_array = process_email(file_name, words, lmtzr, stopword_set)
        with open("frequency.csv", "a") as f:
            f.write(','.join(map(str, words_list_array)))
            f.write("-1" if len(file_name) == 68 else "1")
            f.write('\n')
        if k % 100 == 0:
            print("Done " + str(k))
    print("Time (in seconds) to segregate the entire dataset to form the input vector: " + str(round(time() - start_time, 2)))
if __name__ == "__main__":
    main()