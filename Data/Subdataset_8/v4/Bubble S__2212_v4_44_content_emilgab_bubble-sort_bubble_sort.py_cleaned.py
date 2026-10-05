import re
import sys
def process_data(file_path):
    words = []
    try:
        with open(file_path, mode="r") as file:
            for line in file:
                for word in line.split():
                    word = re.sub(r'\W', '', word).lower()
                    words.append(word)
    except FileNotFoundError:
        print("File not found")
    return words
def bubble_sort_words(word_list):
    for i in range(len(word_list)-1, 0, -1):
        for j in range(i):
            if len(word_list[j]) > len(word_list[j+1]):
                word_list[j], word_list[j+1] = word_list[j+1], word_list[j]
            elif len(word_list[j]) == len(word_list[j+1]) and word_list[j] > word_list[j+1]:
                word_list[j], word_list[j+1] = word_list[j+1], word_list[j]
    return word_list
if __name__ == "__main__":
    try:
        if len(sys.argv) == 2:
            file_path = sys.argv[1]
        else:
            file_path = input("Enter the file path: ")
        sorted_words = bubble_sort_words(process_data(file_path))
        for word in sorted_words:
            print(word)
    except Exception as e:
        print("An error occurred:", e)