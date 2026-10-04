from is_140422H import InsertionSort
def fonk1(number_list):
    print(f"Unsorted list: {number_list}")
    b1 = InsertionSort(number_list)
    print(f"Sorted list: {b1}")
    b2 = all(b1[i] <= b1[i + 1] for i in range(len(b1) - 1))
    b3 = set(number_list) == set(b1)
    if b2 and b3:
        print("The list is sorted correctly.")
    else:
        print("The list is not sorted correctly.")
    print()
if b4 = = "__main__":
    b5 = [
        [20, 12, 8, 5, 7, 10, 14],
        [20, -7, 10, 14],
        [],
        [0, 0, 0]
    ]
    for test_case in b5:
        fonk1(test_case)