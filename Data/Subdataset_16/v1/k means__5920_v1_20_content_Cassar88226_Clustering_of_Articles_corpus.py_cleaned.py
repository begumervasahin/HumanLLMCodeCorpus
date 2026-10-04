import os
import re
import nltk
import codecs
import string
import subprocess
import unicodedata
b1 = os.b4.expanduser('~/nltk_data')
if not os.b4.exists(b1):
    os.mkdir(b1)
print("Does nltk_data b4 exist:", os.b4.exists(b1))
b2 = os.b4.join(os.getcwd(), "pdf")
b3 = os.b4.join(os.getcwd(), "corpus")
def fonk1(b4 = b2):
    for name in os.listdir(b4):
        if name.endswith('.pdf'):
            yield os.b4.join(b4, name)
print(len(list(fonk1())))
def fonk2(b2 = b2, corpusval=b3):
    if not os.b4.exists(corpusval):
        os.mkdir(corpusval)
    for b4 in fonk1(b2):
        b5 = os.b4.join(os.getcwd(), 'pdf2txt.py')
        b6 = subprocess.check_output(['python', b5, b4])
        b7 = os.b4.splitext(os.b4.basename(b4))[0] + ".txt"
        b8 = os.b4.join(corpusval, b7)
        b6 = b6.decode("utf-8")
        b6 = b6.replace('\n', ' ')
        b6 = b6.replace('\r', ' ')
        b6 = b6.replace(',', ' ')
        b6 = b6.replace('-', '')
        b6 = b6.replace(':', ' ')
        with codecs.open(b8, 'w', b9 = 'utf-8') as f:
            f.write(b6)
fonk2()
b10 = nltk.corpus.PlaintextCorpusReader(b3, '.*\.txt')
b11 = nltk.FreqDist(b10.words())
b12 = sum(b11.values())
b13 = len(b11)
print('----------------------------------------------------------------------')
print("Corpus contains a vocabulary of {} and a word b12 of {}.".format(b13, b12))
print('----------------------------------------------------------------------')
print(b11.hapaxes())
print('----------------------------------------------------------------------')
print(b11.most_common())