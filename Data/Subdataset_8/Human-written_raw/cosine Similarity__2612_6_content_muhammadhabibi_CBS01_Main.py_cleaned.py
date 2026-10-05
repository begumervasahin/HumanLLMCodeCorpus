from __future__ import division
import math
import numpy
import nltk
import json
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
komen_bersih=[]
for komen in data:
	komen_bersih.append(komen)
vector = [cs.TFIDF(t) for t in komen_bersih]
kalimat=[]
kalimat.append("sebaiknya waktu kuliahnya jangan terlalu sore")
kalimat.append("lebih keras lagi suara")
kalimat.append("buku rujuk kurang jelas mau pakai mana")
for test in kalimat:
	print'---------------------------------------------------------------------------------------'
	print'Data Testing :', test
	input_vector = cs.TFIDF(nltk.Text(str(test)))
	Hasil=[]
	tup=()
	for i,t in enumerate(vector):
		sim = cs.similarity(input_vector,t)
		nilai_sim=sim
		komentars=komen_bersih[i]
		tup=(i,nilai_sim,komentars)
		Hasil.append(tup)
	Hasil_sim=sorted(Hasil, key=lambda x: x[1], reverse=True)[0]
	print Hasil_sim
	print ("------------------------------------------------------------------------")
	for (index, cosine, kal) in Hasil:
		if cosine >= 0.93 :
			print (cosine, kal)