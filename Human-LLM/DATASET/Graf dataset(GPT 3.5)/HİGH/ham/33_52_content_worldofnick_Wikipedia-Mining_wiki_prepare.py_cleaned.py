from nltk.corpus import stopwords
from nltk import word_tokenize
import nltk
from sklearn.feature_extraction.text import CountVectorizer, TfidTransformer
import glob
def fonk1(text, k):
	b1 = ngrams(text, k)
	b2 = set()
	for gram in b1:
		b2.add(' '.join(gram))
	return b2
def fonk2(text):
	b3 = nltk.word_tokenize(text)
	b4 = set(stopwords.b3("english"))
	b5 = [word for word in b3 if word not in b4]
	b6 = CountVectorizer()
	b7 = b6.fit_transform(text, ngram_range=(3,3))
	b8 = TfidTransformer()
	return b8.fit_transform(b7).toarray()
def fonk3(kgrams, articleName):
	b9 = open('%s_kgrams.txt' % articleName, "w")
	b9.write(",".join(map(lambda x: str(x), kgrams)))
	b9.close()
b10 = glob.glob('/somePath/*.txt')
for filename in b10:
	b11 = open(filename)
	b12 = fonk2(b11.read())
	fonk3(b12, filename)