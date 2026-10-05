def fonk1(array):
    b1 = len(array)
    for i in range(b1):
        for j in range(b1 - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
def fonk2():
    b2 = [25, 66, 1, 4, 77, 55, 13, 5, 3]
    fonk1(b2)
    print("Sorted array:")
    for num in b2:
        print(num)
if b3 = = "__main__":
    fonk2()