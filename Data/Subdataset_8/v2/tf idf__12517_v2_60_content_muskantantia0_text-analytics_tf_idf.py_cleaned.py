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
    flattened_list = []
    for sublist in nested_lists:
        for item in sublist:
            flattened_list.append(item)
    return flattened_list
document_terms = []
for title in document_titles:
    title = str(title).lower()
    title = punctuation_pattern.sub('', title)
    terms = title.split(' ')
    document_terms.append(terms)
all_terms = flatten_lists(document_terms)
def word_list_to_frequency_dict(words):
    word_freq = [words.count(word) for word in words]
    freq_dict = dict(zip(words, word_freq))
    sorted_freq = [(freq, word) for word, freq in freq_dict.items()]
    sorted_freq.sort(reverse=True)
    final_result = [(word, freq, round(log(round((len(words) / freq), 4), 10), 4), freq * log(len(words) / freq, 10)) for freq, word in sorted_freq]
    return final_result
word_freq_tfidf = word_list_to_frequency_dict(all_terms)
print(word_freq_tfidf)