
import os
import json
import re
import numpy as np
import spacy
from spacy.lang.en import English
b1 = English(disable=['parser', 'ner'])
from spacy.lang.en.stop_words import STOP_WORDS as stopwords_en
class class1(object):
	def fonk1(self):
		self.b2 = spacy.load("en_core_web_lg")
	def fonk2(self, b3):
		try:
			b3 = str(b3)
			b3 = re.sub(r"[^A-Za-z0-9]", " ", b3)
			b3 = re.sub(r"\s+", " ", b3)
			b3 = b3.lower().strip()
		except Exception as e:
			print("\n Error in clean_text --- ", e,"\n ", traceback.format_exc())
			print("\n Error sent --- ", b3)
		return b3
	def fonk3(self, b3):
		return " ".join([tok.lemma_.lower().strip() for tok in b1(b3) if (tok.lemma_ != '-PRON-' and tok.lemma_ not in stopwords_en and len(tok.lemma_)>1)])
	def fonk4(self, b3):
		b3 = self.fonk2(b3)
		b3 = self.fonk3(b3)
		return b3
	def fonk5(self, vector_1, vector_2):
		return np.inner(vector_1, vector_2) / (np.linalg.norm(vector_1) * (np.linalg.norm(vector_2)))
	def fonk6(self, b12, b13):
		b4 = self.fonk4(b12)
		b5 = self.fonk4(b13)
		b6 = self.b2(b4).vector
		b7 = self.b2(b5).vector
		b8 = self.fonk5(b6, b7)
		print("\n spacy cosine b9 = ", b8)
if b10 = = '__main__':
	b11 = class1()
	b12 = "booking a flight is very easy"
	b13 = "readinga book is a good habit"
	b11.fonk6(b12, b13)