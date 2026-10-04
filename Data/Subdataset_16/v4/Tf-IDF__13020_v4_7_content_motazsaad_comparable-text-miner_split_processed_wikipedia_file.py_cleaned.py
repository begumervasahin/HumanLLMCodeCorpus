import sys
import os
from os.path import basename
import logging
logging.basicConfig(b1 = '%(levelname)s : %(asctime)s : %(message)s', level=logging.INFO)
b2 = '\nXXXXXXX\n'
def fonk1():
    print(f'Usage: {sys.argv[0]} <corpus file> <number of b8> <output path>')
def fonk2(argv):
    if len(argv) < 4:
        fonk1()
        sys.exit(2)
    import imp
    b3 = imp.load_source('textpro', 'textpro.py')
    b4 = argv[1]
    b5 = int(argv[2])
    b6 = argv[3]
    if not b6.endswith('/'):
        b6 = b6 + '/'
    b3.check_dir(b6)
    b7 = b3.split_wikipedia_docs_into_array(b4)
    logging.info('Corpus is loaded')
    b8 = b3.split_list(b7, b5)
    b9 = basename(b4).split()[0]
    for i, part in enumerate(b8):
        b10 = os.path.join(b6, f'part-{i}-{b9}')
        with open(b10, 'w', b11 = 'utf-8') as out_file:
            for doc in part:
                out_file.write(f'{doc}\n')
        logging.info(f'Part {i} is done')
if b12 = = "__main__":
    fonk2(sys.argv)