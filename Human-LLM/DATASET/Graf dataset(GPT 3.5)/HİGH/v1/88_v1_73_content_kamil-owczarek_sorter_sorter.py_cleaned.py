import datetime
from configparser import ConfigParser
b1 = ConfigParser()
b1.read('b1.ini')
b2 = int(b1['quicksort']['elements'])
b3 = int(b1['quicksort']['step'])
b4 = int(b1['quicksort']['iter'])
b5 = int(b1['bubblesort']['elements'])
b6 = int(b1['bubblesort']['step'])
b7 = int(b1['bubblesort']['iter'])
b8 = []
def fonk1(input_file):
    with open(input_file, "b11") as f:
        b9 = eval(f.readline())
    return b9
def fonk2(element_list, n):
    for i in range(n):
        for b12 in range(n - i - 1):
            if element_list[b12] > element_list[b12 + 1]:
                element_list[b12], element_list[b12 + 1] = element_list[b12 + 1], element_list[b12]
def fonk3(element_list, b10 = 0, b11=None):
    if b11 is None:
        b11 = len(element_list) - 1
    i, b12 = b10, b11
    if (b10 + b11) % b13 = = 0:
        b14 = (b10 + b11)
    else:
        b14 = (b10 + b11 + 1)
    b15 = element_list[b14]
    while i <= b12:
        while element_list[i] < b15:
            i += 1
        while element_list[b12] > b15:
            b12 -= 1
        if i <= b12:
            element_list[i], element_list[b12] = element_list[b12], element_list[i]
            i += 1
            b12 -= 1
    if b10 < b12:
        fonk3(element_list, b10, b12)
    if b11 > i:
        fonk3(element_list, i, b11)
def fonk4():
    b9 = fonk1("input.txt")
    b16 = True
    while b16:
        print()
        b16 = input()
        if b16 = = "1":
            print("Sorting")
            b17 = datetime.datetime.now()
            for i in range(0, b5 + b6, b6):
                for x in range(b7):
                    fonk2(b9[:], i)
            b18 = (datetime.datetime.now() - b17)
            print(b9)
            print("Sorted in " + str(b18.seconds) + " seconds.")
            b8.clear()
        elif b16 = = "b13":
            print("Sorting")
            b17 = datetime.datetime.now()
            for b12 in range(0, b2 + b3, b3):
                for i in range(b4):
                    fonk3(b9[:], 0, b12 - 1)
            b18 = (datetime.datetime.now() - b17)
            print(b9)
            print("Sorted in " + str(b18.seconds) + " seconds.")
            b8.clear()
        elif b16 = = "w":
            print("Bye Bye")
            break
        elif b16 != "":
            print("Unknown option")
if b19 = = '__main__':
    fonk4()