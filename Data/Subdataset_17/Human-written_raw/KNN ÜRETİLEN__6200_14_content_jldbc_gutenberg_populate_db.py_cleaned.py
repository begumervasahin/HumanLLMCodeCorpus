from sklearn.feature_extraction.text import TfidfVectorizer
import sys, re
import numpy as np
from random import random
from operator import add
import pymongo
from pymongo import MongoClient
import os
client = MongoClient()
db = client.bookdb
posts = db.posts
documents = []
docsDir = "/Users/jamesledoux/Documents/Drew2"
for book in os.listdir(docsDir):
	if not book.startswith('.'):
		book = str(book)
		with open("/Users/jamesledoux/Documents/Drew2/" + book, 'rb') as f:
			content = f.read()
			content = unicode(content, errors='replace')
			documents.append(content)
tfidf = TfidfVectorizer(max_df=0.9,
                        ngram_range=(1, 1),
                        stop_words='english',
                        strip_accents='unicode', analyzer = 'word')
tfidf_matrix =  tfidf.fit_transform(documents)
feature_names = tfidf.get_feature_names()
title_author_store = []
for book in os.listdir(docsDir):
	title = None
	author = None
	if not book.startswith('.'):
		book = str(book)
		with open("/Users/jamesledoux/Documents/Drew2/" + book, 'rb') as f:
			content = f.read().splitlines()
		for i in range(80):
			if "Title: " in content[i]:
				title = content[i][7:]
			if "Author: " in content[i]:
				author = content[i][8:]
		title_author_tuple = (title, author)
		title_author_store.append(title_author_tuple)
database = {}
for i in range(tfidf_matrix.shape[0]):
	doc = tfidf_matrix[i].toarray()[0]
	phrase_scores = [pair for pair in zip(range(0, len(doc)), doc) if pair[1] > 0]
	sorted_phrase_scores = sorted(phrase_scores, key=lambda t: t[1] * -1)
	local_word_dict = {}
	for pair in sorted_phrase_scores:
		term = feature_names[pair[0]].encode('ascii', 'ignore').decode('ascii')
		local_word_dict[term] = pair[1]
	database[(title_author_store[i])] = local_word_dict
for i in database.keys():
	title = i[0]
	author = i[1]
	try:
		post = {"title_id_0011": str(title), "author_id_0011": str(author)}
		words = database[i]
		post = dict(post.items() + words.items())
		post_id = posts.insert_one(post).inserted_id
	except:
		print str(title) + ", " + str(author) + " failed"
for i in database.keys():
	title = i[0].encode('ascii', 'ignore').decode('ascii')
	author = i[1].encode('ascii', 'ignore').decode('ascii')
	try:
		post = {"title_id_0011": str(title), "author_id_0011": str(author)}
		words = database[i]
		post = dict(post.items() + words.items())
		post_id = posts.insert_one(post).inserted_id
	except:
		print str(title) + ", " + str(author) + " failed"