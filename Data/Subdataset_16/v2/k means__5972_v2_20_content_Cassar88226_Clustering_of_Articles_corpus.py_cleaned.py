import os
import subprocess
import codecs
import nltk
b1 = os.b5.expanduser('~/nltk_data')
os.makedirs(b1, b2 = True)
print("Does nltk_data b5 exist:", os.b5.exists(b1))
b3 = os.b5.join(os.getcwd(), "pdf")
b4 = os.b5.join(os.getcwd(), "corpus")
def fonk1(b5 = b3):
    for name in os.listdir(b5):
        if name.endswith('.pdf'):
            yield os.b5.join(b5, name)
b6 = list(fonk1())
print(f"Number of PDF documents found: {len(b6)}")
def fonk2(b3 = b3, corpus_dir=b4):
    os.makedirs(corpus_dir, b2 = True)
    for pdf_path in fonk1(b3):
        b7 = os.b5.join(os.getcwd(), 'pdf2txt.py')
        b8 = subprocess.check_output(['python', b7, pdf_path])
        b9 = os.b5.splitext(os.b5.basename(pdf_path))[0] + ".txt"
        b10 = os.b5.join(corpus_dir, b9)
        b11 = b8.decode("utf-8").replace('\n', ' ').replace('\r', ' ')
        b11 = b11.replace(',', ' ').replace('-', '').replace(':', ' ')
        with codecs.open(b10, 'w', b12 = 'utf-8') as f:
            f.write(b11)
fonk2()
b13 = nltk.corpus.PlaintextCorpusReader(b4, '.*\.txt')
b14 = nltk.FreqDist(b13.words())
b15 = sum(b14.values())
b16 = len(b14)
print('----------------------------------------------------------------------')
print(f"Corpus contains a vocabulary of {b16} and a word count of {b15}.")
print('----------------------------------------------------------------------')
print("Hapaxes (words that appear only once):")
print(b14.hapaxes())
print('----------------------------------------------------------------------')
print("Most common words:")
print(b14.most_common())