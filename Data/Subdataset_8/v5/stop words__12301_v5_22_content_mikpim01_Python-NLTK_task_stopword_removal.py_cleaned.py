import sys
import getopt
import logging
import pip
import os
from textract import process
from langdetect import detect
from nltk import wordpunct_tokenize
from nltk.corpus import stopwords
def install_package(package_name):
    if not hasattr(sys, 'real_prefix') and os.getuid() != 0:
        print("Permission denied. User does not have sufficient privileges to install {pkg}.".format(pkg=package_name))
        return False
    try:
        logging.info('Installing {pkg} using pip.'.format(pkg=package_name))
        pip.main(['install', package_name])
        return True
    except Exception as e:
        logging.error("Error occurred while installing {pkg} using pip: {err}".format(err=str(e), pkg=package_name))
        return False
def perform_imports():
    try:
        import nltk
    except ImportError:
        logging.warn('NLTK library not found, attempting to install NLTK library using pip...')
        if not install_package('nltk'):
            logging.error('Unable to install NLTK. Please install it manually.')
            exit(1)
    try:
        import textract
    except ImportError:
        logging.warn('Textract library not found. Attempting to install textract using pip...')
        if not install_package('textract'):
            logging.error('Unable to install textract. Please install it manually.')
            exit(1)
def is_pdf(file_name=None):
    if file_name is None or file_name[-3:].lower() != 'pdf':
        return False
    return True
def remove_stopwords(in_file=None, out_file=None):
    if not is_pdf(in_file):
        logging.warning('Input file is not a PDF.')
        return None
    text = process(in_file).decode('UTF-8')
    logging.debug('Text successfully read from {ifile}'.format(ifile=in_file))
    language = detect(text)
    logging.debug('Detected language: {lang}'.format(lang=language))
    tokens = wordpunct_tokenize(text)
    try:
        stop_words = stopwords.words(language)
    except LookupError:
        logging.error('Unable to find data for nltk corpora. Please download.')
        import nltk
        nltk.download()
        stop_words = stopwords.words(language)
    filtered_text = ' '.join([word for word in tokens if word not in stop_words])
    if out_file is None:
        output_file = open(in_file[:-3]+'txt', 'w+')
    else:
        output_file = open(out_file, 'w+')
    output_file.write(filtered_text)
    output_file.close()
    return True
def main(argv):
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["help","infile=", "outfile="])
    except getopt.GetoptError:
        print("Use stopword_removal -h for usage information.")
        sys.exit(-2)
    try:
        infile = None
        outfile = None
        for opt, arg in opts:
            if opt in ('-h', '--help'):
                print('Usage: \n'
                      'stopword_removal -i <input_pdf_file> -o <output_text_file>\n'
                      'stopword_removal --infile <input_pdf_file> --outfile <output_text_file>\n')
                sys.exit()
            elif opt in ('-i', '--infile'):
                infile = arg
            elif opt in ('-o', '--outfile'):
                outfile = arg
        if infile is None:
            print("Use stopword_removal -h for usage information.")
            sys.exit(2)
        perform_imports()
        if remove_stopwords(infile, outfile):
            print("Successfully removed stop words.")
            sys.exit(0)
        else:
            print("Operation not completed successfully.")
            sys.exit(1)
    except Exception as e:
        print(e)
        sys.exit(2)
if __name__ == '__main__':
    main(sys.argv[1:])