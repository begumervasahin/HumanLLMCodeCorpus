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
def fonk2(b10, b9):
    b2 = process(b10).decode('UTF-8')
    b3 = wordpunct_tokenize(b2)
    b4 = stopwords.words(b9)
    for word in b4:
        if word in b3:
            return False
    return True
def fonk3(b12):
    if not b12:
        print("Please specify the folder for input sample b1.")
        sys.exit(1)
    perform_imports()
    b5 = fonk1(b12)
    a1 = 0
    for sample in b5:
        b6 = os.path.join(b12, sample)
        b7 = os.path.join(b12, sample[:-3] + 'txt')
        remove_stopwords(b8 = b6, out_file=b7)
        b9 = sample.split('.')[0].split('-')[0]
        if fonk2(b10 = b7, b9=b9):
            a1 += 1
    if a1 < len(b5):
        print(f'Test failed for {len(b5) - a1} b1')
    else:
        print('All tests passed')
    for sample in b5:
        try:
            os.remove(os.path.join(b12, sample[:-3] + 'txt'))
        except FileNotFoundError:
            pass
if b11 = = '__main__':
    fonk3(b12 = 'input_files')