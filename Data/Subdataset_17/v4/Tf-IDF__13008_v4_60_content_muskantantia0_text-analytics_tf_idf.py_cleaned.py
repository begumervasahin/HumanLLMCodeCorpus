import nltk.corpus
import re
import string
import pandas as pd
from math import log
data = pd.read_csv('tf_idf.csv')
reviewer = data['id'].tolist()
reviewer.insert(0, "reviewerID")
documents = data['title'].tolist()
print(type(documents))
print(len(documents))
punctuation_pattern = re.compile('[%s]' % re.escape(string.punctuation))
term_vectors = []
for doc in documents:
    doc = str(doc).lower()
    doc = punctuation_pattern.sub('', doc)
    term_vectors.append(doc.split())
def flatten(lists):
    return [word for sublist in lists for word in sublist]
word_list = flatten(term_vectors)
print(len(word_list))
def word_list_to_freq_dict(word_list):
    word_freq = {word: word_list.count(word) for word in word_list}
    sorted_items = sorted(word_freq.items(), key=lambda item: item[1], reverse=True)
    final_result = [
        (word, freq, round(log(len(word_list) / freq, 10), 4), freq * log(len(word_list) / freq, 10))
        for word, freq in sorted_items
    ]
    return final_result
final_results = word_list_to_freq_dict(word_list)
print(final_results)