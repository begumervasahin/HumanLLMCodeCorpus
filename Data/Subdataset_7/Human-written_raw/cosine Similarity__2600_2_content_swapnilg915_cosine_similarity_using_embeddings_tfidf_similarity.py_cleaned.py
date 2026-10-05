import json, os, traceback, re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag
class class1(object):
	def fonk1(self):
		self.b1 = list(stopwords.words('english'))
		self.b2 = WordNetLemmatizer()
	def fonk2(self, text):
		return " ".join([tpl[0] for tpl in pos_tag(text.split()) if tpl[1] in ['NN','VB'] ])
	def fonk3(self, b4, b3 = False):
		b4 = str(b4)
		b4 = re.sub(r"([\w].)([\~\!\@\
		b4 = re.sub(r"\s+", " ", b4)
		if b3:
			return " ".join([self.b2.lemmatize(token, 'v') for token in word_tokenize(b4.lower()) if token not in self.b1 and token.isalpha()])
		else:
			return " ".join([token for token in word_tokenize(b4.lower()) if token not in self.b1 and token.isalpha()])
	def fonk4(self, b10, b11):
		b5 = ''
		try:
			print("\n TF-TDF Vectorizer --- ")
			print("\n JD 333--- ", b10, len(b10))
			print("\n b11 333--- ",b11, len(b11))
			b6 = list(set(b10.split()) & set(b11.split()))
			print("\n common words --- ", b6, len(b6))
			b7 = TfidfVectorizer(use_idf = True, sublinear_tf=True, lowercase = True)
			b8 = [b10]
			b8 = b7.fit_transform(b8)
			b9 = b7.transform([b11])
			b5 = cosine_similarity(b8, b9).flatten()[0]
			print("\n tfidf similarity --- ", b5)
		except Exception as e:
			print("\n Error in fonk4() ",e, "\n ",traceback.format_exc())
		return b5
	def fonk5(self, b10, b11):
		b10 = self.fonk3(b10, True)
		b11 = self.fonk3(b11, True)
		b11 = self.fonk2(b11)
		return self.fonk4(b10, b11)
	def fonk6(self):
		self.fonk5(b10, b11)
if b12 = = '__main__':
	b13 = class1()
	b13.fonk5()