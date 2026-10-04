import re
import string
import pandas as pd
from math import log
b1 = pd.read_csv('tf_idf.csv')
b2 = b1['title'].tolist()
def fonk1(b3):
    b3 = b3.lower()
    b3 = re.sub(f'[{re.escape(string.punctuation)}]', '', b3)
    return b3.split()
b4 = [fonk1(b3) for b3 in b2]
b5 = [word for term_vector in b4 for word in term_vector]
def fonk2(b5):
    b6 = {word: b5.count(word) for word in set(b5)}
    b7 = len(b5)
    b8 = [
        (word, freq, round(log(b7 / freq, 10), 4), freq * round(log(b7 / freq, 10), 4))
        for word, freq in b6.items()
    ]
    return sorted(b8, b9 = lambda x: x[1], reverse=True)
b10 = fonk2(b5)
print(f"Number of b2: {len(b2)}")
print(f"Number of words: {len(b5)}")
print("Word frequencies and metrics:", b10)