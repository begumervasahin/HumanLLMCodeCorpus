import os
import string
import numpy as np
import pandas as pd
from time import time
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
start_time = time()
df = pd.read_csv('wordslist.csv')
words = df['word'].tolist()
lmtzr = WordNetLemmatizer()
directory_path = "emails/"
directory = os.fsencode(directory_path)
with open("frequency.csv", "w") as freq_file:
    header = ','.join(words) + ',output\n'
    freq_file.write(header)
processed_count = 0
for file in os.listdir(directory):
    file_name = os.fsdecode(file)
    file_path = os.path.join(directory_path, file_name)
    processed_count += 1
    with open(file_path, "r", encoding='utf-8', errors='ignore') as email_file:
        words_list_array = np.zeros(len(words))
        for word in email_file.read().split():
            word = lmtzr.lemmatize(word.lower())
            if word in stopwords.words('english') or word in string.punctuation or len(word) <= 2 or word.isdigit():
                continue
            if word in words:
                words_list_array[words.index(word)] += 1
        with open("frequency.csv", "a") as freq_file:
            freq_file.write(','.join(map(str, map(int, words_list_array))) + ',')
            output_label = "1" if len(file_name) == 71 else "-1"
            freq_file.write(output_label + '\n')
    if processed_count % 100 == 0:
        print(f"Processed {processed_count} files")
elapsed_time = round(time() - start_time, 2)
print(f"Time (in seconds) to process the entire dataset: {elapsed_time}")