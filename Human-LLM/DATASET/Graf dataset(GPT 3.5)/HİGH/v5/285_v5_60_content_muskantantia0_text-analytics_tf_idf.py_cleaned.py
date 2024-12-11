import re
import string
import pandas as pd
b1 = pd.read_csv('tf_idf.csv')
b2 = b1['id'].tolist()
b2.insert(0, "reviewerID")
b3 = b1['b4'].tolist()
def fonk1(b4):
    b4 = b4.lower()
    b4 = re.sub('[%s]' % re.escape(string.punctuation), '', b4)
    return b4.split()
b5 = [fonk1(b4) for b4 in b3]
b6 = [word for sublist in b5 for word in sublist]
def fonk2(b6):
    b7 = [b6.count(word) for word in b6]
    return dict(zip(b6, b7))
b8 = fonk2(b6)
b9 = sorted(b8.items(), key=lambda x: x[1], reverse=True)
def fonk3(b9, total_words):
    b10 = [(word, freq, round(log(total_words / freq, 10), 4), freq * log(total_words / freq, 10)) for word, freq in b9]
    return b10
b11 = fonk3(b9, len(b6))
print(b11)