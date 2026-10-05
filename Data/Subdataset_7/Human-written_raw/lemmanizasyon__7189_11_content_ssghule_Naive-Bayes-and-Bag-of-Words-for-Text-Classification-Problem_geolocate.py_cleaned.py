import pandas as pd
import sys
import string as s
import nltk
from nltk.tokenize import word_tokenize
import string
from nltk.stem.snowball import SnowballStemmer
nltk.download('stopwords')
nltk.download('punkt')
from nltk.corpus import stopwords
import numpy as np
import collections
def fonk1(b14):
	with open(b14, 'r') as datafile:
   		b1 = datafile.readlines()
	b2 = [word_tokenize(line) for line in b1]
	b3 = stopwords.b2('english')
	b4 = list(string.punctuation) + ['i','\x89','_CA','_TX', '_IL','_NY', '_PA', '_GA', '_Ontario', '_MA', '_FL', '_DC','__', '___']+b3
	b5 = SnowballStemmer("english")
	b2 = [[b5.stem(w) for w in item if w not in b4] for item in b2 if len(item)>1]
	return [word for word in b2 if len(word)>1 and word[0] in b18]
def fonk2(t):
	b6 = set([w for word in t for w in word])
	b7 = pd.DataFrame(0,index=b6, columns=b18)
	for word in t[:]:
		b8 = word[0]
		for w in word[1:]:
			b7.at[w,b8]+=1
	return b7
def fonk3(b15):
	with open(b15, 'r') as datafile:
   		b1 = datafile.readlines()
	b9 = {}
	b3 = stopwords.b2('english')
	b4 = list(string.punctuation) + ['i','\x89','_CA','_TX', '_IL','_NY', '_PA', '_GA', '_Ontario', '_MA', '_FL', '_DC','__', '___'] +b3
	b5 = SnowballStemmer("english")
	for line in b1:
		b2 = word_tokenize(line)
		b9[line]=[b5.stem(w) for w in b2 if w not in b4]
		if b9[line]:
			b9[line].pop(0)
	return b9
def fonk4(b2):
	for word in b2:
		b19[word[0]]+=1
	b10 = sum(b19.values())
	for i in b19:
        	b19[i] = float(b19[i]/b10)
def fonk5(b21, b22, b16):
	with open(b16, 'w') as f:
		for tweet in b22:
			b11 = ''
			b2 = b22[tweet]
			if not b2:
				continue
			else:
				b12 = [[(b21.at[w,b18[i]]/sum(b21.loc[:,b18[i]])*b19[b18[i]]) if w in b21.index else 0.00001*b19[b18[i]] for i in range(0,12)] for w in b2]
			b13 = b12[0]
			for i in range(1,len(b12)):
				b13 = np.multiply(b13,b12[i])
			b13 = list(b13)
			b11 = b17[b13.index(max(b13))]
			f.write(b11+" "+tweet)
	f.close()
	print("Output written to ", b16)
b14 = str(sys.argv[1])
b15 = str(sys.argv[2])
b16 = str(sys.argv[3])
b17 = ['Los_Angeles,_CA', 'San_Francisco,_CA','San_Diego,_CA', 'Houston,_TX','Chicago,_IL','Philadelphia,_PA', 'Toronto,_Ontario','Atlanta,_GA','Boston,_MA', 'Orlando,_FL', 'Washington,_DC', 'Manhattan,_NY']
b18 = ["los_angel", "san_francisco" ,"san_diego" ,"houston", "chicago", "philadelphia", "toronto","atlanta","boston", "orlando","washington", "manhattan"]
b19 = dict.fromkeys(b18, 0)
b20 = fonk1(b14)
b21 = fonk2(b20)
b22 = (fonk3(b15))
fonk4(b20)
b21 = b21+(0.00001)
fonk5(b21, b22, b16)
print('Top five b2 for each b18: ')
for c in b18:
	print(b17[b18.index(c)], b21.nlargest(5, c).index.tolist())