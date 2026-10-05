import os, os.path
path = os.path.expanduser('~/nltk_data')
if not os.path.exists(path):
    os.mkdir(path)
print ("Does path exists : ", os.path.exists(path))
import os
import re
import nltk
import codecs
import string
import subprocess
import unicodedata
DOCS_PDF = os.path.join(os.getcwd(), "pdf")
def get_pdf_docs(path=DOCS_PDF):
	print(path)
	for name in os.listdir(path):
		if name.endswith('.pdf'):
			yield os.path.join(path, name)
print(len(list(get_pdf_docs())))
CORPUS = os.path.join(os.getcwd(), "corpus")
def extract_pdf_corpus(DOCS_PDF=DOCS_PDF, corpusval=CORPUS):
	if not os.path.exists(corpusval):
		os.mkdir(corpusval)
	for path in get_pdf_docs(DOCS_PDF):
		tp=os.getcwd()+'\\pdf2txt.py'
		document = subprocess.check_output(
			['python',tp, path]
		)
		filen = os.path.splitext(os.path.basename(path))[0] + ".txt"
		outp = os.path.join(corpusval, filen)
		document=document.decode("utf-8")
		document=document.replace('\n',' ')
		document=document.replace('\r',' ')
		document=document.replace(',',' ')
		document=document.replace('-','')
		document=document.replace(':',' ')
		document=str(document)
		document=str(document)
		with codecs.open(outp, 'w', encoding='utf-8') as f:
			f.write(document)
extract_pdf_corpus()
kddcorpus = nltk.corpus.PlaintextCorpusReader(CORPUS, '.*\.txt')
wordsvals = nltk.FreqDist(kddcorpus.words())
count = sum(wordsvals.values())
vocab = len(wordsvals)
print('----------------------------------------------------------------------')
print("Corpus contains a vocabulary of {} and a word count of {}.".format(
	count, vocab
))
print('----------------------------------------------------------------------')
print(wordsvals.hapaxes)
print('----------------------------------------------------------------------')
print(wordsvals.most_common)