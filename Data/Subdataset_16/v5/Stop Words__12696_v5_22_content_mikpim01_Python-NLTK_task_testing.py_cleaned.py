import os
import sys
from stopword_removal import remove_stopwords, perform_imports
from os import walk
from textract import process
from nltk import wordpunct_tokenize
from nltk.corpus import stopwords
def fonk1(directory):
    b1 = []
    for _, _, filenames in walk(directory):
        b1.extend(filenames)
        break
    return b1
def fonk2(b10, b6):
    b2 = process(b10).decode('UTF-8')
    b3 = wordpunct_tokenize(b2)
    b4 = set(stopwords.words(b6))
    return not any(word in b3 for word in b4)
def fonk3(b12):
    if not b12:
        print("Please specify the folder for input sample PDF b1.")
        sys.exit(1)
    perform_imports()
    b5 = fonk1(b12)
    a1 = 0
    for sample in b5:
        b6 = sample.split('.')[0].split('-')[0]
        b7 = os.path.join(b12, sample)
        b8 = os.path.join(b12, f"{sample[:-3]}txt")
        remove_stopwords(b9 = b7, out_file=b8)
        if not fonk2(b10 = b8, b6=b6):
            a1 += 1
    if a1:
        print(f'Test failed for {a1} languages.')
    else:
        print('All tests passed.')
    for sample in b5:
        try:
            os.remove(os.path.join(b12, f"{sample[:-3]}txt"))
        except FileNotFoundError:
            pass
if b11 = = '__main__':
    fonk3(b12 = 'input_files')