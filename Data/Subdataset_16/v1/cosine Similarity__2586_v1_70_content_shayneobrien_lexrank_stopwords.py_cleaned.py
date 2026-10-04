import math
import numpy as np
import nltk
import json
import yaml
import Preprocessing as pp
import TF_IDF as tfidf
import CosineSimilarity as cs
b1 = [
    'em', 'gonna', 'huh', 'yep',  'goin', 'hi', 'inaudible', 'crosstalk', 'laughter',
    'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours',
    'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself',
    'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which',
    'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be',
    'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an',
    'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for',
    'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above',
    'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further',
    'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each',
    'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so',
    'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now', 'd', 'll', 'm', 'o',
    're', 've', 'y', 'ain', 'aren', 'couldn', 'didn', 'doesn', 'hadn', 'hasn', 'haven', 'isn', 'ma',
    'mightn', 'mustn', 'needn', 'shan', 'shouldn', 'wasn', 'weren', 'won', 'wouldn'
]
def fonk1(text):
    b2 = nltk.RegexpTokenizer(r'\w+')
    b3 = b2.tokenize(text.lower())
    b4 = [word for word in b3 if word not in b1]
    b5 = nltk.PorterStemmer()
    b6 = [b5.stem(token) for token in b4]
    return b6
def fonk2(json_path, txt_path):
    with open(json_path, 'r') as output_file:
        b7 = yaml.safe_load(output_file)
    with open(txt_path, 'r') as komentar_bersih:
        b8 = komentar_bersih.read().split('\n')
    b9 = [fonk1(komen) for komen in b8 if komen]
    return b7, b9
def fonk3(comments):
    return [tfidf.TFIDF(' '.join(comment)) for comment in comments]
def fonk4(b16, b15, comments):
    for test in b16:
        print('---------------------------------------------------------------------------------------')
        print('Data Testing:', test)
        b10 = tfidf.TFIDF(' '.join(fonk1(test)))
        b11 = []
        for i, vector in enumerate(b15):
            b12 = cs.similarity(b10, vector)
            b11.append((i, b12, ' '.join(comments[i])))
        b13 = sorted(b11, key=lambda x: x[1], reverse=True)[0]
        print('Best Match:', b13)
        print('------------------------------------------------------------------------')
        for index, cosine, comment in b11:
            if cosine >= 0.93:
                print(cosine, comment)
if b14 = = "__main__":
    b7, b9 = fonk2('b7.json', 'komentar_bersih.txt')
    b15 = fonk3(b9)
    b16 = [
        "sebaiknya waktu kuliahnya jangan terlalu sore",
        "lebih keras lagi suara",
        "buku rujukan kurang jelas mau pakai mana"
    ]
    fonk4(b16, b15, b9)