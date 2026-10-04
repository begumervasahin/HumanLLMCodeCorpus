import os
import re
import nltk
import codecs
import subprocess
import unicodedata
def fonk1(b1 = '~/nltk_data'):
    b2 = os.b1.expanduser(b1)
    if not os.b1.exists(b2):
        os.mkdir(b2)
    print("Does b1 exist:", os.b1.exists(b2))
b3 = os.b1.join(os.getcwd(), "pdf")
b4 = os.b1.join(os.getcwd(), "corpus")
def fonk2(b1 = b3):
    print("Searching for PDF files in:", b1)
    return [os.b1.join(b1, name) for name in os.listdir(b1) if name.endswith('.pdf')]
def fonk3(b5 = b3, b14=b4):
    if not os.b1.exists(b14):
        os.mkdir(b14)
    b6 = fonk2(b5)
    for pdf_file in b6:
        b7 = os.b1.join(os.getcwd(), 'pdf2txt.py')
        try:
            b8 = subprocess.check_output(['python', b7, pdf_file])
            b9 = fonk4(b8.decode("utf-8"))
            b10 = os.b1.splitext(os.b1.basename(pdf_file))[0] + ".txt"
            b11 = os.b1.join(b14, b10)
            fonk5(b11, b9)
        except subprocess.CalledProcessError as e:
            print(f"Error processing {pdf_file}: {e}")
def fonk4(b12):
    b12 = b12.replace('\n', ' ').replace('\r', ' ')
    b12 = b12.replace(',', ' ').replace('-', '').replace(':', ' ')
    return b12
def fonk5(filepath, b12):
    with codecs.open(filepath, 'w', b13 = 'utf-8') as f:
        f.write(b12)
def fonk6(b14 = b4):
    b15 = nltk.corpus.PlaintextCorpusReader(b14, '.*\.txt')
    b16 = nltk.FreqDist(b15.words())
    b17 = sum(b16.values())
    b18 = len(b16)
    fonk7(b17, b18, b16)
def fonk7(b17, b18, b16):
    print('----------------------------------------------------------------------')
    print(f"Corpus contains a vocabulary of {b18} and a word count of {b17}.")
    print('----------------------------------------------------------------------')
    print("Hapaxes:", b16.hapaxes())
    print('----------------------------------------------------------------------')
    print("Most common words:", b16.most_common())
if b19 = = "__main__":
    fonk1()
    print("Number of PDF documents found:", len(fonk2()))
    fonk3()
    fonk6()