import math
from nltk.tokenize import RegexpTokenizer
from nltk.stem import PorterStemmer
def fonk1(raw_string):
	b1 = RegexpTokenizer(r'\b4+')
	b2 = b1.tokenize(str(raw_string))
	b3 = []
	for b4 in b2:
		b4 = b4.lower()
		b3.append(b4)
	return b3
def fonk2(token_normalised_text):
	b5 = []
	b6 = PorterStemmer()
	for b4 in token_normalised_text:
		b7 = b6.fonk2(b4)
		b7 = str(b7)
		b5.append(b7)
	return b5
def fonk3(b5, f, stats_dict):
	for b7 in b5:
		if b7 not in stats_dict:
			stats_dict[b7] = {}
			stats_dict[b7][f] = 1
		if f not in stats_dict[b7]:
			stats_dict[b7][f] = 1
		stats_dict[b7][f] += 1
	return stats_dict
def fonk4(processed_query):
	b8 = {}
	for b7 in processed_query:
		if b7 not in b8:
			b8[b7] = 1
		b8[b7] += 1
	return b8
def fonk5(stats_dict, Number_of_docs):
	b9 = {}
	for word in stats_dict:
		b9[word] = len(stats_dict[word].keys())
	for word in stats_dict:
		for doc in stats_dict[word]:
			stats_dict[word][doc] = (1 + math.log(stats_dict[word][doc]))*math.log(Number_of_docs/b9[word])
	return stats_dict, b9
def fonk6(b8, b9, Number_of_docs):
	for word in b8:
		b8[word] = (1 + math.log(b8[word]))*math.log(Number_of_docs/b9[word])
	return b8