import sys
import string
from collections import Counter
default_file = 'files/sample.txt'
default_stop_words = 'stop_words.txt'
def main():
    if len(sys.argv) > 3:
        print("Usage: python indexer.py <yourFile> <stopWords>")
        print("If no arguments are given, {} and {} will be used as default files".format(default_file, default_stop_words))
        sys.exit()
    elif len(sys.argv) == 3:
        your_stop_words = sys.argv[2]
        your_file = sys.argv[1]
    elif len(sys.argv) == 2:
        your_stop_words = default_stop_words
        your_file = sys.argv[1]
    elif len(sys.argv) == 1:
        your_stop_words = default_stop_words
        your_file = default_file
    print('Using {} as file and {} as stop word reference.'.format(your_file, your_stop_words))
    print()
    index_them(your_file, your_stop_words)
def index_them(your_file, your_stop_words):
    punct = set(string.punctuation)
    with open(your_file) as file:
        book_words = file.read().decode("unicode-escape").encode("ascii", "ignore").lower().split()
        book_words = [el.rstrip(string.punctuation).lstrip(string.punctuation) for el in book_words]
    with open(your_stop_words) as file:
        stop_words = file.read().decode("utf-8-sig").encode("utf-8").splitlines()
    final_words = [x for x in book_words if x not in stop_words]
    top_words = Counter(final_words)
    final = sorted(top_words.items(), key=lambda x: x[0])
    for word, count in final:
        print('{}: {}'.format(word, count))
if __name__ == '__main__':
    main()