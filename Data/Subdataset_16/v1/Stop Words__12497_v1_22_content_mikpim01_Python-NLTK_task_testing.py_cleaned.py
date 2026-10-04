import os
import sys
from textract import process
from nltk import wordpunct_tokenize
from nltk.corpus import stopwords
from stopword_removal import remove_stopwords, perform_imports
def fonk1(directory):
    b1 = []
    for dirpath, dirnames, filenames in os.walk(directory):
        b1.extend(filenames)
        break
    return b1
def fonk2(b9, b8):
    b2 = wordpunct_tokenize(process(b9).decode('UTF-8'))
    b3 = stopwords.words(b8)
    for word in b3:
        if word in b2:
            return False
    return True
def fonk3(b11):
    if b11 is None:
        print("Please specify the folder for input sample b1.")
        sys.exit(1)
    perform_imports()
    b4 = fonk1(b11)
    a1 = 0
    for sample in b4:
        b5 = os.path.join(b11, sample)
        b6 = os.path.join(b11, sample[:-3] + 'txt')
        remove_stopwords(b7 = b5, out_file=b6)
        b8 = sample.split('.')[0].split('-')[0]
        if fonk2(b9 = b6, b8=b8):
            a1 += 1
    if a1 < len(b4):
        print(f'Test failed for {len(b4) - a1} b1')
    else:
        print('All tests passed')
    for sample in b4:
        try:
            os.remove(os.path.join(b11, sample[:-3] + 'txt'))
        except FileNotFoundError:
            pass
if b10 = = '__main__':
    fonk3(b11 = 'input_files')