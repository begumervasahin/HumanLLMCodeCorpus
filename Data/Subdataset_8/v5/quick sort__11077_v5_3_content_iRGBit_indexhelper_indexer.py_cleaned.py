import sys
import string
from collections import Counter
LANGUAGES = ['EN', 'DE']
DEFAULT_LANGUAGE_INDEX = 0
DEFAULT_FILE = 'files/sample.txt'
DEFAULT_STOPWORDS_FILE = f'stopwords/stop_words_{LANGUAGES[DEFAULT_LANGUAGE_INDEX]}.txt'
DEFAULT_OUTPUT_FILE = 'out.txt'
def main():
    language_choice = prompt_language_selection()
    stop_words_file = get_stop_words_file(language_choice)
    output_file = prompt_output_file_name()
    input_file = get_input_file()
    index_words(input_file, stop_words_file, output_file)
def prompt_language_selection():
    print(f"Select Language from the following: {concat(LANGUAGES)} - default is EN: ")
    language = input().upper()
    if language in LANGUAGES:
        return LANGUAGES[LANGUAGES.index(language)]
    else:
        print("Not a valid language. Assuming English...")
        return LANGUAGES[DEFAULT_LANGUAGE_INDEX]
def get_stop_words_file(language):
    return f'stopwords/stop_words_{language}.txt'
def prompt_output_file_name():
    output_file_name = input(f"Select name of output text file (default is {DEFAULT_OUTPUT_FILE}): ")
    if output_file_name == "":
        return DEFAULT_OUTPUT_FILE
    elif output_file_name.endswith('.txt'):
        return output_file_name
    else:
        return output_file_name + '.txt'
def get_input_file():
    if len(sys.argv) > 2:
        print("\nUsage: python indexer.py <yourFile>")
        print(f"If no arguments are given {DEFAULT_FILE} and {DEFAULT_STOPWORDS_FILE} will be used as default files\n")
        sys.exit()
    elif len(sys.argv) == 2:
        return sys.argv[1]
    else:
        return DEFAULT_FILE
def index_words(input_file, stop_words_file, output_file):
    punctuation = set(string.punctuation)
    with open(input_file, 'r') as f:
        book_words = f.read().decode("unicode-escape").encode("ascii", "ignore").lower().split()
        book_words = [el.rstrip(string.punctuation).lstrip(string.punctuation) for el in book_words]
    with open(stop_words_file, 'r') as f:
        stop_words = f.read().decode("utf-8-sig").encode("utf-8").splitlines()
    final_words = [x for x in book_words if x not in stop_words]
    top_words = Counter(final_words)
    frequency = sum(top_words.values())
    frequent = frequency / len(top_words)
    tops = {k: v for (k, v) in top_words.items() if v >= frequent}
    final = sorted(tops.items(), key=lambda x: x[0])
    with open(output_file, 'w+') as out_file:
        for word, count in final:
            print(f'{word}: {count}', file=out_file)
def concat(items):
    return " ".join(items)
if __name__ == '__main__':
    main()