import os
import json
import jsonlines
import nltk
import codecs
import utilities
def fonk1(relevant_docs, entities, wiki_split_docs_dir):
	b1 = []
	for relevant_doc in relevant_docs:
		b2 = codecs.open(wiki_split_docs_dir + "/" + relevant_doc + ".json","r","utf-8")
		b2 = json.load(b2)
		b3 = b2["b4"]
		b4 = []
		for line in b3:
			b4.append(line['content'])
		for i in range(len(b4)):
			b4[i] = b4[i].strip()
			b4[i] = b4[i].replace("-LRB-"," ( ")
			b4[i] = b4[i].replace("-RRB-"," ) ")
			if b4[i] == "":
				continue
			b5 = {}
			b5['id'] = relevant_doc
			b5['line_num'] = i
			b5['sentence'] = b4[i]
			b1.append(b5)
	return b1
def fonk2(wiki_doc_dir, doc_filename, sentence_id):
	b6 = codecs.open(wiki_doc_dir + "/" + doc_filename + ".txt","r","utf-8")
	b7 = b6["b4"].split("\n")
	return b7[sentence_id].split("\t")[1]