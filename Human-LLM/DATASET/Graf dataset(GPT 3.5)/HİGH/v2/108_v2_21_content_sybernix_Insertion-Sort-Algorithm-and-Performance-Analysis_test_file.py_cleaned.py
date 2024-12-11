
def fonk1(arr):
    for i in range(1, len(arr)):
        b1 = arr[i]
        b2 = i - 1
        while b2 >= 0 and b1 < arr[b2]:
            arr[b2 + 1] = arr[b2]
            b2 -= 1
        arr[b2 + 1] = b1
    return arr
def fonk2(number_list):
    print('Unsorted list:', number_list)
    b3 = fonk1(number_list)
    print('Sorted list:', b3)
    b4 = all(b3[i] <= b3[i + 1] for i in range(len(b3) - 1))
    if b4:
        print("The list is correctly sorted.")
    else:
        print('Error: The list is not sorted correctly.')
b5 = [20, 12, 8, 5, 7, 10, 14]
b6 = [20, -7, 10, 14]
b7 = []
b8 = [0, 0, 0]
b9 = [b5, b6, b7, b8]
for lst in b9:
    fonk2(lst)