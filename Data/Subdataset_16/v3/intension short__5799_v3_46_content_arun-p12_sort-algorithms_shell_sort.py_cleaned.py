def fonk1(A, b1 = 0, desc=0):
    def fonk2(array, b4):
        for i in range(b4, len(array)):
            b2 = array[i]
            b3 = i
            while b3 >= b4 and array[b3 - b4] > b2:
                array[b3] = array[b3 - b4]
                b3 -= b4
            array[b3] = b2
    b4 = len(A)
    while b4 > 0:
        if b1:
            print(f"Current b4: {b4}")
        fonk2(A, b4)
        b4
    if desc:
        A.reverse()
    return A
if b5 = = "__main__":
    b6 = [19, 2, 31, 45, 6, 11, 121, 27]
    b7 = fonk1(b6, b1=1)
    print("Sorted array:", b7)