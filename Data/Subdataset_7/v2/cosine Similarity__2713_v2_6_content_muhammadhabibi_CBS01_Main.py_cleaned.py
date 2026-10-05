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
    b4 = file.read().split('\n')
    b5 = [komen for komen in b4]
b6 = [b2.TFIDF(comment) for comment in b5]
b7 = [
    "sebaiknya waktu kuliahnya jangan terlalu sore",
    "lebih keras lagi suara",
    "buku rujuk kurang jelas mau pakai mana"
]
for test in b7:
    print('---------------------------------------------------------------------------------------')
    print('Data Testing:', test)
    b8 = b2.TFIDF(nltk.Text(str(test)))
    b9 = []
    for i, t in enumerate(b6):
        b10 = b2.similarity(b8, t)
        b11 = b10
        b12 = b5[i]
        b9.append((i, b11, b12))
    b13 = sorted(b9, key=lambda x: x[1], reverse=True)[0]
    print(b13)
    print("------------------------------------------------------------------------")
    for (index, cosine, kal) in b9:
        if cosine >= 0.93:
            print(cosine, kal)