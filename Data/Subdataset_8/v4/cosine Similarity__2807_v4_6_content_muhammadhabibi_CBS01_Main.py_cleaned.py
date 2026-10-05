from __future__ import division
import numpy as np
import nltk
import json
import yaml
import Preprocessing
import TF_IDF
import CosineSimilarity
pp = Preprocessing
cs = CosineSimilarity
with open('komentar.json', 'r') as file:
    komentar = yaml.safe_load(file)
with open('komentar_bersih.txt', 'r') as file:
    data = file.read().split('\n')
    komen_bersih = [komen for komen in data]
vector = [cs.TFIDF(comment) for comment in komen_bersih]
kalimat = [
    "sebaiknya waktu kuliahnya jangan terlalu sore",
    "lebih keras lagi suara",
    "buku rujuk kurang jelas mau pakai mana"
]
for test in kalimat:
    print('---------------------------------------------------------------------------------------')
    print('Data Testing:', test)
    input_vector = cs.TFIDF(nltk.Text(str(test)))
    similarity_results = []
    for i, t in enumerate(vector):
        sim = cs.similarity(input_vector, t)
        nilai_sim = sim
        komentars = komen_bersih[i]
        similarity_results.append((i, nilai_sim, komentars))
    most_similar = sorted(similarity_results, key=lambda x: x[1], reverse=True)[0]
    print(most_similar)
    print("------------------------------------------------------------------------")
    for (index, cosine, kal) in similarity_results:
        if cosine >= 0.93:
            print(cosine, kal)