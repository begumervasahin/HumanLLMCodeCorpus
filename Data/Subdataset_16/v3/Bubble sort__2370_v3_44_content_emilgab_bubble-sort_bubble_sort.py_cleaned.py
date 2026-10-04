import re
import sys
def fonk1(in_file):
    b1 = []
    try:
        with open(in_file, 'r') as file:
            for word in file.read().split():
                b2 = re.sub(r"\W", "", word).lower()
                if b2:
                    b1.append(b2)
    except FileNotFoundError:
        print(f"Error: File '{in_file}' not found.")
        sys.exit(1)
    return b1
def fonk2(word_list):
    b3 = len(word_list)
    for passnum in range(b3 - 1, 0, -1):
        for i in range(passnum):
            if (len(word_list[i]) > len(word_list[i + 1])) or \
               (len(word_list[i]) == len(word_list[i + 1]) and word_list[i] > word_list[i + 1]):
                word_list[i], word_list[i + 1] = word_list[i + 1], word_list[i]
    return word_list
if b4 = = "__main__":
    if len(sys.argv) == 2:
        b5 = sys.argv[1]
    else:
        b5 = input("What is the name of the file? ")
    b6 = fonk2(fonk1(b5))
    for word in b6:
        print(word)