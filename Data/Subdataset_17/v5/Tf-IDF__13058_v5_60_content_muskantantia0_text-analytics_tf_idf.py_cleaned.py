import re
import string
import pandas as pd
from math import log
data = pd.read_csv('tf_idf.csv')
reviewer_ids = data['id'].tolist()
reviewer_ids.insert(0, "reviewerID")
documents = data['title'].tolist()
print(f"Type of documents: {type(documents)}")
print(f"Number of documents: {len(documents)}")
punctuation_pattern = re.compile(f'[{re.escape(string.punctuation)}]')
def tokenize_and_clean(doc):
    doc = str(doc).lower()
    doc = punctuation_pattern.sub('', doc)
    return doc.split()
term_vectors = [tokenize_and_clean(doc) for doc in documents]
def flatten(list_of_lists):
    return [word for sublist in list_of_lists for word in sublist]
word_list = flatten(term_vectors)
print(f"Number of words: {len(word_list)}")
def calculate_word_frequencies(words):
    return {word: words.count(word) for word in set(words)}
word_frequencies = calculate_word_frequencies(word_list)
sorted_word_frequencies = sorted(word_frequencies.items(), key=lambda item: item[1], reverse=True)
def compute_tfidf_statistics(word_frequencies, total_words):
    return [
        (
            word,
            freq,
            round(log(total_words / freq, 10), 4),
            freq * log(total_words / freq, 10)
        )
        for word, freq in word_frequencies
    ]
total_words = len(word_list)
final_results = compute_tfidf_statistics(sorted_word_frequencies, total_words)
print(final_results)