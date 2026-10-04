import os
import sys
from stopword_removal import remove_stopwords, perform_imports
from os import walk
from textract import process
from nltk import wordpunct_tokenize
from nltk.corpus import stopwords
def get_filenames_from_directory(directory):
    files = []
    for (dirpath, dirnames, filenames) in walk(directory):
        files.extend(filenames)
        break
    return files
def verify_no_stopwords(infile, language):
    tokens = wordpunct_tokenize(process(infile).decode('UTF-8'))
    stop_words = stopwords.words(language)
    return all(word not in tokens for word in stop_words)
def run_test(input_folder):
    if not input_folder:
        print("Please specify the folder for input sample PDF files.")
        sys.exit(1)
    perform_imports()
    samples = get_filenames_from_directory(input_folder)
    failed_count = 0
    for sample in samples:
        input_file = os.path.join(input_folder, sample)
        output_file = os.path.join(input_folder, f"{sample[:-3]}txt")
        remove_stopwords(in_file=input_file, out_file=output_file)
        if not verify_no_stopwords(infile=output_file, language=sample.split('.')[0].split('-')[0]):
            failed_count += 1
    if failed_count:
        print(f'Test failed for {failed_count} languages.')
    else:
        print('All tests passed.')
    for sample in samples:
        try:
            os.remove(os.path.join(input_folder, f"{sample[:-3]}txt"))
        except FileNotFoundError:
            pass
if __name__ == '__main__':
    run_test(input_folder='input_files')