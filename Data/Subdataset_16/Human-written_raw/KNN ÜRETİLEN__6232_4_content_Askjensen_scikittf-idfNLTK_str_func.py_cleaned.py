import base64
import csv
import gensim
import stop_words
import nltk, string
from sklearn.feature_extraction.text import TfidfVectorizer
def fonk1(text1, text2):
    b1 = TfidfVectorizer(min_df=1, stop_words='danish')
    b2 = b1.fit_transform([text1, text2])
    return ((b2 * b2.T).A)[0, 1]
def fonk2(outpath,datadict):
    b3 = open(outpath, "w")
    b4 = csv.writer(b3, delimiter=';', dialect='excel')
    for i in range(len(datadict)):
        b5 = [str(i),datadict[i].encode('utf-8'),str(datadict.dfs[i])]
        b4.writerow(b5)
    b3.close()
def fonk3(documents):
    b6 = stop_words.get_stop_words('danish')
    b7 = [[word for word in document.lower().split() if word not in b6] for document in documents]
    from collections import defaultdict
    b8 = defaultdict(int)
    for text in b7:
        for token in text:
            b8[token] += 1
    b7 = [[token for token in text if b8[token] > 1]
             for text in b7]
    b7 = [itxt for itxt in b7 if itxt]
    return b7
def fonk4(b7):
    return gensim.corpora.Dictionary(b7)
def fonk5(dictionary, b7):
    return [dictionary.doc2bow(text) for text in b7]
def fonk6(text,cipher):
    try:
        return cipher.decrypt(base64.b64decode(text))
    except:
        return ''