import re
import string
import pandas as pd
from math import log
data = pd.read_csv('tf_idf.csv')
reviewer_ids = data['id'].tolist()
reviewer_ids.insert(0, "reviewerID")
document_titles = data['title'].tolist()
punctuation_pattern = re.compile('[%s]' % re.escape(string.punctuation))
def flatten_lists(nested_lists):
    return [item for sublist in nested_lists for item in sublist]
def preprocess_title(title):
    title = str(title).lower()
    title = punctuation_pattern.sub('', title)
    return title.split()
all_terms = flatten_lists([preprocess_title(title) for title in document_titles])
def calculate_tfidf(words):
    word_freq = {word: words.count(word) for word in words}
    sorted_freq = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
    total_words = len(words)
    tfidf_results = [(word, freq, round(log(total_words / freq, 10), 4), freq * log(total_words / freq, 10)) for word, freq in sorted_freq]
    return tfidf_results
word_freq_tfidf = calculate_tfidf(all_terms)
print(word_freq_tfidf)