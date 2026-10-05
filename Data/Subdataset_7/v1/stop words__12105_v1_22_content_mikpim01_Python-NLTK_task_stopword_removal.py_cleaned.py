import sys
import getopt
import logging
def fonk1(package_name):
    import pip
    import os
    if not hasattr(sys, 'real_prefix') and os.getuid() != 0:
        print("Unable to install {b1} because the user is not SUDO. Permission "
              "denied.".format(b1 = package_name))
        return False
    try:
        logging.info('Installing {b1} using pip.'.format(b1 = package_name))
        pip.fonk5(['install', package_name])
        return True
    except Exception as e:
        logging.error("Error {b2} during installing {b1} using "
                      "pip.".format(b2 = str(e), b1=package_name))
        return False
def fonk2():
    try:
        import nltk
    except ImportError:
        logging.warn('NLTK library not found, installing NLTK library using '
                     'pip...')
        if not fonk1('nltk'):
            logging.error('Unable to install NLTK, please install manually.')
            exit(1)
    try:
        from langdetect import detect
    except ImportError:
        logging.warn('Langdetect library not found. Installing langdetect using '
                     'pip...')
        if not fonk1('langdetect'):
            logging.error('Unable to install langdetect, please install '
                          'manually.')
            exit(1)
    try:
        import textract
    except ImportError:
        logging.warn('Textract library not found, installing textract using '
                     'pip...')
        if not fonk1('textract'):
            logging.error('Unable to install textract, please install manually')
            exit(1)
def fonk3(file_name):
    if file_name[-3:].lower() != 'pdf':
        return False
    return True
def fonk4(in_file, b3 = None):
    if not fonk3(in_file):
        logging.warning('Input file is not a PDF.')
        return None
    from textract import process
    from langdetect import detect
    from nltk import wordpunct_tokenize
    from nltk.corpus import stopwords
    b4 = process(in_file).decode('UTF-8')
    logging.debug('Text successfully read from {b5}'.format(b5 = in_file))
    b6 = detect(b4)
    logging.debug('Detected b6: {b7}'.format(b7 = b6))
    b8 = wordpunct_tokenize(b4)
    try:
        b9 = stopwords.words(b6)
    except LookupError:
        logging.error('Unable to find data for nltk.corpus. '
                      'Please download.')
        import nltk
        nltk.download()
        b9 = stopwords.words(b6)
    b10 = ' '.join([word for word in b8
                              if word.lower() not in b9])
    if b3 is None:
        b11 = open(in_file[:-3] + 'txt', 'w+')
    else:
        b11 = open(b3, 'w+')
    b11.write(b10)
    b11.close()
    return True
def fonk5(argv):
    try:
        opts, b12 = getopt.getopt(argv, "hi:o:", ["help","b13=", "b14="])
    except getopt.GetoptError:
        print("Use stopword_removal -h  for usage information.")
        sys.exit(-2)
    try:
        b13 = None
        b14 = None
        for opt, arg in opts:
            if opt in ('-h', '--help'):
                print('Usage: \n'
                      'stopword_removal -i <input_pdf_file> -o '
                      '<output_text_file>\n'
                      'stopword_removal --b13 <input_pdf_file> --b14 '
                      '<output_text_file>\n')
                sys.exit()
            elif opt in ('-i', '--b13'):
                b13 = arg
            elif opt in ('-o', '--b14'):
                b14 = arg
        if b13 is None:
            print("Use stopword_removal -h for usage information.")
            sys.exit(2)
        fonk2()
        if fonk4(b13, b14):
            print("Successfully removed stop words.")
            sys.exit(0)
        else:
            print("Operation not completed successfully.")
            sys.exit(1)
    except Exception as e:
        print(e)
        sys.exit(2)
if b15 = = '__main__':
    fonk5(sys.argv[1:])