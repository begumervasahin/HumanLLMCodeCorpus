import base64
import csv
import gensim
from stop_words import get_stop_words
from sklearn.feature_extraction.text import TfidfVectorizer
from collections import defaultdict
def fonk1(text1, text2):
    b1 = TfidfVectorizer(min_df=1, stop_words='danish')
    b2 = b1.fit_transform([text1, text2])
    b3 = (b2 * b2.T).A[0, 1]
    return b3
def fonk2(outpath, datadict):
    with open(outpath, "w", b4 = '', encoding='utf-8') as outfile:
        b5 = csv.writer(outfile, delimiter=';', dialect='excel')
        for i, (text, dfs) in enumerate(datadict.items()):
            b6 = [str(i), text, str(dfs)]
            b5.writerow(b6)
def fonk3(documents):
    b7 = get_stop_words('danish')
    b8 = [[word for word in document.lower().split() if word not in b7] for document in documents]
    b9 = defaultdict(int)
    for text in b8:
        for token in text:
            b9[token] += 1
    b10 = [[token for token in text if b9[token] > 1] for text in b8]
    b10 = [text for text in b10 if text]
    return b10
def fonk4(b8):
    return gensim.corpora.Dictionary(b8)
def fonk5(dictionary, b8):
    return [dictionary.doc2bow(text) for text in b8]
def fonk6(text, cipher):
    try:
        b11 = cipher.decrypt(base64.b64decode(text)).decode('utf-8')
        return b11
    except Exception as e:
        print(f"Decryption failed: {e}")
        return ''