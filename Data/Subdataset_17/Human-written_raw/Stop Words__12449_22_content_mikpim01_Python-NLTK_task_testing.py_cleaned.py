import os
import sys
from stopword_removal import remove_stopwords, perform_imports
def get_filenames_from_directory(directory):
    from os import walk
    files = []
    for (dirpath, dirnames, filenames) in walk(directory):
        files.extend(filenames)
        break
    return files
def verify_no_stopwords(infile=None, language=None):
    from textract import process
    from nltk import wordpunct_tokenize
    from nltk.corpus import stopwords
    tokens = wordpunct_tokenize(process(infile).decode('UTF-8'))
    stop_words = stopwords.words(language)
    for word in stop_words:
        if word in tokens:
            return False
    return True
def run_test(input_folder=None):
    if input_folder is None:
        print("Please specify the folder for input_sample_pdf files.")
        sys.exit(1)
    perform_imports()
    samples = get_filenames_from_directory(input_folder)
    count = 0
    for sample in samples:
        remove_stopwords(in_file=input_folder+'/'+sample,
                         out_file=input_folder+'/'+sample[:-3]+'txt')
        count += 1 if verify_no_stopwords(
            infile=input_folder+'/'+sample[:-3]+'txt',
            language=sample.split('.')[0].split('-')[0]) else 0
    if count < len(samples):
        print('Test failed for {failed} languages'.format(failed=count))
    else:
        print('All tests passed')
    for sample in samples:
        try:
            os.remove(input_folder+'/'+sample[:-3]+'txt')
        except FileNotFoundError:
            pass
if __name__ == '__main__':
    run_test(input_folder='input_files')