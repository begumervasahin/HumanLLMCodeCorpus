import re
import string
import pandas as pd
from math import log
data = pd.read_csv('tf_idf.csv')
documents = data['title'].tolist()
def preprocess_document(doc):
    doc = doc.lower()
    doc = re.sub(f'[{re.escape(string.punctuation)}]', '', doc)
    return doc.split()
term_vectors = [preprocess_document(doc) for doc in documents]
word_list = [word for term_vector in term_vectors for word in term_vector]
def word_list_to_freq_dict(word_list):
    word_freq = {word: word_list.count(word) for word in set(word_list)}
    total_words = len(word_list)
    freq_list = [
        (word, freq, round(log(total_words / freq, 10), 4), freq * round(log(total_words / freq, 10), 4))
        for word, freq in word_freq.items()
    ]
    return sorted(freq_list, key=lambda x: x[1], reverse=True)
finals = word_list_to_freq_dict(word_list)
print(f"Number of documents: {len(documents)}")
print(f"Number of words: {len(word_list)}")
print("Word frequencies and metrics:")
for item in finals:
    print(item)