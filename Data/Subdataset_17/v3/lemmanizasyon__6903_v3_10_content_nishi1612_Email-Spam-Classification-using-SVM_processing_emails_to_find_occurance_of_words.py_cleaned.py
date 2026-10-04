import os
import string
import numpy as np
import pandas as pd
from time import time
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
def load_words(words_csv):
    df = pd.read_csv(words_csv, header=0)
    return df['word'], set(df['word'])
def initialize_output_csv(output_csv, words):
    with open(output_csv, "w") as f:
        f.write(','.join(words) + ',output\n')
def process_email_file(file_path, words, words_set, lemmatizer):
    words_list_array = np.zeros(len(words))
    with open(file_path, "r", encoding='utf-8', errors='ignore') as file:
        content = file.read().split()
        for word in content:
            word = lemmatizer.lemmatize(word.lower())
            if word in stopwords.words('english') or word in string.punctuation or len(word) <= 2 or word.isdigit():
                continue
            if word in words_set:
                index = words.get_loc(word)
                words_list_array[index] += 1
    return words_list_array
def append_frequencies_to_csv(output_csv, words_list_array, file_length):
    with open(output_csv, "a") as f:
        f.write(','.join(map(str, map(int, words_list_array))) + ',')
        if file_length == 68:
            f.write("-1")
        elif file_length == 71:
            f.write("1")
        f.write('\n')
def process_emails(words_csv, emails_dir, output_csv):
    start_time = time()
    words, words_set = load_words(words_csv)
    lemmatizer = WordNetLemmatizer()
    initialize_output_csv(output_csv, words)
    processed_count = 0
    for file in os.listdir(os.fsencode(emails_dir)):
        file_path = os.path.join(emails_dir, file.decode("utf-8"))
        processed_count += 1
        words_list_array = process_email_file(file_path, words, words_set, lemmatizer)
        append_frequencies_to_csv(output_csv, words_list_array, len(file_path))
        if processed_count % 100 == 0:
            print(f"Processed {processed_count} files")
    elapsed_time = round(time() - start_time, 2)
    print(f"Time (in seconds) to process all emails: {elapsed_time}")
words_csv = 'wordslist.csv'
emails_dir = 'emails/'
output_csv = 'frequency.csv'
process_emails(words_csv, emails_dir, output_csv)