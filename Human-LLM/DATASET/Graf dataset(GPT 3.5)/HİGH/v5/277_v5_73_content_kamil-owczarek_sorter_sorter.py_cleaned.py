import datetime
from configparser import ConfigParser
b1 = ConfigParser()
b1.read('b1.ini')
b2 = b1['quicksort']
b3 = b1['bubblesort']
b4 = int(b2['elements'])
b5 = int(b2['step'])
b6 = int(b2['iter'])
b7 = int(b3['elements'])
b8 = int(b3['step'])
b9 = int(b3['iter'])
def fonk1(input_file):
    with open(input_file, "b12") as f:
        b10 = eval(f.readline())
    return b10
def fonk2(element_list, n):
    for i in range(n):
        for b13 in range(n - i - 1):
            if element_list[b13] > element_list[b13 + 1]:
                element_list[b13], element_list[b13 + 1] = element_list[b13 + 1], element_list[b13]
def fonk3(element_list, b11 = 0, b12=None):
    if b12 is None:
        b12 = len(element_list) - 1
    i, b13 = b11, b12
    b14 = (b11 + b12)
    b15 = element_list[b14]
    while i <= b13:
        while element_list[i] < b15:
            i += 1
        while element_list[b13] > b15:
            b13 -= 1
        if i <= b13:
            element_list[i], element_list[b13] = element_list[b13], element_list[i]
            i += 1
            b13 -= 1
    if b11 < b13:
        fonk3(element_list, b11, b13)
    if b12 > i:
        fonk3(element_list, i, b12)
def fonk4():
    b10 = fonk1("input.txt")
    b16 = True
    while b16:
        print()
        b16 = input()
        if b16 = = "1":
            print("Sorting with Bubble Sort")
            b17 = datetime.datetime.now()
            for i in range(0, b7 + b8, b8):
                for x in range(b7):
                    fonk2(b10, i)
            b18 = datetime.datetime.now() - b17
            print(b10)
            print("Sorted in " + str(b18.seconds) + " seconds.")
        elif b16 = = "2":
            print("Sorting with Quick Sort")
            b17 = datetime.datetime.now()
            for b13 in range(0, b4 + b5, b5):
                for i in range(b6):
                    fonk3(b10, 0, b13 - 1)
            b18 = datetime.datetime.now() - b17
            print(b10)
            print("Sorted in " + str(b18.seconds) + " seconds.")
        elif b16 = = "w":
            print("Exiting program.")
            break
        elif b16 != "":
            print("Unknown option")
if b19 = = '__main__':
    fonk4()