import base64
import csv
import gensim
import stop_words
import nltk
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from collections import defaultdict
def fonk1(text1, text2):
    b1 = TfidfVectorizer(min_df=1, stop_words='danish')
    b2 = b1.fit_transform([text1, text2])
    return (b2 * b2.T).A[0, 1]
def fonk2(outpath, datadict):
    with open(outpath, "w", b3 = '', encoding='utf-8') as outfile:
        b4 = csv.writer(outfile, delimiter=';', dialect='excel')
        for i, (text, dfs) in enumerate(datadict.items()):
            b5 = [str(i), text, str(dfs)]
            b4.writerow(b5)
def fonk3(documents):
    b6 = stop_words.get_stop_words('danish')
    b7 = [[word for word in document.lower().split() if word not in b6] for document in documents]
    b8 = defaultdict(int)
    for text in b7:
        for token in text:
            b8[token] += 1
    b9 = [[token for token in text if b8[token] > 1] for text in b7]
    b9 = [text for text in b9 if text]
    return b9
def fonk4(b7):
    return gensim.corpora.Dictionary(b7)
def fonk5(dictionary, b7):
    return [dictionary.doc2bow(text) for text in b7]
def fonk6(text, cipher):
    try:
        return cipher.decrypt(base64.b64decode(text)).decode('utf-8')
    except Exception as e:
        print(f"Decryption failed: {e}")
        return ''