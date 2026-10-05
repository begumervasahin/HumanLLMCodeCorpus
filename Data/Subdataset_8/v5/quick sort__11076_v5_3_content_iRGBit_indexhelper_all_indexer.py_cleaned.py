import sys
import string
from collections import Counter
DEFAULT_FILE = 'files/sample.txt'
DEFAULT_STOP_WORDS = 'stop_words.txt'
def main():
    if len(sys.argv) > 3:
        print("Usage: python indexer.py <yourFile> <stopWords>")
        print("If no arguments are given, {} and {} will be used as default files".format(DEFAULT_FILE, DEFAULT_STOP_WORDS))
        sys.exit()
    your_file, your_stop_words = get_file_and_stop_words()
    print('Using {} as file and {} as stop word reference.'.format(your_file, your_stop_words))
    print()
    index_words(your_file, your_stop_words)
def get_file_and_stop_words():
    if len(sys.argv) == 3:
        return sys.argv[1], sys.argv[2]
    elif len(sys.argv) == 2:
        return sys.argv[1], DEFAULT_STOP_WORDS
    else:
        return DEFAULT_FILE, DEFAULT_STOP_WORDS
def index_words(your_file, your_stop_words):
    punct = set(string.punctuation)
    with open(your_file) as file:
        book_words = file.read().lower().split()
        book_words = [el.rstrip(string.punctuation).lstrip(string.punctuation) for el in book_words]
    with open(your_stop_words) as file:
        stop_words = file.read().splitlines()
    final_words = [x for x in book_words if x not in stop_words]
    top_words = Counter(final_words)
    final = sorted(top_words.items(), key=lambda x: x[0])
    for word, count in final:
        print('{}: {}'.format(word, count))
if __name__ == '__main__':
    main()