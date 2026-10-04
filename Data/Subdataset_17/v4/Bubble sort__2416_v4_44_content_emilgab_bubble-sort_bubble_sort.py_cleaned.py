import re
import sys
def data_process(in_file):
    words = []
    try:
        with open(in_file, 'r') as file:
            for word in file.read().split():
                cleaned_word = re.sub(r"\W", "", word).lower()
                if cleaned_word:
                    words.append(cleaned_word)
    except FileNotFoundError:
        print(f"Error: The file '{in_file}' was not found.")
        sys.exit(1)
    return words
def bubble_sort(words):
    n = len(words)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if len(words[j]) > len(words[j + 1]) or (len(words[j]) == len(words[j + 1]) and words[j] > words[j + 1]):
                words[j], words[j + 1] = words[j + 1], words[j]
    return words
if __name__ == "__main__":
    if len(sys.argv) == 2:
        input_file = sys.argv[1]
    else:
        input_file = input("Enter the name of the file: ")
    words = data_process(input_file)
    sorted_words = bubble_sort(words)
    for word in sorted_words:
        print(word)