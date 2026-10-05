import re
import string
import pandas as pd
from math import log
b1 = pd.read_csv('tf_idf.csv')
b2 = b1['id'].tolist()
b2.insert(0, "reviewerID")
b3 = b1['b5'].tolist()
b4 = re.compile('[%s]' % re.escape(string.punctuation))
def fonk1(nested_lists):
    return [item for sublist in nested_lists for item in sublist]
def fonk2(b5):
    b5 = str(b5).lower()
    b5 = b4.sub('', b5)
    return b5.split()
b6 = fonk1([fonk2(b5) for b5 in b3])
def fonk3(words):
    b7 = {word: words.count(word) for word in words}
    b8 = sorted(b7.items(), key=lambda x: x[1], reverse=True)
    b9 = len(words)
    b10 = [(word, freq, round(log(b9 / freq, 10), 4), freq * log(b9 / freq, 10)) for word, freq in b8]
    return b10
b11 = fonk3(b6)
print(b11)