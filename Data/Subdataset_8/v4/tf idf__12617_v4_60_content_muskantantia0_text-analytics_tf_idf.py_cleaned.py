import nltk.corpus
import re
import string
import pandas as pd
data = pd.read_csv('tf_idf.csv')
reviewer = data['id'].tolist()
reviewer.insert(0, "reviewerID")
titles = data['title'].tolist()
punctuation = re.compile('[%s]' % re.escape(string.punctuation))
term_vec = []
for title in titles:
    title = str(title)
    title = title.lower()
    title = punctuation.sub('', title)
    title = title.split(' ')
    term_vec.append(title)
wordlist = []
def flatten(lists):
    for sublist in lists:
        for word in sublist:
            wordlist.append(word)
    return wordlist
wordlist = flatten(term_vec)
wordfreq = []
def wordListToFreqDict(wordlist):
    wordfreq = [wordlist.count(word) for word in wordlist]
    word_freq_dict = dict(zip(wordlist, wordfreq))
    sorted_word_freq = sorted(word_freq_dict.items(), key=lambda x: x[1], reverse=True)
    final_result = [(word, freq, round(log(len(wordlist)/freq, 10), 4), freq * log(len(wordlist)/freq, 10)) for word, freq in sorted_word_freq]
    return final_result
finals = wordListToFreqDict(wordlist)
print(finals)