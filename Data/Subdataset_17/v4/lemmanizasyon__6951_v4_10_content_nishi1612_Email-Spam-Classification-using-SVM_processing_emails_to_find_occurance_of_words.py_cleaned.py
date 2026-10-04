import os
import string
import numpy as np
import pandas as pd
from time import time
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
start_time = time()
df = pd.read_csv('wordslist.csv')
words = df['word']
lmtzr = WordNetLemmatizer()
directory_in_str = "emails/"
directory = os.fsencode(directory_in_str)
with open("frequency.csv", "w") as f:
    f.write(','.join(words) + ',output\n')
k = 0
for file in os.listdir(directory):
    file_name = os.path.join(directory_in_str, file.decode("utf-8"))
    with open(file_name, "r", encoding='utf-8', errors='ignore') as file_reading:
        words_list_array = np.zeros(words.size)
        for word in file_reading.read().split():
            word = lmtzr.lemmatize(word.lower())
            if (word in stopwords.words('english') or
                word in string.punctuation or
                len(word) <= 2 or
                word.isdigit()):
                continue
            if word in words.values:
                words_list_array[words[words == word].index[0]] += 1
    with open("frequency.csv", "a") as f:
        f.write(','.join(map(str, map(int, words_list_array))) + ',')
        f.write("-1" if len(file_name) == 68 else "1")
        f.write('\n')
    k += 1
    if k % 100 == 0:
        print(f"Processed {k} files")
print(f"Time (in seconds) to process dataset: {round(time() - start_time, 2)}")