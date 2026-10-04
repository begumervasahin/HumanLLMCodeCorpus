import re
import string
import pandas as pd
from math import log
def fonk1(file_path):
    return pd.read_csv(file_path)
def fonk2(b1):
    b1 = b1.lower()
    b1 = re.sub(f'[{re.escape(string.punctuation)}]', '', b1)
    return b1.split()
def fonk3(b7):
    return [fonk2(b1) for b1 in b7]
def fonk4(b8):
    return [word for term_vector in b8 for word in term_vector]
def fonk5(b9):
    b2 = {word: b9.count(word) for word in set(b9)}
    b3 = len(b9)
    b4 = [
        (word, freq, round(log(b3 / freq, 10), 4), freq * round(log(b3 / freq, 10), 4))
        for word, freq in b2.items()
    ]
    return sorted(b4, b5 = lambda x: x[1], reverse=True)
def fonk6():
    b6 = fonk1('tf_idf.csv')
    b7 = b6['title'].tolist()
    b8 = fonk3(b7)
    b9 = fonk4(b8)
    b10 = fonk5(b9)
    print(f"Number of b7: {len(b7)}")
    print(f"Number of words: {len(b9)}")
    print("Word frequencies and metrics:")
    for item in b10:
        print(item)
if b11 = = "__main__":
    fonk6()