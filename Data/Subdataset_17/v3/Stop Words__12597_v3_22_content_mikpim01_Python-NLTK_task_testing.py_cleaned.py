import os
import sys
from textract import process
from nltk import wordpunct_tokenize
from nltk.corpus import stopwords
from stopword_removal import remove_stopwords, perform_imports
def get_filenames_from_directory(directory):
    for dirpath, dirnames, filenames in os.walk(directory):
        return filenames
    return []
def verify_no_stopwords(infile, language):
    try:
        text = process(infile).decode('UTF-8')
    except Exception as e:
        print(f"Error processing file {infile}: {e}")
        return False
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
        output_file = os.path.join(input_folder, sample.rsplit('.', 1)[0] + '.txt')
        remove_stopwords(in_file=input_file, out_file=output_file)
        language = sample.split('-')[0]
        if verify_no_stopwords(infile=output_file, language=language):
            count += 1
    total_samples = len(samples)
    failed_tests = total_samples - count
    if failed_tests > 0:
        print(f'Test failed for {failed_tests} files')
    else:
        print('All tests passed')
    for sample in samples:
        output_file = os.path.join(input_folder, sample.rsplit('.', 1)[0] + '.txt')
        try:
            os.remove(output_file)
        except FileNotFoundError:
            pass
if __name__ == '__main__':
    run_test(input_folder='input_files')