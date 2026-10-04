import math
import numpy as np
import json
import yaml
import nltk
from Preprocessing import preprocess
from TF_IDF import compute_tfidf
from CosineSimilarity import compute_similarity
def fonk1(json_path, txt_path):
    with open(json_path, 'r') as output_file:
        b1 = yaml.safe_load(output_file)
    with open(txt_path, 'r') as komentar_bersih:
        b2 = komentar_bersih.read().split('\n')
    b3 = [preprocess(komen) for komen in b2]
    return b3
def fonk2(comments):
    return [compute_tfidf(comment) for comment in comments]
def fonk3(b10, b9, comments):
    for test in b10:
        print('---------------------------------------------------------------------------------------')
        print('Data Testing:', test)
        b4 = compute_tfidf(nltk.Text(str(test)))
        b5 = []
        for i, vector in enumerate(b9):
            b6 = compute_similarity(b4, vector)
            b5.append((i, b6, comments[i]))
        b7 = sorted(b5, key=lambda x: x[1], reverse=True)[0]
        print('Best Match:', b7)
        print('------------------------------------------------------------------------')
        for index, cosine, kal in b5:
            if cosine >= 0.93:
                print(cosine, kal)
if b8 = = "__main__":
    b3 = fonk1('b1.json', 'komentar_bersih.txt')
    b9 = fonk2(b3)
    b10 = [
        "sebaiknya waktu kuliahnya jangan terlalu sore",
        "lebih keras lagi suara",
        "buku rujukan kurang jelas mau pakai mana"
    ]
    fonk3(b10, b9, b3)