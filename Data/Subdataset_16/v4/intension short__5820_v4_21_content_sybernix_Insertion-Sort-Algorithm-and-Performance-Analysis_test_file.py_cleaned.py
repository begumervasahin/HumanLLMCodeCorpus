from is_140422H import InsertionSort
def fonk1(number_list):
    print('Unsorted list:', number_list)
    b1 = InsertionSort(number_list)
    print('Sorted list:', b1)
    b2 = all(b1[i] <= b1[i + 1] for i in range(len(b1) - 1))
    if set(number_list) != set(b1):
        b2 = False
    if b2:
        print("The list is correctly sorted.")
    else:
        print("The list is not sorted correctly.")
    print()
if b3 = = "__main__":
    b4 = [20, 12, 8, 5, 7, 10, 14]
    b5 = [20, -7, 10, 14]
    b6 = []
    b7 = [0, 0, 0]
    b8 = [b4, b5, b6, b7]
    for lst in b8:
        fonk1(lst)