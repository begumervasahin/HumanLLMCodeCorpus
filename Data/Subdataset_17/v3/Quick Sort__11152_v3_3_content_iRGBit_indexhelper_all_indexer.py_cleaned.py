import sys
import string
from collections import Counter
DEFAULT_FILE = 'files/sample.txt'
DEFAULT_STOP_WORDS = 'stop_words.txt'
def main():
    if len(sys.argv) > 3:
        print("\nUsage: python indexer.py <yourFile> <stopWords>")
        print(f"If no arguments are given, {DEFAULT_FILE} and {DEFAULT_STOP_WORDS} will be used as default files\n")
        sys.exit()
    input_file = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_FILE
    stop_words_file = sys.argv[2] if len(sys.argv) > 2 else DEFAULT_STOP_WORDS
    print(f'Using {input_file} as the input file and {stop_words_file} as the stop words reference.\n')
    index_words(input_file, stop_words_file)
def index_words(input_file, stop_words_file):
    book_words = read_and_process_file(input_file)
    stop_words = read_stop_words(stop_words_file)
    filtered_words = filter_stop_words(book_words, stop_words)
    word_counts = count_words(filtered_words)
    print_word_counts(word_counts)
def read_and_process_file(file_path):
    with open(file_path, 'r', encoding='unicode_escape') as file:
        words = file.read().lower().split()
        processed_words = [word.strip(string.punctuation) for word in words]
    return processed_words
def read_stop_words(file_path):
    with open(file_path, 'r', encoding='utf-8-sig') as file:
        stop_words = file.read().splitlines()
    return stop_words
def filter_stop_words(words, stop_words):
    return [word for word in words if word not in stop_words]
def count_words(words):
    return Counter(words)
def print_word_counts(word_counts):
    sorted_word_counts = sorted(word_counts.items())
    for word, count in sorted_word_counts:
        print(f'{word}: {count}')
if __name__ == '__main__':
    main()