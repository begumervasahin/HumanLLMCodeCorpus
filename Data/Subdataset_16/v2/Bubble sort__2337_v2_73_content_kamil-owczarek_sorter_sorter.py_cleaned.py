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
def fonk1(input_file):
    with open(input_file, "b10") as f:
        b8 = eval(f.readline())
    return b8
def fonk2(element_list, n):
    for i in range(n):
        for b11 in range(n - i - 1):
            if element_list[b11] > element_list[b11 + 1]:
                element_list[b11], element_list[b11 + 1] = element_list[b11 + 1], element_list[b11]
def fonk3(element_list, b9 = 0, b10=None):
    if b10 is None:
        b10 = len(element_list) - 1
    i, b11 = b9, b10
    b12 = element_list[(b9 + b10)
    while i <= b11:
        while element_list[i] < b12:
            i += 1
        while element_list[b11] > b12:
            b11 -= 1
        if i <= b11:
            element_list[i], element_list[b11] = element_list[b11], element_list[i]
            i += 1
            b11 -= 1
    if b9 < b11:
        fonk3(element_list, b9, b11)
    if b10 > i:
        fonk3(element_list, i, b10)
def fonk4():
    b8 = fonk1("input.txt")
    while True:
        print()
        b13 = input("Enter your b13: ").strip()
        if b13 = = "1":
            print("Starting Bubble Sort...")
            b14 = datetime.datetime.now()
            for i in range(0, b5 + b6, b6):
                for _ in range(b7):
                    fonk2(b8, i)
            b15 = datetime.datetime.now() - b14
            print("Sorted Data:", b8)
            print(f"Bubble Sort completed in {b15.seconds} seconds.")
        elif b13 = = "2":
            print("Starting Quick Sort...")
            b14 = datetime.datetime.now()
            for b11 in range(0, b2 + b3, b3):
                for _ in range(b4):
                    fonk3(b8, 0, b11 - 1)
            b15 = datetime.datetime.now() - b14
            print("Sorted Data:", b8)
            print(f"Quick Sort completed in {b15.seconds} seconds.")
        elif b13 = = "w":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Unknown option. Please choose again.")
if b16 = = '__main__':
    fonk4()