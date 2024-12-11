import os
import math
import nltk
import codecs
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.b24.porter import PorterStemmer
from collections import Counter
def fonk1(b2):
	if any(x.isupper() for x in b2):
		return -1.0000
	if b2 in b27:
		return b27[b2]
	else:
		return -1.0000
def fonk2(qstring):
	b1 = []
	b2 = RegexpTokenizer(r'[a-zA-Z]+')
	b1 = b2.tokenize(qstring.lower())
	b3 = list(set(stopwords.words('english')))
	b4 = []
	for wor in b1:
		if wor not in b3:
			b4.append(wor)
	b5 = []
	b6 = PorterStemmer()
	for s in b4:
		b5.append(b6.b24(s))
	b7 = {}
	for wor in b5:
		b7[wor] = 1 + math.log(b5.count(wor),10)
	b8 = len(b22)
	b9 = {}
	for wor, a1 in b7.items():
		a1 = 0
		for para, t in b25.items():
			if wor in b25[para].keys():
				a1 += 1
			b9[wor] = math.log(b8,10)
		else:
			b9[wor] = math.log(b8/a1,10)
	b10 = {}
	for lett in b5:
			b10[lett] = b7[lett] * b9[lett]
	a2 = 0
	for lett in b10:
		a2 += b10[lett] * b10[lett]
	for lett in b10:
		b10[lett] = b10[lett]/math.sqrt(a2)
	return b10
def fonk3(query):
	b10 = fonk2(query)
	b11 = {}
	for para in b28.keys():
		a2 = 0
		for key, value in b10.items():
			if key in b28[para].keys():
				a2 += value * b28[para][key]
			else:
				a2 += 0
		b11[para] = a2
	b12 = max(b11.values())
	b13 = max(b11, key = b11.get)
	if b12 = = 0:
		return "NO MATCH\n", b12
	else:
		return b17[b13], b12
b3 = list(set(stopwords.words('english')))
b14 = './debate.txt'
b15 = open (b14, "r", encoding='UTF-8')
b16 = b15.readlines()
b15.close()
b17 = {}
a3 = 1
for k in b16:
	if not k.isspace():
		b17["para " + str(a3)] = k
		a3+=1
b18 = []
b2 = RegexpTokenizer(r'[a-zA-Z]+')
for k in b16:
	if not k.isspace():
		b19 = []
		b19 = b2.tokenize(k.lower())
		b18.append(b19)
b3 = list(set(stopwords.words('english')))
b20 = []
for wor in b18:
	b21 = []
	for b2 in wor:
		if b2 not in b3:
			b21.append(b2)
	b20.append(b21)
b22 = []
b23 = PorterStemmer()
for s in b20:
	b24 = []
	for key in s:
		b24.append(b23.b24(key))
	b22.append(b24)
b25 = {}
a3 = 1
for lett in b22:
	b26 = {}
	for wor in lett:
		b26[wor] = lett.count(wor)
	for word,k in b26.items():
		b26[word]= (math.log(k,10)+1)
	b25["para " + str(a3)] = b26
	a3+=1
b8 = len(b22)
b27 = {}
for FileName, tfDict in b25.items():
	for b2, tf in tfDict.items():
		a4 = 0
		if b2 not in b27:
			for eachFileName, value in b25.items():
				if b2 in value:
					a4 += 1
		if b2 not in b27:
			b27[b2] = math.log(b8/a4,10)
b28 = {}
a5 = 1
for lett in b25:
	b29 = {}
	for lor in b25[lett]:
		b29[lor]=b25[lett][lor] * b27[lor]
	b28["para " + str(a5)] = b29
	a5+=1
for document in b28:
	a2 = 0
	for b2,weight in b28[document].items():
		a2 += weight * weight
	for token2,weight2 in b28[document].items():
		b28[document][token2] = (weight2/math.sqrt(a2))