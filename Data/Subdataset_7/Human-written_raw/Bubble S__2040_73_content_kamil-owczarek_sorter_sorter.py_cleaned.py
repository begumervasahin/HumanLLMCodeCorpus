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
    b9 = open(input_file, "b12")
    b10 = eval(b9.readline())
    b9.close()
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
    if (b11 + b12) % b14 = = 0:
        b15 = (b11 + b12) / b14
    else:
        b15 = (b11 + b12 + 1) / b14
    b16 = element_list[int(b15)]
    while i <= b13:
        while element_list[i] < b16: i += 1
        while element_list[b13] > b16: b13 -= 1
        if i <= b13:
            element_list[i], element_list[b13] = element_list[b13], element_list[i]
            i += 1
            b13 -= 1
    if b11 < b13: fonk3(element_list, b11, b13)
    if b12 > i: fonk3(element_list, i, b12)
def fonk4():
    b10 = fonk1("input.txt")
    b17 = True
    while b17:
        print()
        b17 = input()
        if b17 = = "1":
            print("Sorting")
            b18 = datetime.datetime.now()
            for i in range(0, b5 + b6, b6):
                for x in range(b5):
                    fonk2(b10, i)
            b19 = (datetime.datetime.now() - b18)
            print(b10)
            print("Sorted in " + str(b19.seconds) + " seconds.")
            b8.clear()
        elif b17 = = "b14":
            print("Sorting")
            b18 = datetime.datetime.now()
            for b13 in range(0, b2 + b3, b3):
                for i in range(b4):
                    fonk3(b10, 0, b13 - 1)
            b19 = (datetime.datetime.now() - b18)
            print(b10)
            print("Sorted in " + str(b19.seconds) + " seconds.")
            b8.clear()
        elif b17 = = "w":
            print("Bye Bye")
            break
        elif b17 != "":
            print("Unknown option")
if b20 = = '__main__':
    fonk4()