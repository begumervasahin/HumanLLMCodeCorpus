import os
import string
import numpy as np
import pandas as pd
from time import time
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
df = pd.read_csv('wordslist.csv', header=0)
words = df['word']
lemmatizer = WordNetLemmatizer()
input_directory = "emails/"
output_file_path = "frequency.csv"
with open(output_file_path, "w+") as output_file:
    output_file.write(','.join(map(str, words)) + ',output\n')
start_time = time()
file_count = 0
for file_name in os.listdir(input_directory):
    file_name = file_name.decode("utf-8")
    full_file_path = os.path.join(os.getcwd(), input_directory, file_name)
    with open(full_file_path, "r", encoding='utf-8', errors='ignore') as file_reading:
        words_list_array = np.zeros(words.size)
        for word in file_reading.read().split():
            word = lemmatizer.lemmatize(word.lower())
            if word in stopwords.words('english') or word in string.punctuation or len(word) <= 2 or word.isdigit():
                continue
            for i, target_word in enumerate(words):
                if target_word == word:
                    words_list_array[i] += 1
                    break
        with open(output_file_path, "a") as output_file:
            output_file.write(','.join(map(str, words_list_array.astype(int))))
            if len(file_name) == 68:
                output_file.write(", -1\n")
            elif len(file_name) == 71:
                output_file.write(", 1\n")
    file_count += 1
    if file_count % 100 == 0:
        print("Processed {} files".format(file_count))
print("Time taken to process {} files: {:.2f} seconds".format(file_count, time() - start_time))