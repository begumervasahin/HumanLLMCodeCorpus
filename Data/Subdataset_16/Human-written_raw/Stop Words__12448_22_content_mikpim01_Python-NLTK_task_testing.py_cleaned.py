import os
import sys
from stopword_removal import remove_stopwords, perform_imports
def fonk1(directory):
    from os import walk
    b1 = []
    for (dirpath, dirnames, filenames) in walk(directory):
        b1.extend(filenames)
        break
    return b1
def fonk2(b2 = None, b9=None):
    from textract import process
    from nltk import wordpunct_tokenize
    from nltk.corpus import stopwords
    b3 = wordpunct_tokenize(process(b2).decode('UTF-8'))
    b4 = stopwords.words(b9)
    for word in b4:
        if word in b3:
            return False
    return True
def fonk3(b5 = None):
    if b5 is None:
        print("Please specify the folder for input_sample_pdf b1.")
        sys.exit(1)
    perform_imports()
    b6 = fonk1(b5)
    a1 = 0
    for sample in b6:
        remove_stopwords(b7 = b5+'/'+sample,
                         b8 = b5+'/'+sample[:-3]+'txt')
        a1 += 1 if fonk2(
            b2 = b5+'/'+sample[:-3]+'txt',
            b9 = sample.split('.')[0].split('-')[0]) else 0
    if a1 < len(b6):
        print('Test b10 for {b10} languages'.format(b10 = a1))
    else:
        print('All tests passed')
    for sample in b6:
        try:
            os.remove(b5+'/'+sample[:-3]+'txt')
        except FileNotFoundError:
            pass
if b11 = = '__main__':
    fonk3(b5 = 'input_files')