from sklearn.feature_extraction.text import TfidfVectorizer
import sys, re
import numpy as np
from random import random
from operator import add
import pymongo
from pymongo import MongoClient
import os
b1 = MongoClient()
b2 = b1.bookdb
b3 = b2.b3
b4 = []
b5 = "/Users/jamesledoux/Documents/Drew2"
for b6 in os.listdir(b5):
	if not b6.startswith('.'):
		b6 = str(b6)
		with open("/Users/jamesledoux/Documents/Drew2/" + b6, 'rb') as f:
			b7 = f.read()
			b7 = unicode(b7, errors='replace')
			b4.append(b7)
b8 = TfidfVectorizer(max_df=0.9,
                        b9 = (1, 1),
                        b10 = 'english',
                        b11 = 'unicode', analyzer = 'word')
b12 = b8.fit_transform(b4)
b13 = b8.get_feature_names()
b14 = []
for b6 in os.listdir(b5):
	b15 = None
	b16 = None
	if not b6.startswith('.'):
		b6 = str(b6)
		with open("/Users/jamesledoux/Documents/Drew2/" + b6, 'rb') as f:
			b7 = f.read().splitlines()
		for i in range(80):
			if "Title: " in b7[i]:
				b15 = b7[i][7:]
			if "Author: " in b7[i]:
				b16 = b7[i][8:]
		b17 = (b15, b16)
		b14.append(b17)
b18 = {}
for i in range(b12.shape[0]):
	b19 = b12[i].toarray()[0]
	b20 = [pair for pair in zip(range(0, len(b19)), b19) if pair[1] > 0]
	b21 = sorted(b20, key=lambda t: t[1] * -1)
	b22 = {}
	for pair in b21:
		b23 = b13[pair[0]].encode('ascii', 'ignore').decode('ascii')
		b22[b23] = pair[1]
	b18[(b14[i])] = b22
for i in b18.keys():
	b15 = i[0]
	b16 = i[1]
	try:
		b24 = {"title_id_0011": str(b15), "author_id_0011": str(b16)}
		b25 = b18[i]
		b24 = dict(b24.items() + b25.items())
		b26 = b3.insert_one(b24).inserted_id
	except:
		print str(b15) + ", " + str(b16) + " failed"
for i in b18.keys():
	b15 = i[0].encode('ascii', 'ignore').decode('ascii')
	b16 = i[1].encode('ascii', 'ignore').decode('ascii')
	try:
		b24 = {"title_id_0011": str(b15), "author_id_0011": str(b16)}
		b25 = b18[i]
		b24 = dict(b24.items() + b25.items())
		b26 = b3.insert_one(b24).inserted_id
	except:
		print str(b15) + ", " + str(b16) + " failed"