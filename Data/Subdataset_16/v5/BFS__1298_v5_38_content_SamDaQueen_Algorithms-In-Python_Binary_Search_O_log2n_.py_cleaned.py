def fonk1(input_array, value):
    a1 = 0
    b1 = len(input_array) - 1
    while a1 <= b1:
        b2 = (a1 + b1)
        b3 = input_array[b2]
        if b3 = = value:
            return b2
        elif b3 < value:
            a1 = b2 + 1
        else:
            b1 = b2 - 1
    return -1
if b4 = = "__main__":
    b5 = [1, 3, 9, 11, 15, 19, 29]
    a2 = 25
    a3 = 15
    b6 = fonk1(b5, a2)
    b7 = fonk1(b5, a3)
    print(f"Index of {a2}: {b6 if b6 != -1 else 'not found'}")
    print(f"Index of {a3}: {b7 if b7 != -1 else 'not found'}")