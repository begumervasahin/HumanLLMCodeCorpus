import datetime
from configparser import ConfigParser
b1 = 'b3.ini'
b2 = 'input.txt'
def fonk1():
    b3 = ConfigParser()
    b3.read(b1)
    return b3
def fonk2(input_file):
    try:
        with open(input_file, "b7") as f:
            b4 = eval(f.readline())
        return b4
    except FileNotFoundError:
        print("Input file not found.")
        return None
    except Exception as e:
        print("Error reading input file:", e)
        return None
def fonk3(element_list):
    b5 = len(element_list)
    for i in range(b5):
        for j in range(b5 - i - 1):
            if element_list[j] > element_list[j + 1]:
                element_list[j], element_list[j + 1] = element_list[j + 1], element_list[j]
def fonk4(element_list, b6 = 0, b7=None):
    if b7 is None:
        b7 = len(element_list) - 1
def fonk5():
    b3 = fonk1()
    if not b3:
        return
    b4 = fonk2(b2)
    if not b4:
        return
    while True:
        print()
        b8 = input().strip()
        if b8 = = "1":
            print("Bubble Sort:")
            b9 = datetime.datetime.now()
            fonk3(b4[:])
            b10 = datetime.datetime.now()
            print("Sorted:", b4)
            print("Sorted in", (b10 - b9).seconds, "seconds.")
        elif b8 = = "2":
            print("Quick Sort:")
            b9 = datetime.datetime.now()
            fonk4(b4[:])
            b10 = datetime.datetime.now()
            print("Sorted:", b4)
            print("Sorted in", (b10 - b9).seconds, "seconds.")
        elif b8.lower() == "w":
            print("Goodbye!")
            break
        else:
            print("Unknown option")
if b11 = = '__main__':
    fonk5()