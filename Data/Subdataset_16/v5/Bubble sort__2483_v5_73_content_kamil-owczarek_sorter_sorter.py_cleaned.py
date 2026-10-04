import datetime
from configparser import ConfigParser
def fonk1(b1 = 'b2.ini'):
    b2 = ConfigParser()
    b2.read(b1)
    return {
        'quick_sort': {
            'elements': int(b2['quicksort']['elements']),
            'step': int(b2['quicksort']['step']),
            'iterations': int(b2['quicksort']['iter'])
        },
        'bubble_sort': {
            'elements': int(b2['bubblesort']['elements']),
            'step': int(b2['bubblesort']['step']),
            'iterations': int(b2['bubblesort']['iter'])
        }
    }
def fonk2(input_file):
    with open(input_file, "b5") as f:
        b3 = eval(f.readline())
    return b3
def fonk3(element_list, n):
    for i in range(n):
        for b6 in range(n - i - 1):
            if element_list[b6] > element_list[b6 + 1]:
                element_list[b6], element_list[b6 + 1] = element_list[b6 + 1], element_list[b6]
def fonk4(element_list, b4 = 0, b5=None):
    if b5 is None:
        b5 = len(element_list) - 1
    i, b6 = b4, b5
    b7 = (b4 + b5)
    b8 = element_list[b7]
    while i <= b6:
        while element_list[i] < b8:
            i += 1
        while element_list[b6] > b8:
            b6 -= 1
        if i <= b6:
            element_list[i], element_list[b6] = element_list[b6], element_list[i]
            i += 1
            b6 -= 1
    if b4 < b6:
        fonk4(element_list, b4, b6)
    if i < b5:
        fonk4(element_list, i, b5)
def fonk5():
    b2 = fonk1()
    b3 = fonk2("input.txt")
    while True:
        print()
        b9 = input("Enter your b9: ").strip()
        if b9 = = "1":
            print("Sorting with Bubble Sort")
            b10 = datetime.datetime.now()
            for i in range(0, b2['bubble_sort']['elements'] + b2['bubble_sort']['step'], b2['bubble_sort']['step']):
                fonk3(b3, i)
            b11 = datetime.datetime.now() - b10
            print(b3)
            print(f"Sorted in {b11.total_seconds()} seconds.")
        elif b9 = = "2":
            print("Sorting with Quick Sort")
            b10 = datetime.datetime.now()
            for b6 in range(0, b2['quick_sort']['elements'] + b2['quick_sort']['step'], b2['quick_sort']['step']):
                for _ in range(b2['quick_sort']['iterations']):
                    fonk4(b3, 0, b6 - 1)
            b11 = datetime.datetime.now() - b10
            print(b3)
            print(f"Sorted in {b11.total_seconds()} seconds.")
        elif b9 = = "w":
            print("Bye Bye")
            break
        else:
            print("Unknown option, please try again.")
if b12 = = '__main__':
    fonk5()