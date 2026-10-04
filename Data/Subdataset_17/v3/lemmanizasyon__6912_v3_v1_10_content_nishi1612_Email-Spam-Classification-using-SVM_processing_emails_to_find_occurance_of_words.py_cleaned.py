import os
import string
import numpy as np
import pandas as pd
from time import time
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
def load_words_list(file_path):
    df = pd.read_csv(file_path)
    return df['word'].tolist()
def write_headers(file_path, headers):
    with open(file_path, "w") as file:
        file.write(','.join(headers) + ',output\n')
def process_email_file(file_path, words, lmtzr, stop_words):
    word_freq = np.zeros(len(words))
    with open(file_path, "r", encoding='utf-8', errors='ignore') as file:
        for word in file.read().split():
            word = lmtzr.lemmatize(word.lower())
            if word in stop_words or word in string.punctuation or len(word) <= 2 or word.isdigit():
                continue
            if word in words:
                word_freq[words.index(word)] += 1
    return word_freq
def determine_output_label(file_name):
    return "1" if len(file_name) == 71 else "-1"
def append_to_csv(file_path, word_freq, output_label):
    with open(file_path, "a") as file:
        file.write(','.join(map(str, map(int, word_freq))) + ',')
        file.write(output_label + '\n')
def main():
    start_time = time()
    words = load_words_list('wordslist.csv')
    lmtzr = WordNetLemmatizer()
    stop_words = set(stopwords.words('english'))
    directory_path = "emails/"
    directory = os.fsencode(directory_path)
    write_headers("frequency.csv", words)
    processed_count = 0
    for file in os.listdir(directory):
        file_name = os.fsdecode(file)
        file_path = os.path.join(directory_path, file_name)
        processed_count += 1
        word_freq = process_email_file(file_path, words, lmtzr, stop_words)
        output_label = determine_output_label(file_name)
        append_to_csv("frequency.csv", word_freq, output_label)
        if processed_count % 100 == 0:
            print(f"Processed {processed_count} files")
    elapsed_time = round(time() - start_time, 2)
    print(f"Time (in seconds) to process the entire dataset: {elapsed_time}")
if __name__ == "__main__":
    main()