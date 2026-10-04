import sys
import string
from collections import Counter
defaultFile = 'files/sample.txt'
defaultStopWords = 'stop_words.txt'
def main():
    if len(sys.argv) > 3:
        print("\nUsage: python indexer.py <yourFile> <stopWords>")
        print(f"If no arguments are given {defaultFile} and {defaultStopWords} will be used as default files\n")
        sys.exit()
    yourFile = sys.argv[1] if len(sys.argv) > 1 else defaultFile
    yourStopWords = sys.argv[2] if len(sys.argv) > 2 else defaultStopWords
    print(f'Using {yourFile} as file and {yourStopWords} as stop word reference.\n')
    index_them(yourFile, yourStopWords)
def index_them(yourFile, yourStopWords):
    with open(yourFile, 'r', encoding='unicode_escape') as file:
        book_words = file.read().lower().split()
        book_words = [word.strip(string.punctuation) for word in book_words]
    with open(yourStopWords, 'r', encoding='utf-8-sig') as file:
        stop_words = file.read().splitlines()
    final_words = [word for word in book_words if word not in stop_words]
    top_words = Counter(final_words)
    sorted_words = sorted(top_words.items())
    for word, count in sorted_words:
        print(f'{word}: {count}')
if __name__ == '__main__':
    main()