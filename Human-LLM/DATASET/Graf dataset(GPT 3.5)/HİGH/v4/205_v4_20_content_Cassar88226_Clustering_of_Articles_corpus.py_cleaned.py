import os
import subprocess
import codecs
import nltk
b1 = os.path.expanduser('~/nltk_data')
if not os.path.exists(b1):
    os.mkdir(b1)
def fonk1(path):
    for name in os.listdir(path):
        if name.endswith('.pdf'):
            yield os.path.join(path, name)
b2 = os.path.join(os.getcwd(), "pdf")
b3 = os.path.join(os.getcwd(), "corpus")
def fonk2(pdf_path, b3):
    if not os.path.exists(b3):
        os.mkdir(b3)
    for path in fonk1(pdf_path):
        b4 = os.path.join(os.getcwd(), 'pdf2txt.py')
        b5 = subprocess.check_output(['python', b4, path])
        b5 = b5.decode("utf-8")
        b5 = b5.replace('\n', ' ')
        b5 = b5.replace('\r', ' ')
        b5 = b5.replace(',', ' ')
        b5 = b5.replace('-', '')
        b5 = b5.replace(':', ' ')
        b5 = str(b5)
        b6 = os.path.splitext(os.path.basename(path))[0] + ".txt"
        b7 = os.path.join(b3, b6)
        with codecs.open(b7, 'w', b8 = 'utf-8') as f:
            f.write(b5)
fonk2(b2, b3)
b9 = nltk.corpus.PlaintextCorpusReader(b3, '.*\.txt')
b10 = nltk.FreqDist(b9.words())
b11 = sum(b10.values())
b12 = len(b10)
print('----------------------------------------------------------------------')
print("Corpus contains a vocabulary of {} and a word count of {}.".format(b11, b12))
print('----------------------------------------------------------------------')
print("Hapax legomena (words that appear only once):", b10.hapaxes())
print('----------------------------------------------------------------------')
print("Most common words:", b10.most_common())
print('----------------------------------------------------------------------')