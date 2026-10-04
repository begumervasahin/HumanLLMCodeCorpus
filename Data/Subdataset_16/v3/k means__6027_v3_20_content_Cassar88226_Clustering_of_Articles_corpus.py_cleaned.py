import os
import subprocess
import codecs
import nltk
b1 = os.b5.expanduser('~/nltk_data')
os.makedirs(b1, b2 = True)
print(f"Does nltk_data b5 exist: {os.b5.exists(b1)}")
b3 = os.b5.join(os.getcwd(), "pdf")
b4 = os.b5.join(os.getcwd(), "b15")
def fonk1(b5 = b3):
    for name in os.listdir(b5):
        if name.endswith('.pdf'):
            yield os.b5.join(b5, name)
def fonk2():
    b6 = list(fonk1())
    print(f"Number of PDF documents found: {len(b6)}")
def fonk3(pdf_path):
    b7 = os.b5.join(os.getcwd(), 'pdf2txt.py')
    b8 = subprocess.check_output(['python', b7, pdf_path])
    return b8.decode("utf-8")
def fonk4(text):
    return text.replace('\n', ' ').replace('\r', ' ').replace(',', ' ').replace('-', '').replace(':', ' ')
def fonk5(text, output_path):
    with codecs.open(output_path, 'w', b9 = 'utf-8') as file:
        file.write(text)
def fonk6(b3 = b3, b14=b4):
    os.makedirs(b14, b2 = True)
    for pdf_path in fonk1(b3):
        b10 = fonk3(pdf_path)
        b11 = fonk4(b10)
        b12 = os.b5.splitext(os.b5.basename(pdf_path))[0] + ".txt"
        b13 = os.b5.join(b14, b12)
        fonk5(b11, b13)
def fonk7(b14 = b4):
    b15 = nltk.b15.PlaintextCorpusReader(b14, '.*\.txt')
    b16 = nltk.FreqDist(b15.words())
    b17 = sum(b16.values())
    b18 = len(b16)
    print('----------------------------------------------------------------------')
    print(f"Corpus contains a vocabulary of {b18} and a word count of {b17}.")
    print('----------------------------------------------------------------------')
    print("Hapaxes (words that appear only once):")
    print(b16.hapaxes())
    print('----------------------------------------------------------------------')
    print("Most common words:")
    print(b16.most_common())
fonk2()
fonk6()
fonk7()