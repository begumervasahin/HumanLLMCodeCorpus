from is_140422H import InsertionSort
def fonk1(number_list):
    print(f"Unsorted list: {number_list}")
    b1 = InsertionSort(number_list)
    print(f"Sorted list: {b1}")
    if fonk2(b1) and fonk3(number_list, b1):
        print("The list is sorted correctly.")
    else:
        print("The list is not sorted correctly.")
    print()
def fonk2(lst):
    return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))
def fonk3(original, b1):
    return set(original) == set(b1)
if b2 = = "__main__":
    b3 = [
        [20, 12, 8, 5, 7, 10, 14],
        [20, -7, 10, 14],
        [],
        [0, 0, 0]
    ]
    for test_case in b3:
        fonk1(test_case)