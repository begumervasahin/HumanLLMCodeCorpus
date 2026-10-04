import os
import string
import numpy as np
import pandas as pd
from time import time
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
start_time = time()
words_df = pd.read_csv('wordslist.csv', header=0)
words = words_df['word']
lemmatizer = WordNetLemmatizer()
emails_directory = "emails/"
encoded_directory = os.fsencode(emails_directory)
with open("frequency.csv", "w+") as freq_file:
    freq_file.write(','.join(words) + ',output\n')
file_count = 0
for file in os.listdir(encoded_directory):
    file_name = os.fsdecode(file)
    full_file_path = os.path.join(os.getcwd(), 'emails', file_name)
    file_count += 1
    with open(full_file_path, "r", encoding='utf-8', errors='ignore') as email_file:
        word_frequencies = np.zeros(len(words))
        for word in email_file.read().split():
            word = lemmatizer.lemmatize(word.lower())
            if word in stopwords.words('english') or word in string.punctuation or len(word) <= 2 or word.isdigit():
                continue
            if word in words.values:
                word_index = words[words == word].index[0]
                word_frequencies[word_index] += 1
        with open("frequency.csv", "a") as freq_file:
            freq_file.write(','.join(map(str, word_frequencies.astype(int))) + ',')
            if len(full_file_path) == 68:
                freq_file.write("-1")
            elif len(full_file_path) == 71:
                freq_file.write("1")
            freq_file.write('\n')
    if file_count % 100 == 0:
        print(f"Processed {file_count} files")
print(f"Time (in seconds) to process the dataset: {round(time() - start_time, 2)}")