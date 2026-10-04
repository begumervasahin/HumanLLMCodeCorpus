import sys
import string
from collections import Counter
LANGUAGES = ['EN', 'DE']
DEFAULT_LANGUAGE = 'EN'
DEFAULT_FILE = 'files/sample.txt'
DEFAULT_OUT_FILE = 'out.txt'
def get_stopwords_file(language):
    return f'stopwords/stop_words_{language}.txt'
def main():
    selected_language = input(f"Select language from the following: {', '.join(LANGUAGES)} (default is {DEFAULT_LANGUAGE}): ").upper()
    if selected_language in LANGUAGES:
        stopwords_file = get_stopwords_file(selected_language)
        print(f"Parsing your text with the {selected_language} stopwords.")
    else:
        stopwords_file = get_stopwords_file(DEFAULT_LANGUAGE)
        print("Invalid language. Assuming English...")
    output_file = input(f"Select name of output text file (default is {DEFAULT_OUT_FILE}): ")
    if not output_file:
        output_file = DEFAULT_OUT_FILE
    elif not output_file.endswith('.txt'):
        output_file += '.txt'
    print(f"Printing your results to {output_file}.")
    if len(sys.argv) > 2:
        print("\nUsage: python indexer.py <yourFile>")
        print(f"If no arguments are given, {DEFAULT_FILE} and {stopwords_file} will be used as default files.\n")
        sys.exit()
    elif len(sys.argv) == 2:
        input_file = sys.argv[1]
    else:
        input_file = DEFAULT_FILE
    print(f'Using {input_file} as file and {stopwords_file} as stop word reference, printing to {output_file}.\n')
    index_words(input_file, stopwords_file, output_file)
def index_words(input_file, stopwords_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        book_words = file.read().lower().split()
        book_words = [word.strip(string.punctuation) for word in book_words]
    with open(stopwords_file, 'r', encoding='utf-8') as file:
        stopwords = file.read().splitlines()
    final_words = [word for word in book_words if word not in stopwords]
    word_counts = Counter(final_words)
    total_words = sum(word_counts.values())
    average_frequency = total_words / len(word_counts)
    frequent_words = {word: count for word, count in word_counts.items() if count >= average_frequency}
    sorted_frequent_words = sorted(frequent_words.items())
    with open(output_file, 'w') as file:
        for word, count in sorted_frequent_words:
            file.write(f'{word}: {count}\n')
if __name__ == '__main__':
    main()