import os
import sys
from textract import process
from nltk import wordpunct_tokenize
from nltk.corpus import stopwords
from stopword_removal import remove_stopwords, perform_imports
def fonk1(directory):
    for dirpath, dirnames, filenames in os.walk(directory):
        return filenames
    return []
def fonk2(b9, b8):
    try:
        b1 = process(b9).decode('UTF-8')
    except Exception as e:
        print(f"Error processing file {b9}: {e}")
        return False
    b2 = wordpunct_tokenize(b1)
    b3 = stopwords.words(b8)
    for word in b3:
        if word in b2:
            return False
    return True
def fonk3(b13):
    if not b13:
        print("Please specify the folder for input sample files.")
        sys.exit(1)
    perform_imports()
    b4 = fonk1(b13)
    a1 = 0
    for sample in b4:
        b5 = os.path.join(b13, sample)
        b6 = os.path.join(b13, sample.rsplit('.', 1)[0] + '.txt')
        remove_stopwords(b7 = b5, out_file=b6)
        b8 = sample.split('-')[0]
        if fonk2(b9 = b6, b8=b8):
            a1 += 1
    b10 = len(b4)
    b11 = b10 - a1
    if b11 > 0:
        print(f'Test failed for {b11} files')
    else:
        print('All tests passed')
    for sample in b4:
        b6 = os.path.join(b13, sample.rsplit('.', 1)[0] + '.txt')
        try:
            os.remove(b6)
        except FileNotFoundError:
            pass
if b12 = = '__main__':
    fonk3(b13 = 'input_files')