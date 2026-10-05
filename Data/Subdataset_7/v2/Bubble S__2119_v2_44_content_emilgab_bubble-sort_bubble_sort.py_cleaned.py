import re
import sys
def fonk1(b5):
    '''
    Reads the file, processes its content, and returns a list of b1.
    Each b3 is converted to lowercase and stripped of punctuation.
    '''
    b1 = []
    try:
        with open(b5, b2 = "r") as file:
            for b3 in file.read().split():
                b3 = re.sub("\W", "", b3).lower()
                b1.append(b3)
    except FileNotFoundError:
        print("File not found")
    return b1
def fonk2(b1):
    '''
    Sorts a list of b1 by length using bubble sort.
    If b1 have equal length, they are sorted lexicographically.
    '''
    for i in range(len(b1) - 1, 0, -1):
        for j in range(i):
            if len(b1[j]) > len(b1[j + 1]):
                b1[j], b1[j + 1] = b1[j + 1], b1[j]
            elif len(b1[j]) == len(b1[j + 1]) and b1[j] > b1[j + 1]:
                b1[j], b1[j + 1] = b1[j + 1], b1[j]
    return b1
if b4 = = "__main__":
    if len(sys.argv) == 2:
        b5 = sys.argv[1]
    else:
        b5 = input("What is the name of the file? ")
    b1 = fonk1(b5)
    b6 = fonk2(b1)
    for b3 in b6:
        print(b3)