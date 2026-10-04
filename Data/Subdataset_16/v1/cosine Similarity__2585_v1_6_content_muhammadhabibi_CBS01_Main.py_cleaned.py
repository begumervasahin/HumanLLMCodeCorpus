import math
import numpy as np
import json
import yaml
import nltk
from Preprocessing import preprocess
from TF_IDF import compute_tfidf
from CosineSimilarity import compute_similarity
with open('b1.json', 'r') as output_file:
    b1 = yaml.safe_load(output_file)
with open('komentar_bersih.txt', 'r') as komentar_bersih:
    b2 = komentar_bersih.read().split('\n')
b3 = [preprocess(komen) for komen in b2]
b4 = [compute_tfidf(komen) for komen in b3]
b5 = [
    "sebaiknya waktu kuliahnya jangan terlalu sore",
    "lebih keras lagi suara",
    "buku rujukan kurang jelas mau pakai mana"
]
for test in b5:
    print('---------------------------------------------------------------------------------------')
    print('Data Testing:', test)
    b6 = compute_tfidf(nltk.Text(str(test)))
    b7 = []
    for i, t in enumerate(b4):
        b8 = compute_similarity(b6, t)
        b7.append((i, b8, b3[i]))
    b9 = sorted(b7, key=lambda x: x[1], reverse=True)[0]
    print('Best Match:', b9)
    print('------------------------------------------------------------------------')
    for (index, cosine, kal) in b7:
        if cosine >= 0.93:
            print(cosine, kal)