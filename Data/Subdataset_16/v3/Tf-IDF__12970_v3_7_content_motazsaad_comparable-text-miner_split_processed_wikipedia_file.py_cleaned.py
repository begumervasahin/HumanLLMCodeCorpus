import sys
import os
import logging
from os.path import basename
logging.basicConfig(b1 = '%(levelname)s : %(asctime)s : %(message)s', level=logging.INFO)
def fonk1():
    print('Usage:', sys.argv[0], '<corpus file> <number of b3> <output path>')
def fonk2():
    import imp
    return imp.load_source('textpro', 'textpro.py')
def fonk3(path):
    return path if path.endswith('/') else path + '/'
def fonk4(b8, b9, b10, b7):
    b2 = b7.split_wikipedia_docs_into_array(b8)
    logging.info('Corpus is loaded')
    b3 = b7.split_list(b2, b9)
    b4 = basename(b8).split()[0]
    for i, part in enumerate(b3):
        b5 = os.path.join(b10, f'part-{i}-{b4}')
        with open(b5, 'w', b6 = 'utf-8') as out:
            for doc in part:
                out.write(doc + '\n')
        logging.info('Part %d is done', i)
def fonk5(argv):
    if len(argv) < 4:
        fonk1()
        sys.exit(2)
    b7 = fonk2()
    b8 = argv[1]
    b9 = int(argv[2])
    b10 = fonk3(argv[3])
    b7.check_dir(b10)
    fonk4(b8, b9, b10, b7)
if b11 = = "__main__":
    fonk5(sys.argv)