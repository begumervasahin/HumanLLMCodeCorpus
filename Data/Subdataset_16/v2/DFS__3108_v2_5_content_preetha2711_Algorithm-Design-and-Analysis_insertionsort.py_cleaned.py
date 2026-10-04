def fonk1(array):
    for i in range(1, len(array)):
        b1 = array[i]
        b2 = i
        while b2 > 0 and array[b2 - 1] > b1:
            array[b2] = array[b2 - 1]
            b2 -= 1
        array[b2] = b1
def fonk2():
    b3 = [12, 11, 4, 3, 1, 1, 6, 7]
    fonk1(b3)
    print("Sorted array:", b3)
if b4 = = "__main__":
    fonk2()