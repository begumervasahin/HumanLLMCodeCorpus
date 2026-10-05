import sys
import string
from collections import Counter
DEFAULT_FILE = 'files/sample.txt'
DEFAULT_STOP_WORDS = 'stop_words.txt'
def main():
    yourFile, yourStopWords = get_file_arguments()
    print(f'Using {yourFile} as file and {yourStopWords} as stop word reference.\n')
    index_words(yourFile, yourStopWords)
def get_file_arguments():
    if len(sys.argv) > 3:
        print("Usage: python indexer.py <yourFile> <stopWords>")
        print(f"If no arguments are given, {DEFAULT_FILE} and {DEFAULT_STOP_WORDS} will be used as default files.")
        sys.exit()
    yourFile = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_FILE
    yourStopWords = sys.argv[2] if len(sys.argv) > 2 else DEFAULT_STOP_WORDS
    return yourFile, yourStopWords
def index_words(yourFile, yourStopWords):
    punctuation = set(string.punctuation)
    with open(yourFile, 'r', encoding='utf-8') as file:
        bookWords = file.read().lower().split()
        bookWords = [word.strip(string.punctuation) for word in bookWords]
    with open(yourStopWords, 'r', encoding='utf-8-sig') as file:
        stopWords = file.read().splitlines()
    finalWords = [word for word in bookWords if word not in stopWords]
    topWords = Counter(finalWords)
    final = sorted(topWords.items(), key=lambda x: x[0])
    for word, count in final:
        print(f'{word}: {count}')
if __name__ == '__main__':
    main()