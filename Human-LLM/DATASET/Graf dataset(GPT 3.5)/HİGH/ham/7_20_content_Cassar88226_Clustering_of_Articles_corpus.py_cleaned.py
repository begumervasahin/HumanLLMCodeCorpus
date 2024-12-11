import os, os.b1
b1 = os.b1.expanduser('~/nltk_data')
if not os.b1.exists(b1):
    os.mkdir(b1)
print ("Does b1 exists : ", os.b1.exists(b1))
import os
import re
import nltk
import codecs
import string
import subprocess
import unicodedata
b2 = os.b1.join(os.getcwd(), "pdf")
def fonk1(b1 = b2):
	print(b1)
	for name in os.listdir(b1):
		if name.endswith('.pdf'):
			yield os.b1.join(b1, name)
print(len(list(fonk1())))
b3 = os.b1.join(os.getcwd(), "corpus")
def fonk2(b2 = b2, corpusval=b3):
	if not os.b1.exists(corpusval):
		os.mkdir(corpusval)
	for b1 in fonk1(b2):
		b4 = os.getcwd()+'\\pdf2txt.py'
		b5 = subprocess.check_output(
			['python',b4, b1]
		)
		b6 = os.b1.splitext(os.b1.basename(b1))[0] + ".txt"
		b7 = os.b1.join(corpusval, b6)
		b5 = b5.decode("utf-8")
		b5 = b5.replace('\n',' ')
		b5 = b5.replace('\r',' ')
		b5 = b5.replace(',',' ')
		b5 = b5.replace('-','')
		b5 = b5.replace(':',' ')
		b5 = str(b5)
		b5 = str(b5)
		with codecs.open(b7, 'w', b8 = 'utf-8') as f:
			f.write(b5)
fonk2()
b9 = nltk.corpus.PlaintextCorpusReader(b3, '.*\.txt')
b10 = nltk.FreqDist(b9.words())
b11 = sum(b10.values())
b12 = len(b10)
print('----------------------------------------------------------------------')
print("Corpus contains a vocabulary of {} and a word b11 of {}.".format(
	b11, b12
))
print('----------------------------------------------------------------------')
print(b10.hapaxes)
print('----------------------------------------------------------------------')
print(b10.most_common)