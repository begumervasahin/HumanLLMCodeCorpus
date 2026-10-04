def fonk1(input_array, value):
    b1 = len(input_array)
    a1 = 0
    b2 = b1
    b3 = b1
    while (value != input_array[b2]) and (b3 >= 0):
        if value < input_array[b2]:
            b1 = b2
            b2 = b2 - (b1 - a1)
        else:
            a1 = b2
            b2 = b2 + (b1 - a1)
        b3 = b3 - 1
    if b3 < 0:
        return -1
    else:
        return b2
if b4 = = "__main__":
    b5 = [1, 3, 9, 11, 15, 19, 29]
    a2 = 25
    a3 = 15
    b6 = fonk1(b5, a2)
    b7 = fonk1(b5, a3)
    print(f"Index of {a2} in the list: {b6}")
    print(f"Index of {a3} in the list: {b7}")