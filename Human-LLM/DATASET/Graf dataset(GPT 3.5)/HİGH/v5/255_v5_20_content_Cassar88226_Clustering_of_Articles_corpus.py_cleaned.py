import os
import subprocess
import codecs
import nltk
b1 = os.path.expanduser('~/nltk_data')
if not os.path.exists(b1):
    os.mkdir(b1)
def fonk1(directory):
    for b6 in os.listdir(directory):
        if b6.endswith('.pdf'):
            yield os.path.join(directory, b6)
b2 = os.path.join(os.getcwd(), "pdf")
b3 = os.path.join(os.getcwd(), "corpus")
def fonk2(b2, b3):
    if not os.path.exists(b3):
        os.mkdir(b3)
    for pdf_path in fonk1(b2):
        b4 = os.path.join(os.getcwd(), 'pdf2txt.py')
        b5 = subprocess.check_output(['python', b4, pdf_path])
        b5 = b5.decode("utf-8")
        b5 = b5.replace('\n', ' ')
        b5 = b5.replace('\r', ' ')
        b5 = b5.replace(',', ' ')
        b5 = b5.replace('-', '')
        b5 = b5.replace(':', ' ')
        b6 = os.path.splitext(os.path.basename(pdf_path))[0] + ".txt"
        b7 = os.path.join(b3, b6)
        with codecs.open(b7, 'w', b8 = 'utf-8') as file:
            file.write(b5)
fonk2(b2, b3)
b9 = nltk.corpus.PlaintextCorpusReader(b3, '.*\.txt')
b10 = nltk.FreqDist(b9.words())
b11 = sum(b10.values())
b12 = len(b10)
print('----------------------------------------------------------------------')
print("Corpus contains a vocabulary of {} words and a total word count of {}.".format(b12, b11))
print('----------------------------------------------------------------------')
print("Hapax legomena (words that appear only once):", b10.hapaxes())
print('----------------------------------------------------------------------')
print("Most common words:", b10.most_common())
print('----------------------------------------------------------------------')