import base64
import csv
import gensim
import stop_words
from sklearn.feature_extraction.text import TfidfVectorizer
def fonk1(text1, text2):
    b1 = TfidfVectorizer(min_df=1, stop_words='danish')
    b2 = b1.fit_transform([text1, text2])
    return ((b2 * b2.T).A)[0, 1]
def fonk2(output_path, data_dict):
    with open(output_path, "w", b3 = '', encoding='utf-8') as csvfile:
        b4 = csv.b4(csvfile, delimiter=';', dialect='excel')
        for idx, (key, value) in enumerate(data_dict.items()):
            b4.writerow([str(idx), key, str(value)])
def fonk3(documents):
    b5 = stop_words.get_stop_words('danish')
    b6 = [[word for word in document.lower().split() if word not in b5] for document in documents]
    from collections import defaultdict
    b7 = defaultdict(int)
    for text in b6:
        for token in text:
            b7[token] += 1
    b6 = [[token for token in text if b7[token] > 1] for text in b6]
    b6 = [txt for txt in b6 if txt]
    return b6
def fonk4(b6):
    return gensim.corpora.Dictionary(b6)
def fonk5(dictionary, b6):
    return [dictionary.doc2bow(text) for text in b6]
def fonk6(text, cipher):
    try:
        return cipher.decrypt(base64.b64decode(text))
    except Exception as e:
        return ''
