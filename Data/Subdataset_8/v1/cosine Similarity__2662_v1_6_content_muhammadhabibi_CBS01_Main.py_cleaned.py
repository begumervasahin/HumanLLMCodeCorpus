import nltk
import yaml
import Preprocessing
import TF_IDF
import CosineSimilarity
pp = Preprocessing
cs = CosineSimilarity
output_file = open('komentar.json').read()
komentar = yaml.safe_load(output_file)
komentar_bersih = open('komentar_bersih.txt', 'r')
data = komentar_bersih.read().split('\n')
komen_bersih = [komen for komen in data]
vector = [cs.TFIDF(t) for t in komen_bersih]
kalimat = [
    "sebaiknya waktu kuliahnya jangan terlalu sore",
    "lebih keras lagi suara",
    "buku rujuk kurang jelas mau pakai mana"
]
for test in kalimat:
    print('---------------------------------------------------------------------------------------')
    print('Data Testing :', test)
    input_vector = cs.TFIDF(nltk.Text(str(test)))
    Hasil = []
    for i, t in enumerate(vector):
        sim = cs.similarity(input_vector, t)
        nilai_sim = sim
        komentars = komen_bersih[i]
        Hasil.append((i, nilai_sim, komentars))
    Hasil_sim = sorted(Hasil, key=lambda x: x[1], reverse=True)[0]
    print(Hasil_sim)
    print("------------------------------------------------------------------------")
    for (index, cosine, kal) in Hasil:
        if cosine >= 0.93:
            print(cosine, kal)