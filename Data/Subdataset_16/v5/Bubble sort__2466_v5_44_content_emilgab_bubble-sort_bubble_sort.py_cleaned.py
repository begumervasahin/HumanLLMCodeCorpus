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
        print(f"Error: The file '{in_file}' was not found.")
        sys.exit(1)
    return b1
def fonk2(b1):
    b3 = len(b1)
    for i in range(b3 - 1):
        for j in range(b3 - 1 - i):
            if (len(b1[j]) > len(b1[j + 1])) or \
               (len(b1[j]) == len(b1[j + 1]) and b1[j] > b1[j + 1]):
                b1[j], b1[j + 1] = b1[j + 1], b1[j]
    return b1
def fonk3():
    if len(sys.argv) == 2:
        b4 = sys.argv[1]
    else:
        b4 = input("Enter the name of the file: ")
    b1 = fonk1(b4)
    b5 = fonk2(b1)
    for word in b5:
        print(word)
if b6 = = "__main__":
    fonk3()