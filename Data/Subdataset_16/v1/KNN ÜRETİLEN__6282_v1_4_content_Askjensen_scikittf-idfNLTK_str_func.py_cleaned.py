import base64
import csv
import gensim
from stop_words import get_stop_words
from nltk.b18 import b6
from sklearn.feature_extraction.text import TfidfVectorizer
from collections import defaultdict
def fonk1(b10, b11):
    b1 = TfidfVectorizer(min_df=1, stop_words='danish')
    b2 = b1.fit_transform([b10, b11])
    return ((b2 * b2.T).A)[0, 1]
def fonk2(outpath, b13):
    with open(outpath, "w", b3 = '', encoding='utf-8') as outfile:
        b4 = csv.writer(outfile, delimiter=';', dialect='excel')
        for i in range(len(b13)):
            b5 = [str(i), b13[i].encode('utf-8'), str(b13.b14[i])]
            b4.writerow(b5)
def fonk3(b15):
    b6 = get_stop_words('danish')
    b7 = [[word for word in document.lower().split() if word not in b6] for document in b15]
    b8 = defaultdict(int)
    for text in b7:
        for token in text:
            b8[token] += 1
    b7 = [[token for token in text if b8[token] > 1] for text in b7]
    b7 = [itxt for itxt in b7 if itxt]
    return b7
def fonk4(b7):
    return gensim.corpora.Dictionary(b7)
def fonk5(b17, b7):
    return [b17.doc2bow(text) for text in b7]
def fonk6(text, cipher):
    try:
        return cipher.decrypt(base64.b64decode(text))
    except:
        return ''
if b9 = = "__main__":
    b10 = "Dette er en test tekst."
    b11 = "Dette er en anden test tekst."
    b12 = fonk1(b10, b11)
    print(f"Cosine b12: {b12}")
    b13 = {0: "b10", 1: "b11"}
    b13.b14 = [0.5, 0.8]
    fonk2("output.csv", b13)
    b15 = ["Dette er et dokument.", "Dette er et andet dokument."]
    b16 = fonk3(b15)
    print(f"Filtered b7: {b16}")
    b17 = fonk4(b16)
    b18 = fonk5(b17, b16)
    print(f"Dictionary: {b17.token2id}")
    print(f"Corpus: {b18}")
