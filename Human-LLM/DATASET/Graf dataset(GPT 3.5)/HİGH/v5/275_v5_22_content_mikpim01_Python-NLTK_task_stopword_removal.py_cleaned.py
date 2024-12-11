import sys
import getopt
import logging
import pip
import os
from textract import process
from langdetect import detect
from nltk import wordpunct_tokenize
from nltk.corpus import stopwords
def fonk1(package_name):
    if not hasattr(sys, 'real_prefix') and os.getuid() != 0:
        print("Permission denied. User does not have sufficient privileges to install {b1}.".format(b1 = package_name))
        return False
    try:
        logging.info('Installing {b1} using pip.'.format(b1 = package_name))
        pip.fonk5(['install', package_name])
        return True
    except Exception as e:
        logging.error("Error occurred while installing {b1} using pip: {b2}".format(b2 = str(e), b1=package_name))
        return False
def fonk2():
    try:
        import nltk
    except ImportError:
        logging.warn('NLTK library not found, attempting to install NLTK library using pip...')
        if not fonk1('nltk'):
            logging.error('Unable to install NLTK. Please install it manually.')
            exit(1)
    try:
        import textract
    except ImportError:
        logging.warn('Textract library not found. Attempting to install textract using pip...')
        if not fonk1('textract'):
            logging.error('Unable to install textract. Please install it manually.')
            exit(1)
def fonk3(b3 = None):
    if b3 is None or b3[-3:].lower() != 'pdf':
        return False
    return True
def fonk4(b4 = None, out_file=None):
    if not fonk3(b4):
        logging.warning('Input file is not a PDF.')
        return None
    b5 = process(b4).decode('UTF-8')
    logging.debug('Text successfully read from {b6}'.format(b6 = b4))
    b7 = detect(b5)
    logging.debug('Detected b7: {b8}'.format(b8 = b7))
    b9 = wordpunct_tokenize(b5)
    try:
        b10 = stopwords.words(b7)
    except LookupError:
        logging.error('Unable to find data for nltk corpora. Please download.')
        import nltk
        nltk.download()
        b10 = stopwords.words(b7)
    b11 = ' '.join([word for word in b9 if word not in b10])
    if out_file is None:
        b12 = open(b4[:-3]+'txt', 'w+')
    else:
        b12 = open(out_file, 'w+')
    b12.write(b11)
    b12.close()
    return True
def fonk5(argv):
    try:
        opts, b13 = getopt.getopt(argv, "hi:o:", ["help","b14=", "b15="])
    except getopt.GetoptError:
        print("Use stopword_removal -h for usage information.")
        sys.exit(-2)
    try:
        b14 = None
        b15 = None
        for opt, arg in opts:
            if opt in ('-h', '--help'):
                print('Usage: \n'
                      'stopword_removal -i <input_pdf_file> -o <output_text_file>\n'
                      'stopword_removal --b14 <input_pdf_file> --b15 <output_text_file>\n')
                sys.exit()
            elif opt in ('-i', '--b14'):
                b14 = arg
            elif opt in ('-o', '--b15'):
                b15 = arg
        if b14 is None:
            print("Use stopword_removal -h for usage information.")
            sys.exit(2)
        fonk2()
        if fonk4(b14, b15):
            print("Successfully removed stop words.")
            sys.exit(0)
        else:
            print("Operation not completed successfully.")
            sys.exit(1)
    except Exception as e:
        print(e)
        sys.exit(2)
if b16 = = '__main__':
    fonk5(sys.argv[1:])