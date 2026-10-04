import nltk
import numpy as np
import matplotlib.pyplot as plt
from nltk.stem import WordNetLemmatizer
from sklearn.decomposition import TruncatedSVD
b1 = WordNetLemmatizer()
b2 = [line.rstrip() for line in open('all_book_titles.txt')]
b3 = set(w.rstrip() for w in open('b3.txt'))
b3 = b3.union({
    'introduction', 'edition', 'series', 'application',
    'approach', 'card', 'access', 'package', 'plus', 'etext',
    'brief', 'vol', 'fundamental', 'guide', 'essential', 'printed',
    'third', 'second', 'fourth', })
def fonk1(b4):
    b4 = b4.lower()
    b5 = nltk.tokenize.word_tokenize(b4)
    b5 = [t for t in b5 if len(t) > 2]
    b5 = [b1.lemmatize(t) for t in b5]
    b5 = [t for t in b5 if t not in b3]
    b5 = [t for t in b5 if not any(c.isdigit() for c in t)]
    return b5
b6 = {}
a1 = 0
b7 = []
b8 = []
b9 = []
for b10 in b2:
	try:
		b10 = b10.encode('ascii', 'ignore').decode('utf-8')
		b8.append(b10)
		b5 = fonk1(b10)
		b7.append(b5)
		for token in b5:
			if token not in b6:
				b6[token] = a1
				a1 += 1
				b9.append(token)
	except:
		pass
def fonk2(b5):
    b11 = np.zeros(len(b6))
    for t in b5:
        b12 = b6[t]
        b11[b12] = 1
    return b11
b13 = len(b7)
b14 = len(b6)
b15 = np.zeros((b14, b13))
b12 = 0
for b5 in b7:
	b15[:,b12] = fonk2(b5)
	b12 += 1
b16 = TruncatedSVD()
b17 = b16.fit_transform(b15)
plt.scatter(b17[:,0], b17[:,1])
for b12 in range(b14):
	plt.annotate(b4 = b9[b12], xy = (b17[b12,0], b17[b12,1]))
plt.show()