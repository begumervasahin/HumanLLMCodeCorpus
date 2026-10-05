import nltk
import yaml
import Preprocessing
import TF_IDF
import CosineSimilarity
b1 = Preprocessing
b2 = CosineSimilarity
b3 = open('b4.json').read()
b4 = yaml.safe_load(b3)
b5 = open('b5.txt', 'r')
b6 = b5.read().split('\n')
b7 = [komen for komen in b6]
b8 = [b2.TFIDF(t) for t in b7]
b9 = [
    "sebaiknya waktu kuliahnya jangan terlalu sore",
    "lebih keras lagi suara",
    "buku rujuk kurang jelas mau pakai mana"
]
for test in b9:
    print('---------------------------------------------------------------------------------------')
    print('Data Testing :', test)
    b10 = b2.TFIDF(nltk.Text(str(test)))
    b11 = []
    for i, t in enumerate(b8):
        b12 = b2.similarity(b10, t)
        b13 = b12
        b14 = b7[i]
        b11.append((i, b13, b14))
    b15 = sorted(b11, key=lambda x: x[1], reverse=True)[0]
    print(b15)
    print("------------------------------------------------------------------------")
    for (index, cosine, kal) in b11:
        if cosine >= 0.93:
            print(cosine, kal)