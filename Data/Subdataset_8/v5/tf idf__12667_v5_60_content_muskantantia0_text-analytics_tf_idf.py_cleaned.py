import re
import string
import pandas as pd
data = pd.read_csv('tf_idf.csv')
reviewer_ids = data['id'].tolist()
reviewer_ids.insert(0, "reviewerID")
titles = data['title'].tolist()
def clean_and_tokenize(title):
    title = title.lower()
    title = re.sub('[%s]' % re.escape(string.punctuation), '', title)
    return title.split()
term_vec = [clean_and_tokenize(title) for title in titles]
wordlist = [word for sublist in term_vec for word in sublist]
def count_word_frequency(wordlist):
    wordfreq = [wordlist.count(word) for word in wordlist]
    return dict(zip(wordlist, wordfreq))
word_freq_dict = count_word_frequency(wordlist)
sorted_word_freq = sorted(word_freq_dict.items(), key=lambda x: x[1], reverse=True)
def calculate_tfidf(sorted_word_freq, total_words):
    tfidf_scores = [(word, freq, round(log(total_words / freq, 10), 4), freq * log(total_words / freq, 10)) for word, freq in sorted_word_freq]
    return tfidf_scores
finals = calculate_tfidf(sorted_word_freq, len(wordlist))
print(finals)