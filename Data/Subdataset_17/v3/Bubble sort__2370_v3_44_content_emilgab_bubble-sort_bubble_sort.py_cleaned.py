import re
import sys
def data_process(in_file):
    words = []
    try:
        with open(in_file, 'r') as file:
            for word in file.read().split():
                clean_word = re.sub(r"\W", "", word).lower()
                if clean_word:
                    words.append(clean_word)
    except FileNotFoundError:
        print(f"Error: File '{in_file}' not found.")
        sys.exit(1)
    return words
def bubble_sort(word_list):
    n = len(word_list)
    for passnum in range(n - 1, 0, -1):
        for i in range(passnum):
            if (len(word_list[i]) > len(word_list[i + 1])) or \
               (len(word_list[i]) == len(word_list[i + 1]) and word_list[i] > word_list[i + 1]):
                word_list[i], word_list[i + 1] = word_list[i + 1], word_list[i]
    return word_list
if __name__ == "__main__":
    if len(sys.argv) == 2:
        file_name = sys.argv[1]
    else:
        file_name = input("What is the name of the file? ")
    sorted_words = bubble_sort(data_process(file_name))
    for word in sorted_words:
        print(word)