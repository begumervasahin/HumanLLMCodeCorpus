def fonk1(array):
    for i in range(1, len(array)):
        b1 = array[i]
        b2 = i - 1
        while b2 >= 0 and array[b2] > b1:
            array[b2 + 1] = array[b2]
            b2 -= 1
        array[b2 + 1] = b1
if b3 = = "__main__":
    b4 = [12, 11, 13, 5, 6]
    print("Original array:", b4)
    fonk1(b4)
    print("Sorted array:", b4)