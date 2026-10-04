import os
import sys
from textract import process
from nltk import wordpunct_tokenize
from nltk.corpus import stopwords
from stopword_removal import remove_stopwords, perform_imports
def get_filenames_from_directory(directory):
    files = []
    for dirpath, dirnames, filenames in os.walk(directory):
        files.extend(filenames)
        break
    return files
def verify_no_stopwords(infile, language):
    text = process(infile).decode('UTF-8')
    tokens = wordpunct_tokenize(text)
    stop_words = stopwords.words(language)
    for word in stop_words:
        if word in tokens:
            return False
    return True
def run_test(input_folder):
    if not input_folder:
        print("Please specify the folder for input sample files.")
        sys.exit(1)
    perform_imports()
    samples = get_filenames_from_directory(input_folder)
    count = 0
    for sample in samples:
        input_file = os.path.join(input_folder, sample)
        output_file = os.path.join(input_folder, sample[:-3] + 'txt')
        remove_stopwords(in_file=input_file, out_file=output_file)
        language = sample.split('.')[0].split('-')[0]
        if verify_no_stopwords(infile=output_file, language=language):
            count += 1
    if count < len(samples):
        print(f'Test failed for {len(samples) - count} files')
    else:
        print('All tests passed')
    for sample in samples:
        try:
            os.remove(os.path.join(input_folder, sample[:-3] + 'txt'))
        except FileNotFoundError:
            pass
if __name__ == '__main__':
    run_test(input_folder='input_files')