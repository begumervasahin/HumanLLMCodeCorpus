import re
import string
import pandas as pd
from math import log
data = pd.read_csv('tf_idf.csv')
reviewer = data['id'].tolist()
reviewer.insert(0, "reviewerID")
doc = data['title'].tolist()
punc = re.compile('[%s]' % re.escape(string.punctuation))
def flatten(lists):
    wordlist = []
    for numbers in lists:
        for x in numbers:
            wordlist.append(x)
    return wordlist
term_vec = []
for d in doc:
    d = str(d).lower()
    d = punc.sub('', d)
    d = d.split(' ')
    term_vec.append(d)
wordlist = flatten(term_vec)
def wordListToFreqDict(wordlist):
    wordfreq = [wordlist.count(p) for p in wordlist]
    d = dict(zip(wordlist, wordfreq))
    items = [(v, k) for k, v in d.items()]
    items.sort()
    items.reverse()
    finals = [(k, v, round(log(round((len(wordlist) / v), 4), 10), 4), (v * (log((len(wordlist) / v), 10)))) for v, k in items]
    return finals
finals = wordListToFreqDict(wordlist)
print(finals)