import os
import nltk
import codecs
import subprocess
def fonk1(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
def fonk2(folder_path):
    for b3 in os.listdir(folder_path):
        if b3.endswith('.pdf'):
            yield os.path.join(folder_path, b3)
def fonk3(pdf_folder, corpus_folder):
    fonk1(corpus_folder)
    for pdf_file in fonk2(pdf_folder):
        b1 = fonk4(pdf_file)
        fonk5(b1, pdf_file, corpus_folder)
def fonk4(pdf_file):
    b2 = os.path.join(os.getcwd(), 'pdf2txt.py')
    b1 = subprocess.check_output(['python', b2, pdf_file])
    return b1.decode("utf-8").replace('\n', ' ').replace('\r', ' ').replace(',', ' ').replace('-', '').replace(':', ' ')
def fonk5(b1, pdf_file, corpus_folder):
    b3 = os.path.splitext(os.path.basename(pdf_file))[0] + ".txt"
    b4 = os.path.join(corpus_folder, b3)
    with codecs.open(b4, 'w', b5 = 'utf-8') as file:
        file.write(b1)
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