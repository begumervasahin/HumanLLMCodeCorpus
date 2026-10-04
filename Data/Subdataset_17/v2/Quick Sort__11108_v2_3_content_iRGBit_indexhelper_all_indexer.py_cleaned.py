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
    your_file = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_FILE
    your_stop_words = sys.argv[2] if len(sys.argv) > 2 else DEFAULT_STOP_WORDS
    print(f'Using {your_file} as the input file and {your_stop_words} as the stop words reference.\n')
    index_them(your_file, your_stop_words)
def index_them(input_file, stop_words_file):
    with open(input_file, 'r', encoding='unicode_escape') as file:
        book_words = file.read().lower().split()
        book_words = [word.strip(string.punctuation) for word in book_words]
    with open(stop_words_file, 'r', encoding='utf-8-sig') as file:
        stop_words = file.read().splitlines()
    filtered_words = [word for word in book_words if word not in stop_words]
    word_counts = Counter(filtered_words)
    sorted_word_counts = sorted(word_counts.items())
    for word, count in sorted_word_counts:
        print(f'{word}: {count}')
if __name__ == '__main__':
    main()