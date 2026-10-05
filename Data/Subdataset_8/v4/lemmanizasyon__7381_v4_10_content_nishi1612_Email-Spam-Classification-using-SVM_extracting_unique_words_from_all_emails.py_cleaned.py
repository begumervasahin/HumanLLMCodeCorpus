import os
import nltk
import time
import string
import operator
import numpy as np
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
def text_cleanup(text):
    text_without_punctuation = [char for char in text if char not in string.punctuation]
    text_without_punctuation = ''.join(text_without_punctuation)
    text_without_stopwords = [word for word in text_without_punctuation.split() if word.lower() not in stopwords.words('english')]
    text_without_stopwords = ' '.join(text_without_stopwords)
    cleaned_text = [word.lower() for word in text_without_stopwords.split()]
    return cleaned_text
start_time = time.time()
lemmatizer = WordNetLemmatizer()
file_count = 0
word_count = {}
directory_path = "emails/"
directory = os.fsencode(directory_path)
for file in os.listdir(directory):
    file = file.decode("utf-8")
    file_path = os.path.join(os.getcwd(), 'emails', file)
    with open(file_path, "r", encoding='utf-8', errors='ignore') as file_reader:
        words = text_cleanup(file_reader.read())
        for word in words:
            if not word.isdigit() and len(word) > 2:
                word = lemmatizer.lemmatize(word)
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1
        file_count += 1
        if file_count % 100 == 0:
            print(f"Processed {file_count} files")
sorted_word_count = sorted(word_count.items(), key=operator.itemgetter(1), reverse=True)
sorted_word_count = dict(sorted_word_count)
with open("wordslist.csv", "w+") as csv_file:
    csv_file.write('word,count\n')
    for word, count in sorted_word_count.items():
        if count < 100:
            break
        csv_file.write(f"{word},{count}\n")
print(f'Time taken to preprocess emails: {round(time.time() - start_time, 2)} seconds')