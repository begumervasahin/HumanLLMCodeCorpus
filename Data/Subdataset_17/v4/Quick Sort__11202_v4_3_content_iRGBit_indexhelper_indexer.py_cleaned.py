import sys
import string
from collections import Counter
import numpy as np
LANGUAGES = ['EN', 'DE']
DEFAULT_LANGUAGE_INDEX = 0
DEFAULT_FILE = 'files/sample.txt'
DEFAULT_STOPWORDS = f'stopwords/stop_words_{LANGUAGES[DEFAULT_LANGUAGE_INDEX]}.txt'
DEFAULT_OUTPUT_FILE = 'out.txt'
def main():
    selected_language = get_language()
    stopwords_file = get_stopwords_file(selected_language)
    output_file = get_output_file()
    print(f"Using '{DEFAULT_FILE}' as file and '{stopwords_file}' as stop word reference, printing to '{output_file}'.\n")
    if len(sys.argv) > 2:
        print("\nUsage: python indexer.py <yourFile>")
        print(f"If no arguments are given, '{DEFAULT_FILE}' and '{DEFAULT_STOPWORDS}' will be used as default files.\n")
        sys.exit()
    elif len(sys.argv) == 2:
        input_file = sys.argv[1]
    else:
        input_file = DEFAULT_FILE
    index_text(input_file, stopwords_file, output_file)
def get_language():
    languages_str = " ".join(LANGUAGES)
    prompt = f"Select Language from the following ({languages_str}) - default is EN: "
    user_input = input(prompt).upper()
    if user_input in LANGUAGES:
        print(f"Parsing your text with the {user_input} stopwords.")
        return user_input
    else:
        print("Not a valid language. Assuming English...")
        return LANGUAGES[DEFAULT_LANGUAGE_INDEX]
def get_stopwords_file(language):
    return f'stopwords/stop_words_{language}.txt'
def get_output_file():
    prompt = f"Select name of output text file (default is {DEFAULT_OUTPUT_FILE}): "
    user_input = input(prompt)
    if not user_input:
        return DEFAULT_OUTPUT_FILE
    elif user_input.endswith('.txt'):
        return user_input
    else:
        return f'{user_input}.txt'
def index_text(input_file, stopwords_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read().lower()
    with open(stopwords_file, 'r', encoding='utf-8-sig') as file:
        stopwords = file.read().splitlines()
    words = [
        word.strip(string.punctuation)
        for word in text.split()
    ]
    filtered_words = [word for word in words if word and word not in stopwords]
    word_counts = Counter(filtered_words)
    total_words = sum(word_counts.values())
    average_frequency = total_words / len(word_counts)
    frequent_words = {word: count for word, count in word_counts.items() if count >= average_frequency}
    sorted_frequent_words = sorted(frequent_words.items())
    with open(output_file, 'w', encoding='utf-8') as file:
        for word, count in sorted_frequent_words:
            file.write(f'{word}: {count}\n')
if __name__ == '__main__':
    main()