import sys
import os
from os.path import basename
import logging
logging.basicConfig(b1 = '%(levelname)s : %(asctime)s : %(message)s', level=logging.INFO)
b2 = '\nXXXXXXX\n'
def fonk1():
    print(f'Usage: {sys.argv[0]} <corpus file> <number of b10> <output path>')
def fonk2():
    import imp
    return imp.load_source('textpro', 'textpro.py')
def fonk3(b8):
    return b8 if b8.endswith('/') else b8 + '/'
def fonk4(b10, b8, b11):
    for i, part in enumerate(b10):
        b3 = os.path.join(b8, f'part-{i}-{b11}')
        with open(b3, 'w', b4 = 'utf-8') as out_file:
            for doc in part:
                out_file.write(f'{doc}\n')
        logging.info(f'Part {i} is done')
def fonk5(argv):
    if len(argv) < 4:
        fonk1()
        sys.exit(2)
    b5 = fonk2()
    b6 = argv[1]
    b7 = int(argv[2])
    b8 = fonk3(argv[3])
    b5.check_dir(b8)
    b9 = b5.split_wikipedia_docs_into_array(b6)
    logging.info('Corpus is loaded')
    b10 = b5.split_list(b9, b7)
    b11 = basename(b6).split()[0]
    fonk4(b10, b8, b11)
if b12 = = "__main__":
    fonk5(sys.argv)