from __future__ import division
import numpy as np
import nltk
import yaml
import Preprocessing
import TF_IDF
import CosineSimilarity
b1 = Preprocessing
b2 = CosineSimilarity
with open('b3.json', 'r') as file:
    b3 = yaml.safe_load(file)
with open('komentar_bersih.txt', 'r') as file:
    b4 = [line.strip() for line in file]
b5 = [b2.TFIDF(comment) for comment in b4]
b6 = [
    "sebaiknya waktu kuliahnya jangan terlalu sore",
    "lebih keras lagi suara",
    "buku rujuk kurang jelas mau pakai mana"
]
for sentence in b6:
    print('---------------------------------------------------------------------------------------')
    print('Testing Sentence:', sentence)
    b7 = b2.TFIDF(nltk.Text(str(sentence)))
    b8 = []
    for index, vector in enumerate(b5):
        b9 = b2.b9(b7, vector)
        b8.append((index, b9, b4[index]))
    b10 = max(b8, key=lambda x: x[1])
    print("Most Similar Comment:", b10)
    print("------------------------------------------------------------------------")
    for index, cosine, comment in b8:
        if cosine >= 0.93:
            print(cosine, comment)