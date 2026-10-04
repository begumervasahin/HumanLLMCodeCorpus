import re
import string
import pandas as pd
from math import log
b1 = pd.read_csv('tf_idf.csv')
b2 = b1['id'].tolist()
b2.insert(0, "reviewerID")
b3 = b1['title'].tolist()
print(f"Type of b3: {type(b3)}")
print(f"Number of b3: {len(b3)}")
b4 = re.compile(f'[{re.escape(string.punctuation)}]')
def fonk1(b5):
    b5 = str(b5).lower()
    b5 = b4.sub('', b5)
    return b5.split()
b6 = [fonk1(b5) for b5 in b3]
def fonk2(list_of_lists):
    return [word for sublist in list_of_lists for word in sublist]
b7 = fonk2(b6)
print(f"Number of words: {len(b7)}")
def fonk3(words):
    return {word: words.count(word) for word in set(words)}
b8 = fonk3(b7)
b9 = sorted(b8.items(), key=lambda item: item[1], reverse=True)
def fonk4(b8, b10):
    return [
        (
            word,
            freq,
            round(log(b10 / freq, 10), 4),
            freq * log(b10 / freq, 10)
        )
        for word, freq in b8
    ]
b10 = len(b7)
b11 = fonk4(b9, b10)
print(b11)