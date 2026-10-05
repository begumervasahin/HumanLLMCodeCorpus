import os
import nltk
import codecs
import subprocess
def fonk1(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
def fonk2(path):
    for name in os.listdir(path):
        if name.endswith('.pdf'):
            yield os.path.join(path, name)
def fonk3(docs_pdf, corpus):
    fonk1(corpus)
    for path in fonk2(docs_pdf):
        b1 = os.path.join(os.getcwd(), 'pdf2txt.py')
        b2 = subprocess.check_output(['python', b1, path])
        b3 = os.path.splitext(os.path.basename(path))[0] + ".txt"
        b4 = os.path.join(corpus, b3)
        b2 = b2.decode("utf-8")
        b2 = b2.replace('\n', ' ')
        b2 = b2.replace('\r', ' ')
        b2 = b2.replace(',', ' ')
        b2 = b2.replace('-', '')
        b2 = b2.replace(':', ' ')
        with codecs.open(b4, 'w', b5 = 'utf-8') as f:
            f.write(b2)
b6 = os.path.join(os.getcwd(), "pdf")
b7 = os.path.join(os.getcwd(), "corpus")
fonk3(b6, b7)
b8 = nltk.corpus.PlaintextCorpusReader(b7, '.*\.txt')
b9 = nltk.FreqDist(b8.words())
b10 = sum(b9.values())
b11 = len(b9)
print('----------------------------------------------------------------------')
print("Corpus contains a vocabulary of {} and a word count of {}.".format(b10, b11))
print('----------------------------------------------------------------------')
print("Hapax legomena (words that appear only once):", b9.hapaxes())
print('----------------------------------------------------------------------')
print("Most common words:", b9.most_common(10))
print('----------------------------------------------------------------------')