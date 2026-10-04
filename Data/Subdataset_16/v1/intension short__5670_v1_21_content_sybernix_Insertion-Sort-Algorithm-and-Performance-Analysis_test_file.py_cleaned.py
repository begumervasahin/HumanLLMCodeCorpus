from is_140422H import InsertionSort
def fonk1(number_list):
    print('Unsorted list:', number_list)
    b1 = InsertionSort(number_list)
    print('Sorted list:', b1)
    b2 = all(b1[i] <= b1[i + 1] for i in range(len(b1) - 1))
    if b2 and set(number_list) == set(b1):
        print("Answer is the correct sorted list.")
    else:
        print("Answer is not the correct sorted list.")
    print()
if b3 = = "__main__":
    b4 = [20, 12, 8, 5, 7, 10, 14]
    b5 = [20, -7, 10, 14]
    b6 = []
    b7 = [0, 0, 0]
    b8 = [b4, b5, b6, b7]
    for lis in b8:
        fonk1(lis)