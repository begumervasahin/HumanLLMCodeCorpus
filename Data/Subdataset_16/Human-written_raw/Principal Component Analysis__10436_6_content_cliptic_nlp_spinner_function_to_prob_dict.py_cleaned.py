import nltk
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import csv
from nltk.tokenize import RegexpTokenizer
b1 = RegexpTokenizer(r'\w+')
b2 = 'electronics/positive.review'
def fonk1(b2):
	b3 = BeautifulSoup(open(b2).read(), features="html.parser")
	b4 = []
	for i in b3.find_all('review_text'):
		b5 = i.get_text()
		b5 = b5.lower()
		b6 = b1.tokenize(b5)
		b4.append(b6)
	b7 = {}
	b8 = {}
	for i in b4:
		a1 = 0
		for n in i:
			if a1 != 0 and a1 != (len(i)-1):
				if n not in b7:
					b7[i[a1]] = [[i[a1-1], i[a1+1]]]
					b8[i[a1]] = 1
				else:
					b7[i[a1]].append([i[a1-1], i[a1+1]])
					b8[i[a1]] += 1
			a1 += 1
	b9 = {}
	b10 = {}
	for key in b7.keys():
		for b11 in b7[key]:
			b11.sort()
			b11 = tuple(b11)
			if b11 not in b9:
				b9[b11] = {key:1}
				b10[b11] = 1
			else:
				if key not in b9[b11].keys():
					b9[b11][key] = 1
				else:
					b9[b11][key] += 1
				b10[b11] += 1
	for key in b9.keys():
		for b11 in b9[key]:
			b9[key][b11] = b9[key][b11] / b10[key]
	return b9
b12 = fonk1('electronics/positive.review')
print(b12[('i', 'this')]['bought'])