import re
import sys
def fonk1(b5):
    b1 = []
    try:
        with open(b5, b2 = "r") as file:
            for line in file:
                for b3 in line.split():
                    b3 = re.sub(r'\W', '', b3).lower()
                    b1.append(b3)
    except FileNotFoundError:
        print("File not found")
    return b1
def fonk2(word_list):
    for i in range(len(word_list)-1, 0, -1):
        for j in range(i):
            if len(word_list[j]) > len(word_list[j+1]):
                word_list[j], word_list[j+1] = word_list[j+1], word_list[j]
            elif len(word_list[j]) == len(word_list[j+1]) and word_list[j] > word_list[j+1]:
                word_list[j], word_list[j+1] = word_list[j+1], word_list[j]
    return word_list
if b4 = = "__main__":
    try:
        if len(sys.argv) == 2:
            b5 = sys.argv[1]
        else:
            b5 = input("Enter the file path: ")
        b6 = fonk2(fonk1(b5))
        for b3 in b6:
            print(b3)
    except Exception as e:
        print("An error occurred:", e)