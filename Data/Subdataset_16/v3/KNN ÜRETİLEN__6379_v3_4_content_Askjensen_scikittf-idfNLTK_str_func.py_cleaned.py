import base64
import csv
from collections import defaultdict
from stop_words import get_stop_words
from sklearn.feature_extraction.text import TfidfVectorizer
import gensim
def fonk1(b11, b12):
    b1 = TfidfVectorizer(min_df=1, stop_words='danish')
    b2 = b1.fit_transform([b11, b12])
    return (b2 * b2.T).A[0, 1]
def fonk2(outpath, b14):
    with open(outpath, "w", b3 = '', encoding='utf-8') as outfile:
        b4 = csv.writer(outfile, delimiter=';', dialect='excel')
        for i, text in b14.items():
            b5 = [str(i), text.encode('utf-8'), str(b14.b15[i])]
            b4.writerow(b5)
def fonk3(b16):
    b6 = get_stop_words('danish')
    b7 = [
        [word for word in document.lower().split() if word not in b6]
        for document in b16
    ]
    b8 = defaultdict(int)
    for text in b7:
        for token in text:
            b8[token] += 1
    b9 = [
        [token for token in text if b8[token] > 1]
        for text in b7
    ]
    return [text for text in b9 if text]
def fonk4(b7):
    return gensim.corpora.Dictionary(b7)
def fonk5(b17, b7):
    return [b17.doc2bow(text) for text in b7]
def fonk6(text, cipher):
    try:
        return cipher.decrypt(base64.b64decode(text))
    except Exception as e:
        print(f"Decryption failed: {e}")
        return ''
if b10 = = "__main__":
    b11 = "Dette er en test tekst."
    b12 = "Dette er en anden test tekst."
    b13 = fonk1(b11, b12)
    print(f"Cosine b13: {b13}")
    b14 = {0: "b11", 1: "b12"}
    b14.b15 = [0.5, 0.8]
    fonk2("output.csv", b14)
    b16 = ["Dette er et dokument.", "Dette er et andet dokument."]
    b9 = fonk3(b16)
    print(f"Filtered b7: {b9}")
    b17 = fonk4(b9)
    b18 = fonk5(b17, b9)
    print(f"Dictionary: {b17.token2id}")
    print(f"Corpus: {b18}")
