import pandas as pd
import os
from nltk.corpus import stopwords
import nltk.data
import logging
import numpy as np
import gensim
from KaggleWord2VecUtility import KaggleWord2VecUtility
from sklearn.metrics.pairwise import cosine_similarity
def fonk1(words, b11, a3):
    b1 = np.zeros((a3,),dtype="float32")
    a1 = 0.
    b2 = set(b11.index2word)
    for word in words:
        if word in b2:
            a1 = a1 + 1.
            b1 = np.add(b1,b11[word])
    b1 = np.divide(b1,a1)
    return b1
def fonk2(skucollection, b11, a3):
    a2 = 0.
    b3 = np.zeros((len(skucollection),a3),dtype="float32")
    for sku in skucollection:
       if a2%1000. == 0.:
           print "sku %d of %d" % (a2, len(skucollection))
       b3[a2] = fonk1(sku, b11, \
           a3)
       a2 = a2 + 1.
    return b3
def fonk3(skucollection):
    b4 = []
    for sku in skucollection["product_title"]:
        b4.append( KaggleWord2VecUtility.sku_to_wordlist( sku, b5 = False ))
    return b4
def fonk4(skucollection):
    b4 = []
    for sku in skucollection["a4"]:
        b4.append( KaggleWord2VecUtility.sku_to_wordlist( sku, b5 = False ))
    return b4
if b6 = = '__main__':
  	b7 = pd.read_csv( os.path.join(os.path.dirname(__file__), 'data_crowflower', 'b7.csv'), header=0, delimiter=",", quoting=6 )
    	b8 = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data_crowflower', 'b8.csv'), header=0, delimiter=",", quoting=6 )
 	print "Read %d labeled b7 skucollection, %d labeled b8 skucollection" % (b7["product_title"].size, b8["a4"].size)
	b9 = nltk.data.load('tokenizers/punkt/english.pickle')
    	logging.basicConfig(b10 = '%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
	a3 = 300
	b11 = gensim.models.Word2Vec.load('300features_40minwords_10_SKU')
	print "Creating average feature vecs for training skucollection"
    	b12 = fonk2( fonk3(b7), b11, a3 )
    	print "Creating average feature vecs for b8 skucollection"
    	b13 = fonk2( fonk4(b8), b11, a3 )
	print "Query ID, SKU ID, Cosine"
	try:
		a4 = 0
	        for i in b13:
			a5 = 0
			for j in b12:
				a6 = 0.0
				try:
					a6 = cosine_similarity(i,j)
				except:
					pass
				print "%d, %d, %f"  % (a4, a5,a6)
				a5 = a5+1
			a4 = a4+1
	except:
		print "exception"
	        pass