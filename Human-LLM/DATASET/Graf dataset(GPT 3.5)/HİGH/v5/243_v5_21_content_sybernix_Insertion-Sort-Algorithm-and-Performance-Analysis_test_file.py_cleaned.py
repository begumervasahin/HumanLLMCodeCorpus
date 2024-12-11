from is_140422H import InsertionSort
def fonk1(input_list):
    print('Unsorted list:', input_list)
    b1 = InsertionSort(input_list)
    print('Sorted list:', b1)
    b2 = all(b1[i] <= b1[i + 1] for i in range(len(b1) - 1))
    if b2:
        print("The list is correctly sorted.")
    else:
        print('Error: The list is not sorted correctly.')
b3 = [20, 12, 8, 5, 7, 10, 14]
b4 = [20, -7, 10, 14]
b5 = []
b6 = [0, 0, 0]
b7 = [b3, b4, b5, b6]
for test_list in b7:
    fonk1(test_list)