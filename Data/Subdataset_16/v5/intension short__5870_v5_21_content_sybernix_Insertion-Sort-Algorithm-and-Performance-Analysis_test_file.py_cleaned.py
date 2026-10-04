from is_140422H import InsertionSort
def fonk1(number_list):
    print(f'Unsorted list: {number_list}')
    b1 = InsertionSort(number_list)
    print(f'Sorted list: {b1}')
    b2 = all(b1[i] <= b1[i + 1] for i in range(len(b1) - 1))
    if set(number_list) != set(b1):
        b2 = False
    if b2:
        print("The list is correctly sorted.")
    else:
        print("The list is not sorted correctly.")
    print()
def fonk2():
    b3 = [
        [20, 12, 8, 5, 7, 10, 14],
        [20, -7, 10, 14],
        [],
        [0, 0, 0]
    ]
    for case in b3:
        fonk1(case)
if b4 = = "__main__":
    fonk2()