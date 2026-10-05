from __future__ import division
import math
import numpy
import nltk
import json
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
b7 = []
for komen in b6:
	b7.append(komen)
b8 = [b2.TFIDF(t) for t in b7]
b9 = []
b9.append("sebaiknya waktu kuliahnya jangan terlalu sore")
b9.append("lebih keras lagi suara")
b9.append("buku rujuk kurang jelas mau pakai mana")
for test in b9:
	print'---------------------------------------------------------------------------------------'
	print'Data Testing :', test
	b10 = b2.TFIDF(nltk.Text(str(test)))
	b11 = []
	b12 = ()
	for i,t in enumerate(b8):
		b13 = b2.similarity(b10,t)
		b14 = b13
		b15 = b7[i]
		b12 = (i,b14,b15)
		b11.append(b12)
	b16 = sorted(b11, key=lambda x: x[1], reverse=True)[0]
	print b16
	print ("------------------------------------------------------------------------")
	for (index, cosine, kal) in b11:
		if cosine >= 0.93 :
			print (cosine, kal)