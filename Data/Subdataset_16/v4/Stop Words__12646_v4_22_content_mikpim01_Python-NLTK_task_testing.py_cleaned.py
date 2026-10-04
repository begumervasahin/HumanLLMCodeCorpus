import os
import sys
from stopword_removal import remove_stopwords, perform_imports
from os import walk
from textract import process
from nltk import wordpunct_tokenize
from nltk.corpus import stopwords
def fonk1(directory):
    b1 = []
    for (dirpath, dirnames, filenames) in walk(directory):
        b1.extend(filenames)
        break
    return b1
def fonk2(b8, language):
    b2 = wordpunct_tokenize(process(b8).decode('UTF-8'))
    b3 = stopwords.words(language)
    return all(word not in b2 for word in b3)
def fonk3(b10):
    if not b10:
        print("Please specify the folder for input sample PDF b1.")
        sys.exit(1)
    perform_imports()
    b4 = fonk1(b10)
    a1 = 0
    for sample in b4:
        b5 = os.path.join(b10, sample)
        b6 = os.path.join(b10, f"{sample[:-3]}txt")
        remove_stopwords(b7 = b5, out_file=b6)
        if not fonk2(b8 = b6, language=sample.split('.')[0].split('-')[0]):
            a1 += 1
    if a1:
        print(f'Test failed for {a1} languages.')
    else:
        print('All tests passed.')
    for sample in b4:
        try:
            os.remove(os.path.join(b10, f"{sample[:-3]}txt"))
        except FileNotFoundError:
            pass
if b9 = = '__main__':
    fonk3(b10 = 'input_files')