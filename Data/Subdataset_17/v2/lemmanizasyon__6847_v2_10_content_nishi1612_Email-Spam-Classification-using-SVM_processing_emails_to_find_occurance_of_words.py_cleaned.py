import os
import string
import numpy as np
import pandas as pd
from time import time
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
def process_emails(words_csv, emails_dir, output_csv):
    start_time = time()
    df = pd.read_csv(words_csv, header=0)
    words = df['word']
    words_set = set(words)
    lemmatizer = WordNetLemmatizer()
    with open(output_csv, "w") as f:
        f.write(','.join(words) + ',output\n')
    directory = os.fsencode(emails_dir)
    processed_count = 0
    for file in os.listdir(directory):
        file_name = os.path.join(emails_dir, file.decode("utf-8"))
        processed_count += 1
        with open(file_name, "r", encoding='utf-8', errors='ignore') as file:
            words_list_array = np.zeros(len(words))
            content = file.read().split()
            for word in content:
                word = lemmatizer.lemmatize(word.lower())
                if word in stopwords.words('english') or word in string.punctuation or len(word) <= 2 or word.isdigit():
                    continue
                if word in words_set:
                    index = words.get_loc(word)
                    words_list_array[index] += 1
        with open(output_csv, "a") as f:
            f.write(','.join(map(str, map(int, words_list_array))) + ',')
            if len(file_name) == 68:
                f.write("-1")
            elif len(file_name) == 71:
                f.write("1")
            f.write('\n')
        if processed_count % 100 == 0:
            print(f"Processed {processed_count} files")
    elapsed_time = round(time() - start_time, 2)
    print(f"Time (in seconds) to process all emails: {elapsed_time}")
words_csv = 'wordslist.csv'
emails_dir = 'emails/'
output_csv = 'frequency.csv'
process_emails(words_csv, emails_dir, output_csv)